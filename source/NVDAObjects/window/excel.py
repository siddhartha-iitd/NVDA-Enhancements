#NVDAObjects/excel.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2014 NVDA Contributors <http://www.nvaccess.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from comtypes import COMError
import comtypes.automation
import wx
import time
import re
import uuid
import collections
import oleacc
import ui
from tableUtils import HeaderCellInfo, HeaderCellTracker
import config
import textInfos
import colors
import eventHandler
import api
from logHandler import log
import gui
import winUser
from displayModel import DisplayModelTextInfo
import controlTypes
from . import Window
from .. import NVDAObjectTextInfo
import scriptHandler
import inputCore
import virtualBuffers
import browseMode

xlCenter=-4108
xlJustify=-4130
xlLeft=-4131
xlRight=-4152
xlDistributed=-4117
xlBottom=-4107
xlTop=-4160
xlToLeft=-4159
xlFormulas=-4123
xlPart=2
xlByColumns=2
xlPrevious=2
xlUp=-4162

alignmentLabels={
	xlCenter:"center",
	xlJustify:"justify",
	xlLeft:"left",
	xlRight:"right",
	xlDistributed:"distributed",
	xlBottom:"botom",
	xlTop:"top",
	1:"default",
}

xlA1 = 1
xlRC = 2
xlUnderlineStyleNone=-4142

#Excel cell types
xlCellTypeAllFormatConditions =-4172      # from enum XlCellType
xlCellTypeAllValidation       =-4174      # from enum XlCellType
xlCellTypeBlanks              =4          # from enum XlCellType
xlCellTypeComments            =-4144      # from enum XlCellType
xlCellTypeConstants           =2          # from enum XlCellType
xlCellTypeFormulas            =-4123      # from enum XlCellType
xlCellTypeLastCell            =11         # from enum XlCellType
xlCellTypeSameFormatConditions=-4173      # from enum XlCellType
xlCellTypeSameValidation      =-4175      # from enum XlCellType
xlCellTypeVisible             =12         # from enum XlCellType

re_RC=re.compile(r'R(?:\[(\d+)\])?C(?:\[(\d+)\])?')
re_absRC=re.compile(r'^R(\d+)C(\d+)(?::R(\d+)C(\d+))?$')

class ExcelQuickNavItem(browseMode.QuickNavItem):

	def __init__( self , nodeType , document , itemObject , itemCollection ):
		self.excelItemObject = itemObject
		self.excelItemCollection = itemCollection 
		super( ExcelQuickNavItem ,self).__init__( nodeType , document )

	def activate(self):
		pass

	def isChild(self,parent):
		return False

	def report(self,readUnit=None):
		pass

class ExcelChartQuickNavItem(ExcelQuickNavItem):

	def __init__( self , nodeType , document , chartObject , chartCollection ):
		self.chartIndex = chartObject.Index
		if chartObject.Chart.HasTitle:

			self.label = chartObject.Chart.ChartTitle.Text + " " + chartObject.TopLeftCell.address(False,False,1,False) + "-" + chartObject.BottomRightCell.address(False,False,1,False) 

		else:

			self.label = chartObject.Name + " " + chartObject.TopLeftCell.address(False,False,1,False) + "-" + chartObject.BottomRightCell.address(False,False,1,False) 

		super( ExcelChartQuickNavItem ,self).__init__( nodeType , document , chartObject , chartCollection )

	def __lt__(self,other):
		return self.chartIndex < other.chartIndex

	def moveTo(self):
		try:
			self.excelItemObject.Activate()

			# After activate(), though the chart object is selected, 

			# pressing arrow keys moves the object, rather than 

			# let use go inside for sub-objects. Somehow 
		# calling an COM function on a different object fixes that !

			log.debugWarning( self.excelItemCollection.Count )

		except(COMError):

			pass
		focus=api.getDesktopObject().objectWithFocus()
		if not focus or not isinstance(focus,ExcelBase):
			return
		# Charts are not yet automatically detected with objectFromFocus, so therefore use selection
		sel=focus._getSelection()
		if not sel:
			return
		eventHandler.queueEvent("gainFocus",sel)


	@property
	def isAfterSelection(self):
		activeCell = self.document.Application.ActiveCell
		#log.debugWarning("active row: {} active column: {} current row: {} current column: {}".format ( activeCell.row , activeCell.column , self.excelCommentObject.row , self.excelCommentObject.column   ) )

		if self.excelItemObject.TopLeftCell.row == activeCell.row:
			if self.excelItemObject.TopLeftCell.column > activeCell.column:
				return False
		elif self.excelItemObject.TopLeftCell.row > activeCell.row:
			return False
		return True

class ExcelRangeBasedQuickNavItem(ExcelQuickNavItem):

	def __lt__(self,other):
		if self.excelItemObject.row == other.excelItemObject.row:
			return self.excelItemObject.column < other.excelItemObject.column
		else:
			return self.excelItemObject.row < other.excelItemObject.row

	def moveTo(self):
		self.excelItemObject.Activate()
		eventHandler.queueEvent("gainFocus",api.getDesktopObject().objectWithFocus())

	@property
	def isAfterSelection(self):
		activeCell = self.document.Application.ActiveCell
		log.debugWarning("active row: {} active column: {} current row: {} current column: {}".format ( activeCell.row , activeCell.column , self.excelItemObject.row , self.excelItemObject.column   ) )

		if self.excelItemObject.row == activeCell.row:
			if self.excelItemObject.column > activeCell.column:
				return False
		elif self.excelItemObject.row > activeCell.row:
			return False
		return True

class ExcelCommentQuickNavItem(ExcelRangeBasedQuickNavItem):

	def __init__( self , nodeType , document , commentObject , commentCollection ):
		self.label = commentObject.address(False,False,1,False) + " " + commentObject.Comment.Text()
		super( ExcelCommentQuickNavItem , self).__init__( nodeType , document , commentObject , commentCollection )

