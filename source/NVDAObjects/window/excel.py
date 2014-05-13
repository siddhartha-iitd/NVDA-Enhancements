#NVDAObjects/excel.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2007 NVDA Contributors <http://www.nvda-project.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from comtypes import COMError
import comtypes.automation
import wx
import time
import re
import oleacc
import ui
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
import speech

# Chart types in Microsft Excel.
xl3DArea = -4098
xl3DAreaStacked	= 78
xl3DAreaStacked100 = 79
xl3DBarClustered = 60
xl3DBarStacked = 61
xl3DBarStacked100 = 62
xl3DColumn = -4100
xl3DColumnClustered = 54
xl3DColumnStacked = 55
xl3DColumnStacked100 = 56
xl3DLine = -4101
xl3DPie = -4102
xl3DPieExploded = 70
xlArea = 1
xlAreaStacked = 76
xlAreaStacked100 = 77
xlBarClustered = 57
xlBarOfPie = 71
xlBarStacked = 58
xlBarStacked100 = 59
xlBubble = 15
xlBubble3DEffect = 87
xlColumnClustered = 51
xlColumnStacked = 52
xlColumnStacked100 = 53
xlConeBarClustered = 102
xlConeBarStacked = 103
xlConeBarStacked100 = 104
xlConeCol = 105
xlConeColClustered = 99
xlConeColStacked = 100
xlConeColStacked100 = 101
xlCylinderBarClustered = 95
xlCylinderBarStacked = 96
xlCylinderBarStacked100 = 97
xlCylinderCol = 98
xlCylinderColClustered = 92
xlCylinderColStacked = 93
xlCylinderColStacked100 = 94
xlDoughnut = -4120
xlDoughnutExploded = 80
xlLine = 4
xlLineMarkers = 65
xlLineMarkersStacked = 66
xlLineMarkersStacked100 = 67
xlLineStacked = 63
xlLineStacked100 = 64
xlPie = 5
xlPieExploded = 69
xlPieOfPie = 68
xlPyramidBarClustered = 109
xlPyramidBarStacked = 110
xlPyramidBarStacked100 = 111
xlPyramidCol = 112
xlPyramidColClustered = 106
xlPyramidColStacked = 107
xlPyramidColStacked100 = 108
xlRadar = -4151
xlRadarFilled = 82
xlRadarMarkers = 81
xlStockHLC = 88
xlStockOHLC = 89
xlStockVHLC = 90
xlStockVOHLC = 91
xlSurface = 83
xlSurfaceTopView = 85
xlSurfaceTopViewWireframe = 86
xlSurfaceWireframe = 84
xlXYScatter = -4169
xlXYScatterLines = 74
xlXYScatterLinesNoMarkers = 75
xlXYScatterSmooth = 72
xlXYScatterSmoothNoMarkers = 73