class ExcelFormulaQuickNavItem(ExcelRangeBasedQuickNavItem):

	def __init__( self , nodeType , document , formulaObject , formulaCollection ):
		self.label = formulaObject.address(False,False,1,False) + " " + formulaObject.Formula
		super( ExcelFormulaQuickNavItem , self).__init__( nodeType , document , formulaObject , formulaCollection )

class ExcelQuicknavIterator(object):
	"""
	Allows iterating over an MS excel collection (e.g. Comments, Formulas or charts) emitting L{QuickNavItem} objects.
	"""

	def __init__(self, itemType , document , direction , includeCurrent):
		"""
		See L{QuickNavItemIterator} for itemType, document and direction definitions.
		@ param includeCurrent: if true then any item at the initial position will be also emitted rather than just further ones. 
		"""
		self.document=document
		self.itemType=itemType
		self.direction=direction if direction else "next"
		self.includeCurrent=includeCurrent

	def collectionFromWorksheet(self,worksheetObject):
		"""
		Fetches a Microsoft Excel collection object from a Microsoft excel worksheet object. E.g. charts, comments, or formula.
		@param worksheetObject: a Microsoft excel worksheet object.
		@return: a Microsoft excel collection object.
		"""
		raise NotImplementedError

	def filter(self,item):
		"""
		Only allows certain items from a collection to be emitted. E.g. a chart .
		@param item: an item from a Microsoft excel collection (e.g. chart object).
		@return True if this item should be allowed, false otherwise.
		@rtype: bool
		"""
		return True

	def iterate(self):
		"""
		returns a generator that emits L{QuickNavItem} objects for this collection.
		"""
		items=self.collectionFromWorksheet(self.document)
		if not items:
			return
		if self.direction=="previous":
			items=reversed(items)
		for collectionItem in items:
			item=self.quickNavItemClass(self.itemType,self.document,collectionItem , items )
			if not self.filter(collectionItem):
				continue
			yield item

class ChartExcelCollectionQuicknavIterator(ExcelQuicknavIterator):
	quickNavItemClass=ExcelChartQuickNavItem#: the QuickNavItem class that should be instantiated and emitted. 
	def collectionFromWorksheet( self , worksheetObject ):
		return worksheetObject.ChartObjects() 

class CommentExcelCollectionQuicknavIterator(ExcelQuicknavIterator):
	quickNavItemClass=ExcelCommentQuickNavItem#: the QuickNavItem class that should be instantiated and emitted. 
	def collectionFromWorksheet( self , worksheetObject ):
		try:
			return  worksheetObject.cells.SpecialCells( xlCellTypeComments )
		except(COMError):

			return None

class FormulaExcelCollectionQuicknavIterator(ExcelQuicknavIterator):
	quickNavItemClass=ExcelFormulaQuickNavItem#: the QuickNavItem class that should be instantiated and emitted. 
	def collectionFromWorksheet( self , worksheetObject ):
		try:
			return  worksheetObject.cells.SpecialCells( xlCellTypeFormulas )
		except(COMError):

			return None

class ExcelBrowseModeTreeInterceptor(browseMode.BrowseModeTreeInterceptor):

	needsReviewCursorTextInfoWrapper=False
	passThrough=True

	def _get_isAlive(self):
		if not winUser.isWindow(self.rootNVDAObject.windowHandle):
			return False
		try:
			return self.rootNVDAObject.excelWorksheetObject.name==self.rootNVDAObject.excelApplicationObject.activeSheet.name
		except (COMError,AttributeError,NameError):
			log.debugWarning("could not compare sheet names",exc_info=True)
			return False


	def __contains__(self,obj):
		return winUser.isDescendantWindow(self.rootNVDAObject.windowHandle,obj.windowHandle)



	def _set_selection(self,info):
		super(ExcelBrowseModeTreeInterceptor,self)._set_selection(info)
		#review.handleCaretMove(info)

	def _get_ElementsListDialog(self):
		return ElementsListDialog

	def _iterNodesByType(self,nodeType,direction="next",pos=None):
		if nodeType=="chart":
			return ChartExcelCollectionQuicknavIterator( nodeType , self.rootNVDAObject.excelWorksheetObject , direction , None ).iterate()
		elif nodeType=="comment":
			return CommentExcelCollectionQuicknavIterator( nodeType , self.rootNVDAObject.excelWorksheetObject , direction , None ).iterate()
		elif nodeType=="formula":
			return FormulaExcelCollectionQuicknavIterator( nodeType , self.rootNVDAObject.excelWorksheetObject , direction , None ).iterate()
		else:
			raise NotImplementedError

	def script_elementsList(self,gesture):
		super(ExcelBrowseModeTreeInterceptor,self).script_elementsList(gesture)
	# Translators: the description for the elements list dialog script on virtualBuffers.
	script_elementsList.__doc__ = _("Presents a list of links, headings or landmarks")
	script_elementsList.ignoreTreeInterceptorPassThrough=True

	def scriptHelper(self,direction):
		self.excelApplicationObject = self.rootNVDAObject.excelWorksheetObject.Application
		ws = self.rootNVDAObject.excelWorksheetObject
		try:
			getattr(self, 'cellPosition')
		except AttributeError:
			self.cellPosition = self.excelApplicationObject.ActiveCell

		currentColumn = self.cellPosition.Column
		currentRow = self.cellPosition.Row
		lastRow = ws.Cells(ws.Rows.Count, currentColumn).End(xlUp).Row
		lastColumn = ws.Cells(currentRow, ws.Columns.Count).End(xlToLeft).Column 

		if   direction == "left":
			self.cellPosition = self.cellPosition.Offset(0,-1)
		elif direction == "right":
			self.cellPosition = self.cellPosition.Offset(0,1)
		elif direction == "up":
			self.cellPosition = self.cellPosition.Offset(-1,0)
		elif direction == "down":
			self.cellPosition = self.cellPosition.Offset(1,0)
		#Start-of-Column
		elif direction == "startcol":
			rowOffset = 1- currentRow
			self.cellPosition = self.cellPosition.Offset(rowOffset,0)
		#Start-of-Row
		elif direction == "startrow":
			columnOffset = 1 - currentColumn
			self.cellPosition = self.cellPosition.Offset(0,columnOffset)
		#End-of-Row
		elif direction == "endrow":
			columnOffset = lastColumn - currentColumn
			self.cellPosition = self.cellPosition.Offset(0,columnOffset)
		#End-of-Column
		elif direction == "endcol":
			rowOffset = lastRow - currentRow
			self.cellPosition = self.cellPosition.Offset(rowOffset,0)
		else:
			return
		
		if self.cellPosition.MergeCells:
			self.cellPosition = self.cellPosition.MergeArea.Cells(1)
			cellLocationText = self.cellPosition.MergeArea.Address().replace('$','')
		else:
			cellLocationText = self.cellPosition.Address().replace('$','')
		
		cellValueText = self.cellPosition.Text
		if cellValueText:
			ui.message(cellValueText)
		ui.message(cellLocationText)
		
		if not self.cellPosition.Locked :
			ui.message("Editable")
		
	def script_moveLeft(self,gesture):
		self.scriptHelper("left")
	
	def script_moveRight(self,gesture):
		self.scriptHelper("right")

	def script_moveUp(self,gesture):
		self.scriptHelper("up")

	def script_moveDown(self,gesture):
		self.scriptHelper("down")
	
	def getColumnNameFromNumber(self,colNum):
		colList = (self.rootNVDAObject.excelWorksheetObject.Cells(1, colNum).Address(True, False)).split('$')
		return ''.join(colList)[:-1]

	def script_readRow(self,gesture):
		self.scriptHelper(-1)
		ws = self.rootNVDAObject.excelWorksheetObject
		currentRow = self.cellPosition.Row
		ui.message(_("Reading Row {0}".format(currentRow)))
		lastColumn = ws.Cells(currentRow, ws.Columns.Count).End(xlToLeft).Column
		col = 1
		while col <= lastColumn:
			if ws.Cells(currentRow,col).MergeCells:
				mergedAreaColumnCount = ws.Cells(currentRow,col).MergeArea.columns.count
				locationText = _("Column {0} to {1}".format(self.getColumnNameFromNumber(col),self.getColumnNameFromNumber(col+mergedAreaColumnCount-1))) if mergedAreaColumnCount > 1 else _("Column {0}".format(self.getColumnNameFromNumber(col)))				
				cellValueText = ws.Cells(currentRow,col).Text
				col += mergedAreaColumnCount
			else:
				locationText = _("Column {0}".format(self.getColumnNameFromNumber(col)))
				cellValueText = ws.Cells(currentRow,col).Text
				col += 1
			ui.message(locationText)
			ui.message(cellValueText)

	def script_readColumn(self,gesture):
		self.scriptHelper(-1)
		ws = self.rootNVDAObject.excelWorksheetObject
		currentCol = self.cellPosition.Column
		ui.message(_("Reading Column {0}".format(self.getColumnNameFromNumber(currentCol))))
		lastRow = ws.Cells(ws.Rows.Count, currentCol).End(xlUp).Row
		row = 1
		while row <= lastRow:
			if ws.Cells(row,currentCol).MergeCells:
				mergedAreaRowCount = ws.Cells(row,currentCol).MergeArea.rows.count
				locationText = _("Row {0} to {1}".format(row,row+mergedAreaRowCount-1)) if mergedAreaRowCount > 1 else _("Row {0}".format(row)) 
				cellValueText = ws.Cells(row,currentCol).Text
				row += mergedAreaRowCount
			else:
				locationText = _("Row {0}".format(row)) 
				cellValueText = ws.Cells(row,currentCol).Text
				row += 1
			ui.message(locationText)
			ui.message(cellValueText)

	def script_startOfColumn(self,gesture):
		self.scriptHelper("startcol")

	def script_startOfRow(self,gesture):
		self.scriptHelper("startrow")

	def script_endOfRow(self,gesture):
		self.scriptHelper("endrow")

	def script_endOfColumn(self,gesture):
		self.scriptHelper("endcol")

	def script_activatePosition(self,gesture):
		rowNum = self.cellPosition.Row
		colNum = self.cellPosition.Column
		log.io("\nRow is " + str(rowNum) + "\n")
		log.io("\nColumn is " + str(colNum) + "\n")
		focus = api.getFocusObject()
		vbuf = focus.treeInterceptor
		if not vbuf:
			# #2023: Search the focus and its ancestors for an object for which browse mode is optional.
			for obj in itertools.chain((api.getFocusObject(),), reversed(api.getFocusAncestors())):
				if obj.shouldCreateTreeInterceptor:
					continue
				try:
					obj.treeInterceptorClass
				except:
					continue
				break
			else:
				return
			# Force the tree interceptor to be created.
			obj.shouldCreateTreeInterceptor = True
			ti = treeInterceptorHandler.update(obj)
			if not ti:
				return
			if focus in ti:
				# Update the focus, as it will have cached that there is no tree interceptor.
				focus.treeInterceptor = ti
				# If we just happened to create a browse mode TreeInterceptor
				# Then ensure that browse mode is reported here. From the users point of view, browse mode was turned on.
				if isinstance(ti,browseMode.BrowseModeTreeInterceptor) and not ti.passThrough:
					browseMode.reportPassThrough(ti,False)
					braille.handler.handleGainFocus(ti)
			return

		if not isinstance(vbuf, browseMode.BrowseModeTreeInterceptor):
			return
		# Toggle browse mode pass-through.
		vbuf.passThrough = not vbuf.passThrough
		if isinstance(vbuf,virtualBuffers.VirtualBuffer):
			# If we are enabling pass-through, the user has explicitly chosen to do so, so disable auto-pass-through.
			# If we're disabling pass-through, re-enable auto-pass-through.
			vbuf.disableAutoPassThrough = vbuf.passThrough
		browseMode.reportPassThrough(vbuf)