# Dictionary for the Description of chart types.
chartTypeDict = {
	xl3DArea : "3D Area",
	xl3DAreaStacked : "3D Stacked Area",
	xl3DAreaStacked100 : "100 percent Stacked Area",
	xl3DBarClustered : "3D Clustered Bar",
	xl3DBarStacked : "3D Stacked Bar",
	xl3DBarStacked100 : "3D 100 percent Stacked Bar",
	xl3DColumn : "3D Column",
	xl3DColumnClustered : "3D Clustered Column",
	xl3DColumnStacked : "3D Stacked Column",
	xl3DColumnStacked100 : "3D 100 percent Stacked Column",
	xl3DLine : "3D Line",
	xl3DPie : "3D Pie",
	xl3DPieExploded : "Exploded 3D Pie",
	xlArea : "Area",
	xlAreaStacked : "Stacked Area",
	xlAreaStacked100 : "100 percent Stacked Area",
	xlBarClustered : "Clustered Bar",
	xlBarOfPie : "Bar of Pie",
	xlBarStacked : "Stacked Bar",
	xlBarStacked100 : "100 percent Stacked Bar",
	xlBubble : "Bubble",
	xlBubble3DEffect : "Bubble with 3D effects",
	xlColumnClustered : "Clustered Column",
	xlColumnStacked : "Stacked Column",
	xlColumnStacked100 : "100 percent Stacked Column",
	xlConeBarClustered : "Clustered Cone Bar",
	xlConeBarStacked : "Stacked Cone Bar",
	xlConeBarStacked100 : "100 percent Stacked Cone Bar",
	xlConeCol : "3D Cone Column",
	xlConeColClustered : "Clustered Cone Column",
	xlConeColStacked : "Stacked Cone Column",
	xlConeColStacked100 : "100 percent Stacked Cone Column",
	xlCylinderBarClustered : "Clustered Cylinder Bar",
	xlCylinderBarStacked : "Stacked Cylinder Bar",
	xlCylinderBarStacked100 : "100 percent Stacked Cylinder Bar",
	xlCylinderCol : "3D Cylinder Column",
	xlCylinderColClustered : "Clustered Cone Column",
	xlCylinderColStacked : "Stacked Cone Column",
	xlCylinderColStacked100 : "100 percent Stacked Cylinder Column",
	xlDoughnut : "Doughnut",
	xlDoughnutExploded : "Exploded Doughnut",
	xlLine : "Line",
	xlLineMarkers : "Line with Markers",
	xlLineMarkersStacked : "Stacked Line with Markers",
	xlLineMarkersStacked100 : "100 percent Stacked Line with Markers",
	xlLineStacked : "Stacked Line",
	xlLineStacked100 : "100 percent Stacked Line",
	xlPie : "Pie",
	xlPieExploded : "Exploded Pie",
	xlPieOfPie : "Pie of Pie",
	xlPyramidBarClustered : "Clustered Pyramid Bar",
	xlPyramidBarStacked : "Stacked Pyramid Bar",
	xlPyramidBarStacked100 : "100 percent Stacked Pyramid Bar",
	xlPyramidCol : "3D Pyramid Column",
	xlPyramidColClustered : "Clustered Pyramid Column",
	xlPyramidColStacked : "Stacked Pyramid Column",
	xlPyramidColStacked100 : "100 percent Stacked Pyramid Column",
	xlRadar : "Radar",
	xlRadarFilled : "Filled Radar",
	xlRadarMarkers : "Radar with Data Markers",
	xlStockHLC : "High-Low-Close",
	xlStockOHLC : "Open-High-Low-Close",
	xlStockVHLC : "Volume-High-Low-Close",
	xlStockVOHLC : "Volume-Open-High-Low-Close",
	xlSurface : "3D Surface",
	xlSurfaceTopView : "Surface (Top View)",
	xlSurfaceTopViewWireframe : "Surface (Top View wireframe)",
	xlSurfaceWireframe : "3D Surface (wireframe)",
	xlXYScatter : "Scatter",
	xlXYScatterLines : "Scatter with Lines",
	xlXYScatterLinesNoMarkers : "Scatter with Lines and No Data Markers",
	xlXYScatterSmooth : "Scatter with Smoothed Lines",
	xlXYScatterSmoothNoMarkers : "Scatter with Smoothed Lines and No Data Markers"
}

# Axis types in chart
xlCategory = 1
xlValue = 2
xlSeriesAxis = 3 # Valid only for 3-D charts

# Axis Groups in chart
xlPrimary = 1
xlSecondary = 2

xlA1 = 1
xlRC = 2
xlUnderlineStyleNone=-4142

re_RC=re.compile(r'R(?:\[(\d+)\])?C(?:\[(\d+)\])?')

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
		if isMerged:
			obj=ExcelMergedCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=selection.item(1))
		elif numCells>1:
			obj=ExcelSelection(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelRangeObject=selection)
		elif numCells==1:
			obj=ExcelCell(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelCellObject=selection)
		elif isChartActive:
			selection = self.excelWindowObject.ActiveChart
			obj=ExcelChart(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelChartObject=selection)
	
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

	role=controlTypes.ROLE_TABLE

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
		oldSelection=self._getSelection()
		gesture.send()
		import eventHandler
		import time
		import api
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
		"kb:control+pageUp",
		"kb:control+pageDown",
		"kb:control+a",
		"kb:control+v",
		"kb:nvda+alt+s"
	)