# 		activeSheet = self.excelApplicationObject.ActiveSheet
# 		newFocusObject = self.excelApplicationObject.Cells(rowNum,colNum) 
# 		self.excelApplicationObject.Cells(rowNum,colNum).Select
		self.excelCellObject = self.excelApplicationObject.Cells(rowNum,colNum)
		eventHandler.queueEvent("gainFocus",ExcelCell(windowHandle=self.rootNVDAObject.windowHandle,excelWindowObject=self.rootNVDAObject.excelWindowObject,excelCellObject=self.excelCellObject) )
# 		newFocus = posn.Activate
# 		api.setFocusObject(newFocusObject)
# 		newFocus=self.excelApplicationObject.ActiveCell
# 		if eventHandler.lastQueuedFocusObject is newFocus: return
# 		eventHandler.queueEvent("gainFocus",newFocus)

	# Translators: Input help mode message for toggle focus and browse mode command in web browsing and other situations.
	script_activatePosition.__doc__=_("Toggles between browse mode and focus mode. When in focus mode, keys will pass straight through to the application, allowing you to interact directly with a control. When in browse mode, you can navigate the document with the cursor, quick navigation keys, etc.")
	script_activatePosition.category=inputCore.SCRCAT_BROWSEMODE

	__gestures = {
		"kb:upArrow": "moveUp",
		"kb:downArrow":"moveDown",
		"kb:leftArrow":"moveLeft",
		"kb:rightArrow":"moveRight",
		"kb:NVDA+r":"readRow",
		"kb:NVDA+c":"readColumn",
		"kb:control+upArrow":"startOfColumn",
		"kb:control+downArrow":"endOfColumn",
		"kb:control+leftArrow":"startOfRow",
		"kb:control+rightArrow":"endOfRow",
		"kb:enter": "activatePosition",
		"kb:space": "activatePosition",
	}

class ElementsListDialog(browseMode.ElementsListDialog):

	ELEMENT_TYPES=(
		# Translators: The label of a radio button to select the type of element
		# in the browse mode Elements List dialog.
		("chart", _("&Chart")),
		# Translators: The label of a radio button to select the type of element
		# in the browse mode Elements List dialog.
		("comment", _("&Comment")),
		# Translators: The label of a radio button to select the type of element
		# in the browse mode Elements List dialog.
		("formula", _("&Formula")),
	)

class ExcelBase(Window):
	"""A base that all Excel NVDAObjects inherit from, which contains some useful methods."""

	@staticmethod
	def excelWindowObjectFromWindow(windowHandle):
		try:
			pDispatch=oleacc.AccessibleObjectFromWindow(windowHandle,winUser.OBJID_NATIVEOM,interface=comtypes.automation.IDispatch)
		except (COMError,WindowsError):
			return None
		return comtypes.client.dynamic.Dispatch(pDispatch)

	@staticmethod
	def getCellAddress(cell, external=False,format=xlA1):
		text=cell.Address(False, False, format, external)
		textList=text.split(':')
		if len(textList)==2:
			# Translators: Used to express an address range in excel.
			text=_("{start} through {end}").format(start=textList[0], end=textList[1])
		return text

	def _getDropdown(self):
		w=winUser.getAncestor(self.windowHandle,winUser.GA_ROOT)
		if not w:
			log.debugWarning("Could not get ancestor window (GA_ROOT)")
			return
		obj=Window(windowHandle=w,chooseBestAPI=False)
		if not obj:
			log.debugWarning("Could not instnaciate NVDAObject for ancestor window")
			return
		threadID=obj.windowThreadID
		while not eventHandler.isPendingEvents("gainFocus"):
			obj=obj.previous
			if not obj or not isinstance(obj,Window) or obj.windowThreadID!=threadID:
				log.debugWarning("Could not locate dropdown list in previous objects")
				return
			if obj.windowClassName=='EXCEL:':
				break
		return obj

	def _getSelection(self):
		selection=self.excelWindowObject.Selection
		try:
			isMerged=selection.mergeCells
		except (COMError,NameError):
			isMerged=False

		try:
			numCells=selection.count
		except (COMError,NameError):
			numCells=0

		isChartActive = True if self.excelWindowObject.ActiveChart else False
		obj=None
		if isMerged:
			obj=ExcelMergedCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=selection.item(1))
		elif numCells>1:
			obj=ExcelSelection(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelRangeObject=selection)
		elif numCells==1:
			obj=ExcelCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=selection)
		elif isChartActive:
			selection = self.excelWindowObject.ActiveChart
			import excelChart
			obj=excelChart.ExcelChart(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelChartObject=selection)
		return obj


class Excel7Window(ExcelBase):
	"""An overlay class for Window for the EXCEL7 window class, which simply bounces focus to the active excel cell."""

	def _get_excelWindowObject(self):
		return self.excelWindowObjectFromWindow(self.windowHandle)

	def event_gainFocus(self):
		selection=self._getSelection()
		dropdown=self._getDropdown()
		if dropdown:
			if selection:
				dropdown.parent=selection
			eventHandler.executeEvent('gainFocus',dropdown)
			return
		if selection:
			eventHandler.executeEvent('gainFocus',selection)

class ExcelWorksheet(ExcelBase):


	treeInterceptorClass=ExcelBrowseModeTreeInterceptor

	role=controlTypes.ROLE_TABLE

	def _get_excelApplicationObject(self):
		self.excelApplicationObject=self.excelWorksheetObject.application
		return self.excelApplicationObject

	re_definedName=re.compile(ur'^((?P<sheet>\w+)!)?(?P<name>\w+)(\.(?P<minAddress>[a-zA-Z]+[0-9]+)?(\.(?P<maxAddress>[a-zA-Z]+[0-9]+)?(\..*)*)?)?$')

	def populateHeaderCellTrackerFromNames(self,headerCellTracker):
		sheetName=self.excelWorksheetObject.name
		for x in self.excelWorksheetObject.parent.names:
			fullName=x.name
			nameMatch=self.re_definedName.match(fullName)
			if not nameMatch:
				continue
			sheet=nameMatch.group('sheet')
			if sheet and sheet!=sheetName:
				continue
			name=nameMatch.group('name').lower()
			isColumnHeader=isRowHeader=False
			if name.startswith('title'):
				isColumnHeader=isRowHeader=True
			elif name.startswith('columntitle'):
				isColumnHeader=True
			elif name.startswith('rowtitle'):
				isRowHeader=True
			else:
				continue
			try:
				headerCell=x.refersToRange
			except COMError:
				continue
			if headerCell.parent.name!=sheetName:
				continue
			minColumnNumber=maxColumnNumber=minRowNumber=maxRowNumber=None
			minAddress=nameMatch.group('minAddress')
			if minAddress:
				try:
					minCell=self.excelWorksheetObject.range(minAddress)
				except COMError:
					minCell=None
				if minCell:
					minRowNumber=minCell.row
					minColumnNumber=minCell.column
			maxAddress=nameMatch.group('maxAddress')
			if maxAddress:
				try:
					maxCell=self.excelWorksheetObject.range(maxAddress)
				except COMError:
					maxCell=None
				if maxCell:
					maxRowNumber=maxCell.row
					maxColumnNumber=maxCell.column
			headerCellTracker.addHeaderCellInfo(rowNumber=headerCell.row,columnNumber=headerCell.column,rowSpan=headerCell.rows.count,colSpan=headerCell.columns.count,minRowNumber=minRowNumber,maxRowNumber=maxRowNumber,minColumnNumber=minColumnNumber,maxColumnNumber=maxColumnNumber,name=fullName,isColumnHeader=isColumnHeader,isRowHeader=isRowHeader)

	def _get_headerCellTracker(self):
		self.headerCellTracker=HeaderCellTracker()
		self.populateHeaderCellTrackerFromNames(self.headerCellTracker)
		return self.headerCellTracker

	def setAsHeaderCell(self,cell,isColumnHeader=False,isRowHeader=False):
		oldInfo=self.headerCellTracker.getHeaderCellInfoAt(cell.rowNumber,cell.columnNumber)
		if oldInfo:
			if isColumnHeader and not oldInfo.isColumnHeader:
				oldInfo.isColumnHeader=True
				oldInfo.rowSpan=cell.rowSpan
			elif isRowHeader and not oldInfo.isRowHeader:
				oldInfo.isRowHeader=True
				oldInfo.colSpan=cell.colSpan
			else:
				return False
			isColumnHeader=oldInfo.isColumnHeader
			isRowHeader=oldInfo.isRowHeader
		if isColumnHeader and isRowHeader:
			name="Title_"
		elif isRowHeader:
			name="RowTitle_"
		elif isColumnHeader:
			name="ColumnTitle_"
		else:
			raise ValueError("One or both of isColumnHeader or isRowHeader must be True")
		name+=uuid.uuid4().hex
		if oldInfo:
			self.excelWorksheetObject.parent.names(oldInfo.name).delete()
			oldInfo.name=name
		else:
			self.headerCellTracker.addHeaderCellInfo(rowNumber=cell.rowNumber,columnNumber=cell.columnNumber,rowSpan=cell.rowSpan,colSpan=cell.colSpan,name=name,isColumnHeader=isColumnHeader,isRowHeader=isRowHeader)
		self.excelWorksheetObject.parent.names.add(name,cell.excelRangeObject)
		return True

	def forgetHeaderCell(self,cell,isColumnHeader=False,isRowHeader=False):
		if not isColumnHeader and not isRowHeader: 
			return False
		info=self.headerCellTracker.getHeaderCellInfoAt(cell.rowNumber,cell.columnNumber)
		if not info:
			return False
		if isColumnHeader and info.isColumnHeader:
			info.isColumnHeader=False
		elif isRowHeader and info.isRowHeader:
			info.isRowHeader=False
		else:
			return False
		self.headerCellTracker.removeHeaderCellInfo(info)
		self.excelWorksheetObject.parent.names(info.name).delete()
		if info.isColumnHeader or info.isRowHeader:
			self.setAsHeaderCell(cell,isColumnHeader=info.isColumnHeader,isRowHeader=info.isRowHeader)
		return True

	def fetchAssociatedHeaderCellText(self,cell,columnHeader=False):
		# #4409: cell.currentRegion fails if the worksheet is protected.
		try:
			cellRegion=cell.excelCellObject.currentRegion
		except COMError:
			log.debugWarning("Possibly protected sheet")
			return None
		if cellRegion.count==1:
			minRow=maxRow=minColumn=maxColumn=None
		else:
			rc=cellRegion.address(True,True,xlRC,False)
			g=[int(x) for x in re_absRC.match(rc).groups()]
			minRow,maxRow,minColumn,maxColumn=min(g[0],g[2]),max(g[0],g[2]),min(g[1],g[3]),max(g[1],g[3])
		for info in self.headerCellTracker.iterPossibleHeaderCellInfosFor(cell.rowNumber,cell.columnNumber,minRowNumber=minRow,maxRowNumber=maxRow,minColumnNumber=minColumn,maxColumnNumber=maxColumn,columnHeader=columnHeader):
			textList=[]
			if columnHeader:
				for headerRowNumber in xrange(info.rowNumber,info.rowNumber+info.rowSpan): 
					headerCell=self.excelWorksheetObject.cells(headerRowNumber,cell.columnNumber)
					# The header could be  merged cells. 
					# if so, fetch text from the first in the merge as that always contains the content
					try:
						headerCell=headerCell.mergeArea.item(1)
					except (COMError,NameError,AttributeError):
						pass
					textList.append(headerCell.text)
			else:
				for headerColumnNumber in xrange(info.columnNumber,info.columnNumber+info.colSpan): 
					headerCell=self.excelWorksheetObject.cells(cell.rowNumber,headerColumnNumber)
					# The header could be  merged cells. 
					# if so, fetch text from the first in the merge as that always contains the content
					try:
						headerCell=headerCell.mergeArea.item(1)
					except (COMError,NameError,AttributeError):
						pass
					textList.append(headerCell.text)
			text=" ".join(textList)
			if text:
				return text

	def __init__(self,windowHandle=None,excelWindowObject=None,excelWorksheetObject=None):
		self.excelWindowObject=excelWindowObject
		self.excelWorksheetObject=excelWorksheetObject
		super(ExcelWorksheet,self).__init__(windowHandle=windowHandle)
		for gesture in self.__changeSelectionGestures:
			self.bindGesture(gesture, "changeSelection")

	def _get_name(self):
		return self.excelWorksheetObject.name

	def _isEqual(self, other):
		if not super(ExcelWorksheet, self)._isEqual(other):
			return False
		return self.excelWorksheetObject.index == other.excelWorksheetObject.index

	def _get_firstChild(self):
		cell=self.excelWorksheetObject.cells(1,1)
		return ExcelCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=cell)

	def script_changeSelection(self,gesture):
		oldSelection=api.getFocusObject()
		gesture.send()
		import eventHandler
		import time
		newSelection=None
		curTime=startTime=time.time()
		while (curTime-startTime)<=0.15:
			if scriptHandler.isScriptWaiting():
				# Prevent lag if keys are pressed rapidly
				return
			if eventHandler.isPendingEvents('gainFocus'):
				return
			newSelection=self._getSelection()
			if newSelection and newSelection!=oldSelection:
				break
			api.processPendingEvents(processEventQueue=False)
			time.sleep(0.015)
			curTime=time.time()
		if newSelection:
			if oldSelection.parent==newSelection.parent:
				newSelection.parent=oldSelection.parent
			eventHandler.executeEvent('gainFocus',newSelection)
	script_changeSelection.canPropagate=True

	__changeSelectionGestures = (
		"kb:tab",
		"kb:shift+tab",
		"kb:upArrow",
		"kb:downArrow",
		"kb:leftArrow",
		"kb:rightArrow",
		"kb:control+upArrow",
		"kb:control+downArrow",
		"kb:control+leftArrow",
		"kb:control+rightArrow",
		"kb:home",
		"kb:end",
		"kb:control+home",
		"kb:control+end",
		"kb:shift+upArrow",
		"kb:shift+downArrow",
		"kb:shift+leftArrow",
		"kb:shift+rightArrow",
		"kb:shift+control+upArrow",
		"kb:shift+control+downArrow",
		"kb:shift+control+leftArrow",
		"kb:shift+control+rightArrow",
		"kb:shift+home",
		"kb:shift+end",
		"kb:shift+control+home",
		"kb:shift+control+end",
		"kb:shift+space",
		"kb:control+space",
		"kb:pageUp",
		"kb:pageDown",
		"kb:shift+pageUp",
		"kb:shift+pageDown",
		"kb:alt+pageUp",
		"kb:alt+pageDown",
		"kb:alt+shift+pageUp",
		"kb:alt+shift+pageDown",
		"kb:control+shift+8",
		"kb:control+pageUp",
		"kb:control+pageDown",
		"kb:control+a",
		"kb:control+v",
	)