class ExcelCellTextInfo(NVDAObjectTextInfo):

	def _getFormatFieldAndOffsets(self,offset,formatConfig,calculateOffsets=True):
		formatField=textInfos.FormatField()
		fontObj=self.obj.excelCellObject.font
		if formatConfig['reportFontName']:
			formatField['font-name']=fontObj.name
		if formatConfig['reportFontSize']:
			formatField['font-size']=str(fontObj.size)
		if formatConfig['reportFontAttributes']:
			formatField['bold']=fontObj.bold
			formatField['italic']=fontObj.italic
			underline=fontObj.underline
			formatField['underline']=False if underline is None or underline==xlUnderlineStyleNone else True
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

	columnHeaderRows={}
	rowHeaderColumns={}

	def _get_columnHeaderText(self):
		tableID=self.tableID
		rowNumber=self.rowNumber
		columnNumber=self.columnNumber
		columnHeaderRow=self.columnHeaderRows.get(tableID) or None
		if columnHeaderRow and rowNumber>columnHeaderRow:
			return self.excelCellObject.parent.cells(columnHeaderRow,columnNumber).text

	def _get_rowHeaderText(self):
		tableID=self.tableID
		rowNumber=self.rowNumber
		columnNumber=self.columnNumber
		rowHeaderColumn=self.rowHeaderColumns.get(tableID) or None
		if rowHeaderColumn and columnNumber>rowHeaderColumn:
			return self.excelCellObject.parent.cells(rowNumber,rowHeaderColumn).text

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

	def script_setColumnHeaderRow(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		tableID=self.tableID
		if not config.conf['documentFormatting']['reportTableHeaders']:
			# Translators: a message reported in the SetColumnHeaderRow script for Excel.
			ui.message(_("Cannot set headers. Please enable reporting of table headers in Document Formatting Settings"))
			return
		if scriptCount==0:
			self.columnHeaderRows[tableID]=self.rowNumber
			# Translators: a message reported in the SetColumnHeaderRow script for Excel.
			ui.message(_("Set column header row"))
		elif scriptCount==1 and tableID in self.columnHeaderRows:
			del self.columnHeaderRows[tableID]
			# Translators: a message reported in the SetColumnHeaderRow script for Excel.
			ui.message(_("Cleared column header row"))
	script_setColumnHeaderRow.__doc__=_("Pressing once will set the current row as the row where column headers should be found. Pressing twice clears the setting.")

	def script_setRowHeaderColumn(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		tableID=self.tableID
		if not config.conf['documentFormatting']['reportTableHeaders']:
			# Translators: a message reported in the SetRowHeaderColumn script for Excel.
			ui.message(_("Cannot set headers. Please enable reporting of table headers in Document Formatting Settings"))
			return
		if scriptCount==0:
			self.rowHeaderColumns[tableID]=self.columnNumber
			# Translators: a message reported in the SetRowHeaderColumn script for Excel.
			ui.message(_("Set row header column"))
		elif scriptCount==1 and tableID in self.rowHeaderColumns:
			del self.rowHeaderColumns[tableID]
			# Translators: a message reported in the SetRowHeaderColumn script for Excel.
			ui.message(_("Cleared row header column"))
	script_setRowHeaderColumn.__doc__=_("Pressing once will set the current column as the column where row headers should be found. Pressing twice clears the setting.")

	def script_switchToChart(self,gesture):
		try:
			chart = self.excelCellObject.parent.ChartObjects(1)
		except (COMError,NameError,AttributeError):
			chart = None
		if chart:
			chart.Activate()
			chart.Index
			chartObj = self._getSelection()
			eventHandler.queueEvent("gainFocus", chartObj)
		else:
			text = _("No chart present.")
			speech.speak([text])

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
		rc=self.excelCellObject.address(False,False,xlRC,False)
		return [int(x)+1 if x else 1 for x in re_RC.match(rc).groups()]

	def _get_rowNumber(self):
		return self._rowAndColumnNumber[0]

	def _get_columnNumber(self):
		return self._rowAndColumnNumber[1]

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
		return ExcelWorksheet(windowHandle=self.windowHandle,excelWindowObject=self.excelWindowObject,excelWorksheetObject=worksheet)

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

	__gestures = {
		"kb:NVDA+shift+c": "setColumnHeaderRow",
		"kb:NVDA+shift+r": "setRowHeaderColumn",
		"kb:alt+downArrow":"openDropdown",
		"kb:NVDA+shift+s": "switchToChart",
	}



class ExcelChart(ExcelBase):
	def __init__(self,windowHandle=None,excelWindowObject=None,excelChartObject=None):
		self.excelWindowObject=excelWindowObject
		self.excelChartObject=excelChartObject
		super(ExcelChart,self).__init__(windowHandle=windowHandle)

	def _isEqual(self, other):
		if not super(ExcelChart, self)._isEqual(other):
			return False
		return self.excelChartObject == other.excelChartObject

	def _get_name(self):
		return self.excelChartObject.Name

	def _get_title(self):
		try:
			title=self.excelChartObject.ChartTitle	
		except COMError:
			title=None
		return title

	def script_switchToCell(self,gesture):
		cell=self.excelWindowObject.ActiveCell
		cell.Activate()
		cellObj=self._getSelection()
		eventHandler.queueEvent("gainFocus",cellObj)

	def script_switchBetweenCharts(self,gesture):
		gesture.send()
		chartObj=self._getSelection()
		eventHandler.queueEvent("gainFocus", chartObj)

	def script_speakType(self,gesture):
		chartType = self.excelChartObject.ChartType
		if chartType in chartTypeDict.keys():
			text=_("%s chart type" %(chartTypeDict[chartType]))
		else:
			text=_("Chart type unknown")
		speech.speak([text])

	def script_speakTitle(self,gesture):
		title = self._get_title()
		text=_("Chart title is %s" %(title.text)) if title else _("No chart title defined")
		speech.speak([text])

	def script_speakName(self,gesture):
		name=self._get_name()
		text=_("Chart name is %s" %(name))
		speech.speak([text])

	def speakAxisTitle(self, axisType):
		axis=None
		if self.excelChartObject.HasAxis(axisType, xlPrimary):
			axis = self.excelChartObject.Axes(axisType, xlPrimary)
		else:
			pass
		axisTitle = axis.AxisTitle.Text if axis and axis.HasTitle else "Not defined"
		axisName = "Category" if axisType==xlCategory else "Value" if axisType==xlValue else "Series"
		text=_("%s Axis is %s" %(axisName, axisTitle))
		speech.speak([text])

	def script_speakCategoryAxis(self, gesture):
		self.speakAxisTitle(xlCategory)

	def script_speakValueAxis(self, gesture):
		self.speakAxisTitle(xlValue)

	def script_speakSeriesAxis(self, gesture):
		self.speakAxisTitle(xlSeriesAxis)

	def script_speakSeries(self, gesture):
		count = self.excelChartObject.SeriesCollection().count
		if count>0:
			seriesValueString="%d series in this chart" %(count)
			for i in xrange(1, count+1):
				seriesValueString += ", Series %d %s" %(i, self.excelChartObject.SeriesCollection(i).Name)
			text=_(seriesValueString)	
		else:
			text=_("No Series defined.")
		speech.speak([text])

	def speakDataLabels(self, index):
		count = self.excelChartObject.SeriesCollection().count
		dataLabels=None
		if index > count:
			pass
		else:
			xVal = self.excelChartObject.SeriesCollection(index).XValues
			val = self.excelChartObject.SeriesCollection(index).Values
			dataLabels=zip(xVal, val)
		if dataLabels:
			text="Series name %s, %d pairs" %(self.excelChartObject.SeriesCollection(index).Name, len(dataLabels))
			for label in dataLabels:
				text+=",(%s,%s) " %(label[0], label[1])
		else:
			text=_("Only %d series in this chart." %(count))
		speech.speak([text])

	# seriesIndex is index of series desired
	def script_speakSeriesOne(self, gesture):
		seriesIndex=1
		self.speakDataLabels(seriesIndex)
	
	def script_speakSeriesTwo(self, gesture):
		seriesIndex=2
		self.speakDataLabels(seriesIndex)
	
	def script_speakSeriesThree(self, gesture):
		seriesIndex=3
		self.speakDataLabels(seriesIndex)
	
	def script_speakSeriesFour(self, gesture):
		seriesIndex=4
		self.speakDataLabels(seriesIndex)
	
	def script_speakSeriesFive(self, gesture):
		seriesIndex=5
		self.speakDataLabels(seriesIndex)

	__gestures = {
		"kb:NVDA+shift+s": "switchToCell",
		"kb:escape": "switchToCell",
		"kb:tab" : "switchBetweenCharts",
		"kb:shift+tab" : "switchBetweenCharts",

		"kb:NVDA+shift+1" : "speakType",
		"kb:NVDA+shift+2" : "speakTitle",
		"kb:NVDA+shift+3" : "speakName",
		"kb:NVDA+shift+4" : "speakCategoryAxis",
		"kb:NVDA+shift+5" : "speakValueAxis",
		"kb:NVDA+shift+6" : "speakSeriesAxis",
		"kb:NVDA+shift+7" : "speakSeries",

		"kb:control+alt+1":"speakSeriesOne",
		"kb:control+alt+2":"speakSeriesTwo",
		"kb:control+alt+3":"speakSeriesThree",
		"kb:control+alt+4":"speakSeriesFour",
		"kb:control+alt+5":"speakSeriesFive",
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