class ExcelCellTextInfo(NVDAObjectTextInfo):

	def _getFormatFieldAndOffsets(self,offset,formatConfig,calculateOffsets=True):
		formatField=textInfos.FormatField()
		fontObj=self.obj.excelCellObject.font
		if formatConfig['reportAlignment']:
			value=alignmentLabels.get(self.obj.excelCellObject.horizontalAlignment)
			if value:
				formatField['text-align']=value
			value=alignmentLabels.get(self.obj.excelCellObject.verticalAlignment)
			if value:
				formatField['vertical-align']=value
		if formatConfig['reportFontName']:
			formatField['font-name']=fontObj.name
		if formatConfig['reportFontSize']:
			formatField['font-size']=str(fontObj.size)
		if formatConfig['reportFontAttributes']:
			formatField['bold']=fontObj.bold
			formatField['italic']=fontObj.italic
			underline=fontObj.underline
			formatField['underline']=False if underline is None or underline==xlUnderlineStyleNone else True
		if formatConfig['reportStyle']:
			try:
				styleName=self.obj.excelCellObject.style.nameLocal
			except COMError:
				styleName=None
			if styleName:
				formatField['style']=styleName
		if formatConfig['reportColor']:
			try:
				formatField['color']=colors.RGB.fromCOLORREF(int(fontObj.color))
			except COMError:
				pass
			try:
				formatField['background-color']=colors.RGB.fromCOLORREF(int(self.obj.excelCellObject.interior.color))
			except COMError:
				pass
		return formatField,(self._startOffset,self._endOffset)

class ExcelCell(ExcelBase):

	def _get_columnHeaderText(self):
		return self.parent.fetchAssociatedHeaderCellText(self,columnHeader=True)

	def _get_rowHeaderText(self):
		return self.parent.fetchAssociatedHeaderCellText(self,columnHeader=False)

	def script_openDropdown(self,gesture):
		gesture.send()
		d=None
		curTime=startTime=time.time()
		while (curTime-startTime)<=0.25:
			if scriptHandler.isScriptWaiting():
				# Prevent lag if keys are pressed rapidly
				return
			if eventHandler.isPendingEvents('gainFocus'):
				return
			d=self._getDropdown()
			if d:
				break
			api.processPendingEvents(processEventQueue=False)
			time.sleep(0.025)
			curTime=time.time()
		if not d:
			log.debugWarning("Failed to get dropDown, giving up")
			return
		d.parent=self
		eventHandler.queueEvent("gainFocus",d)

	def script_setColumnHeader(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if not config.conf['documentFormatting']['reportTableHeaders']:
			# Translators: a message reported in the SetColumnHeader script for Excel.
			ui.message(_("Cannot set headers. Please enable reporting of table headers in Document Formatting Settings"))
			return
		if scriptCount==0:
			if self.parent.setAsHeaderCell(self,isColumnHeader=True,isRowHeader=False):
				# Translators: a message reported in the SetColumnHeader script for Excel.
				ui.message(_("Set {address} as start of column headers").format(address=self.cellCoordsText))
			else:
				# Translators: a message reported in the SetColumnHeader script for Excel.
				ui.message(_("Already set {address} as start of column headers").format(address=self.cellCoordsText))
		elif scriptCount==1:
			if self.parent.forgetHeaderCell(self,isColumnHeader=True,isRowHeader=False):
				# Translators: a message reported in the SetColumnHeader script for Excel.
				ui.message(_("removed {address}    from column headers").format(address=self.cellCoordsText))
			else:
				# Translators: a message reported in the SetColumnHeader script for Excel.
				ui.message(_("Cannot find {address}    in column headers").format(address=self.cellCoordsText))
	script_setColumnHeader.__doc__=_("Pressing once will set this cell as the first column header for any cells lower and to the right of it within this region. Pressing twice will forget the current column header for this cell.")

	def script_setRowHeader(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if not config.conf['documentFormatting']['reportTableHeaders']:
			# Translators: a message reported in the SetRowHeader script for Excel.
			ui.message(_("Cannot set headers. Please enable reporting of table headers in Document Formatting Settings"))
			return
		if scriptCount==0:
			if self.parent.setAsHeaderCell(self,isColumnHeader=False,isRowHeader=True):
				# Translators: a message reported in the SetRowHeader script for Excel.
				ui.message(_("Set {address} as start of row headers").format(address=self.cellCoordsText))
			else:
				# Translators: a message reported in the SetRowHeader script for Excel.
				ui.message(_("Already set {address} as start of row headers").format(address=self.cellCoordsText))
		elif scriptCount==1:
			if self.parent.forgetHeaderCell(self,isColumnHeader=False,isRowHeader=True):
				# Translators: a message reported in the SetRowHeader script for Excel.
				ui.message(_("removed {address}    from row headers").format(address=self.cellCoordsText))
			else:
				# Translators: a message reported in the SetRowHeader script for Excel.
				ui.message(_("Cannot find {address}    in row headers").format(address=self.cellCoordsText))
	script_setRowHeader.__doc__=_("Pressing once will set this cell as the first row header for any cells lower and to the right of it within this region. Pressing twice will forget the current row header for this cell.")

	@classmethod
	def kwargsFromSuper(cls,kwargs,relation=None):
		windowHandle=kwargs['windowHandle']
		excelWindowObject=cls.excelWindowObjectFromWindow(windowHandle)
		if not excelWindowObject:
			return False
		if isinstance(relation,tuple):
			excelCellObject=excelWindowObject.rangeFromPoint(relation[0],relation[1])
		else:
			excelCellObject=excelWindowObject.ActiveCell
		if not excelCellObject:
			return False
		kwargs['excelWindowObject']=excelWindowObject
		kwargs['excelCellObject']=excelCellObject
		return True

	def __init__(self,windowHandle=None,excelWindowObject=None,excelCellObject=None):
		self.excelWindowObject=excelWindowObject
		self.excelCellObject=excelCellObject
		super(ExcelCell,self).__init__(windowHandle=windowHandle)

	def _get_excelRangeObject(self):
		return self.excelCellObject

	def _get_role(self):
		try:
			linkCount=self.excelCellObject.hyperlinks.count
		except (COMError,NameError,AttributeError):
			linkCount=None
		if linkCount:
			return controlTypes.ROLE_LINK
		return controlTypes.ROLE_TABLECELL

	TextInfo=ExcelCellTextInfo

	def _isEqual(self,other):
		if not super(ExcelCell,self)._isEqual(other):
			return False
		thisAddr=self.getCellAddress(self.excelCellObject,True)
		try:
			otherAddr=self.getCellAddress(other.excelCellObject,True)
		except COMError:
			#When cutting and pasting the old selection can become broken
			return False
		return thisAddr==otherAddr

	def _get_cellCoordsText(self):
		return self.getCellAddress(self.excelCellObject)

	def _get__rowAndColumnNumber(self):
		rc=self.excelCellObject.address(True,True,xlRC,False)
		return [int(x) if x else 1 for x in re_absRC.match(rc).groups()]

	def _get_rowNumber(self):
		return self._rowAndColumnNumber[0]

	rowSpan=1

	def _get_columnNumber(self):
		return self._rowAndColumnNumber[1]

	colSpan=1

	def _get_tableID(self):
		address=self.excelCellObject.address(1,1,0,1)
		ID="".join(address.split('!')[:-1])
		ID="%s %s"%(ID,self.windowHandle)
		return ID

	def _get_name(self):
		return self.excelCellObject.Text

	def _get_states(self):
		states=super(ExcelCell,self).states
		if self.excelCellObject.HasFormula:
			states.add(controlTypes.STATE_HASFORMULA)
		try:
			validationType=self.excelCellObject.validation.type
		except (COMError,NameError,AttributeError):
			validationType=None
		if validationType==3:
			states.add(controlTypes.STATE_HASPOPUP)
		try:
			comment=self.excelCellObject.comment
		except (COMError,NameError,AttributeError):
			comment=None
		if comment:
			states.add(controlTypes.STATE_HASCOMMENT)
		return states

	def _get_parent(self):
		worksheet=self.excelCellObject.Worksheet
		self.parent=ExcelWorksheet(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelWorksheetObject=worksheet)
		return self.parent

	def _get_next(self):
		try:
			next=self.excelCellObject.next
		except COMError:
			next=None
		if next:
			return ExcelCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=next)

	def _get_previous(self):
		try:
			previous=self.excelCellObject.previous
		except COMError:
			previous=None
		if previous:
			return ExcelCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=previous)

	def script_reportComment(self,gesture):
		commentObj=self.excelCellObject.comment
		text=commentObj.text() if commentObj else None
		if text:
			ui.message(text)
		else:
			# Translators: A message in Excel when there is no comment
			ui.message(_("Not on a comment"))
	# Translators: the description  for a script for Excel
	script_reportComment.__doc__=_("Reports the comment on the current cell")

	def script_editComment(self,gesture):
		commentObj=self.excelCellObject.comment
		d = wx.TextEntryDialog(gui.mainFrame, 
			# Translators: Dialog text for 
			_("Editing comment for cell {address}").format(address=self.cellCoordsText),
			# Translators: Title of a dialog edit an Excel comment 
			_("Comment"),
			defaultValue=commentObj.text() if commentObj else u"",
			style=wx.TE_MULTILINE|wx.OK|wx.CANCEL)
		def callback(result):
			if result == wx.ID_OK:
				if commentObj:
					commentObj.text(d.Value)
				else:
					self.excelCellObject.addComment(d.Value)
		gui.runScriptModalDialog(d, callback)

	__gestures = {
		"kb:NVDA+shift+c": "setColumnHeader",
		"kb:NVDA+shift+r": "setRowHeader",
		"kb:shift+f2":"editComment",
		"kb:alt+downArrow":"openDropdown",
		"kb:NVDA+alt+c":"reportComment",
	}

class ExcelSelection(ExcelBase):

	role=controlTypes.ROLE_TABLECELL

	def __init__(self,windowHandle=None,excelWindowObject=None,excelRangeObject=None):
		self.excelWindowObject=excelWindowObject
		self.excelRangeObject=excelRangeObject
		super(ExcelSelection,self).__init__(windowHandle=windowHandle)

	def _get_states(self):
		states=super(ExcelSelection,self).states
		states.add(controlTypes.STATE_SELECTED)
		return states

	def _get_name(self):
		firstCell=self.excelRangeObject.Item(1)
		lastCell=self.excelRangeObject.Item(self.excelRangeObject.Count)
		# Translators: This is presented in Excel to show the current selection, for example 'a1 c3 through a10 c10'
		return _("{firstAddress} {firstContent} through {lastAddress} {lastContent}").format(firstAddress=self.getCellAddress(firstCell),firstContent=firstCell.Text,lastAddress=self.getCellAddress(lastCell),lastContent=lastCell.Text)

	def _get_parent(self):
		worksheet=self.excelRangeObject.Worksheet
		return ExcelWorksheet(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelWorksheetObject=worksheet)

	def _get_rowNumber(self):
		return self.excelRangeObject.row

	def _get_rowSpan(self):
		return self.excelRangeObject.rows.count

	def _get_columnNumber(self):
		return self.excelRangeObject.column

	def _get_colSpan(self):
		return self.excelRangeObject.columns.count

	#Its useful for an excel selection to be announced with reportSelection script
	def makeTextInfo(self,position):
		if position==textInfos.POSITION_SELECTION:
			position=textInfos.POSITION_ALL
		return super(ExcelSelection,self).makeTextInfo(position)

class ExcelDropdownItem(Window):

	firstChild=None
	lastChild=None
	children=[]
	role=controlTypes.ROLE_LISTITEM

	def __init__(self,parent=None,name=None,states=None,index=None):
		self.name=name
		self.states=states
		self.parent=parent
		self.index=index
		super(ExcelDropdownItem,self).__init__(windowHandle=parent.windowHandle)

	def _get_previous(self):
		newIndex=self.index-1
		if newIndex>=0:
			return self.parent.children[newIndex]

	def _get_next(self):
		newIndex=self.index+1
		if newIndex<self.parent.childCount:
			return self.parent.children[newIndex]

	def _get_positionInfo(self):
		return {'indexInGroup':self.index+1,'similarItemsInGroup':self.parent.childCount,}

class ExcelDropdown(Window):

	@classmethod
	def kwargsFromSuper(cls,kwargs,relation=None):
		return kwargs

	role=controlTypes.ROLE_LIST
	excelCell=None

	def _get__highlightColors(self):
		background=colors.RGB.fromCOLORREF(winUser.user32.GetSysColor(13))
		foreground=colors.RGB.fromCOLORREF(winUser.user32.GetSysColor(14))
		self._highlightColors=(background,foreground)
		return self._highlightColors

	def _get_children(self):
		children=[]
		index=0
		states=set()
		for item in DisplayModelTextInfo(self,textInfos.POSITION_ALL).getTextWithFields():
			if isinstance(item,textInfos.FieldCommand) and item.command=="formatChange":
				states=set([controlTypes.STATE_SELECTABLE])
				foreground=item.field.get('color',None)
				background=item.field.get('background-color',None)
				if (background,foreground)==self._highlightColors:
					states.add(controlTypes.STATE_SELECTED)
			if isinstance(item,basestring):
				obj=ExcelDropdownItem(parent=self,name=item,states=states,index=index)
				children.append(obj)
				index+=1
		return children

	def _get_childCount(self):
		return len(self.children)

	def _get_firstChild(self):
		return self.children[0]
	def _get_selection(self):
		for child in self.children:
			if controlTypes.STATE_SELECTED in child.states:
				return child

	def script_selectionChange(self,gesture):
		gesture.send()
		newFocus=self.selection or self
		if eventHandler.lastQueuedFocusObject is newFocus: return
		eventHandler.queueEvent("gainFocus",newFocus)
	script_selectionChange.canPropagate=True

	def script_closeDropdown(self,gesture):
		gesture.send()
		eventHandler.queueEvent("gainFocus",self.parent)
	script_closeDropdown.canPropagate=True

	__gestures={
		"kb:downArrow":"selectionChange",
		"kb:upArrow":"selectionChange",
		"kb:leftArrow":"selectionChange",
		"kb:rightArrow":"selectionChange",
		"kb:home":"selectionChange",
		"kb:end":"selectionChange",
		"kb:escape":"closeDropdown",
		"kb:enter":"closeDropdown",
		"kb:space":"closeDropdown",
	}

	def event_gainFocus(self):
		child=self.selection
		if not child and self.childCount>0:
			child=self.children[0]
		if child:
			eventHandler.queueEvent("focusEntered",self)
			eventHandler.queueEvent("gainFocus",child)
		else:
			super(ExcelDropdown,self).event_gainFocus()

class ExcelMergedCell(ExcelCell):

	def _get_cellCoordsText(self):
		return self.getCellAddress(self.excelCellObject.mergeArea)

	def _get_rowSpan(self):
		return self.excelCellObject.mergeArea.rows.count

	def _get_colSpan(self):
		return self.excelCellObject.mergeArea.columns.count

