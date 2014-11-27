#NVDAObjects/excel.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2007 NVDA Contributors <http://www.nvda-project.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

# adding support for excel charts ticket 1987

import time
import ui
import eventHandler
import controlTypes
import excel 
from logHandler import log
from . import Window
import scriptHandler
import colors

from comtypes.client import *
import comtypes
from comtypes.automation import IDispatch
import ctypes
import comtypes.GUID

import math
from NVDAObjects import NVDAObject
import string
import weakref


#ChartEvents definition
class ChartEvents(IDispatch):
	_case_insensitive_ = True
	_iid_ = comtypes.GUID('{0002440F-0000-0000-C000-000000000046}')
	_idlflags_ = ['hidden']
	_methods_ = []
	_disp_methods_=[
		comtypes.DISPMETHOD([comtypes.dispid(235)], None, 'Select',
			( ['in'], ctypes.c_int, 'ElementID' ),
			( ['in'], ctypes.c_int, 'Arg1' ),
			( ['in'], ctypes.c_int, 'Arg2' )),
		]

# Chart types in Microsoft Excel.
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

# Dictionary for the segments of different chart types.
chartSegmentDict = {
	xl3DArea : "3D Area",
	xl3DAreaStacked : "3D Stacked Area",
	xl3DAreaStacked100 : "100 percent Stacked Area",
	xl3DBarClustered : "3D Clustered Bar",
	xl3DBarStacked : "3D Stacked Bar",
	xl3DBarStacked100 : "3D 100 percent Stacked Bar",
	xl3DColumn : "Column",
	xl3DColumnClustered : "Column",
	xl3DColumnStacked : "Column",
	xl3DColumnStacked100 : "Column",
	xl3DLine : "Line",
	xl3DPie : "Slice",
	xl3DPieExploded : "Slice",
	xlArea : "Area",
	xlAreaStacked : "Stacked Area",
	xlAreaStacked100 : "100 percent Stacked Area",
	xlBarClustered : "Clustered Bar",
	xlBarOfPie : "Bar of Pie",
	xlBarStacked : "Stacked Bar",
	xlBarStacked100 : "100 percent Stacked Bar",
	xlBubble : "Bubble",
	xlBubble3DEffect : "Bubble with 3D effects",
	xlColumnClustered : "Column",
	xlColumnStacked : "Column",
	xlColumnStacked100 : "Column",
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
	xlLineMarkers : "Line",
	xlLineMarkersStacked : "Line",
	xlLineMarkersStacked100 : "Line",
	xlLineStacked : "Line",
	xlLineStacked100 : "Line",
	xlPie : "slice",
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



# values for enumeration 'XlChartItem'
xlDataLabel = 0
xlChartArea = 2
xlSeries = 3
xlChartTitle = 4
xlWalls = 5
xlCorners = 6
xlDataTable = 7
xlTrendline = 8
xlErrorBars = 9
xlXErrorBars = 10
xlYErrorBars = 11
xlLegendEntry = 12
xlLegendKey = 13
xlShape = 14
xlMajorGridlines = 15
xlMinorGridlines = 16
xlAxisTitle = 17
xlUpBars = 18
xlPlotArea = 19
xlDownBars = 20
xlAxis = 21
xlSeriesLines = 22
xlFloor = 23
xlLegend = 24
xlHiLoLines = 25
xlDropLines = 26
xlRadarAxisLabels = 27
xlNothing = 28
xlLeaderLines = 29
xlDisplayUnitLabel = 30
xlPivotChartFieldButton = 31
xlPivotChartDropZone = 32
XlChartItem = ctypes.c_int # enum



class ExcelChart(excel.ExcelBase):
	def __init__(self,windowHandle=None,excelWindowObject=None,excelChartObject=None):
		self.windowHandle = windowHandle
		self.excelWindowObject = excelWindowObject
		self.excelChartObject = excelChartObject
		self.excelChartEventHandlerObject = ExcelChartEventHandler( self  )
		self.excelChartEventConnection = GetEvents( self.excelChartObject , self.excelChartEventHandlerObject , ChartEvents)
		log.debugWarning("ExcelChart init")
		super(ExcelChart,self).__init__(windowHandle=windowHandle)
		for gesture in self.__changeSelectionGestures:
			self.bindGesture(gesture, "changeSelection")

	def _isEqual(self, other):
		if not super(ExcelChart, self)._isEqual(other):
			return False
		return self.excelChartObject.Parent.Index == other.excelChartObject.Parent.Index

	def _get_name(self):
		if self.excelChartObject.HasTitle:
			name=self.excelChartObject.ChartTitle.Text
		else:
			name=self.excelChartObject.Name
#find the type of the chart
		chartType = self.excelChartObject.ChartType
		if chartType in chartTypeDict.keys():
			chartTypeText=_("%s" %(chartTypeDict[chartType]))
		else:
			chartTypeText=_("unknown")
		return _("Chart title equals %s type equals %s" %(name, chartTypeText))

	def _get_title(self):
		try:
			title=self.excelChartObject.ChartTitle	
		except COMError:
			title=None
		return title
	
	def _get_role(self):
		return controlTypes.ROLE_UNKNOWN
	
	def script_switchToCell(self,gesture):
		cell=self.excelWindowObject.ActiveCell
		cell.Activate()
		cellObj=self._getSelection()
		eventHandler.queueEvent("gainFocus",cellObj)

	def event_gainFocus(self):
		if self.excelChartObject.HasTitle:
			name=self.excelChartObject.ChartTitle.Text
		else:
			name=self.excelChartObject.Name
#find the type of the chart
		chartType = self.excelChartObject.ChartType
		if chartType in chartTypeDict.keys():
			chartTypeText=_("%s" %(chartTypeDict[chartType]))
		else:
			chartTypeText=_("unknown")
		ui.message( _("Chart title equals %s type equals %s" %(name, chartTypeText)) ) 
		self.reportSeriesSummary()

	def script_reportTitle(self,gesture):
		ui.message (self._get_name())

	def reportAxisTitle(self, axisType):
		axis=None
		if self.excelChartObject.HasAxis(axisType, xlPrimary):
			axis = self.excelChartObject.Axes(axisType, xlPrimary)
		else:
			pass
		axisTitle = axis.AxisTitle.Text if axis and axis.HasTitle else "Not defined"
		axisName = "Category" if axisType==xlCategory else "Value" if axisType==xlValue else "Series"
		text=_("%s Axis is %s" %(axisName, axisTitle))
		ui.message(text)

	def script_reportCategoryAxis(self, gesture):
		self.reportAxisTitle(xlCategory)

	def script_reportValueAxis(self, gesture):
		self.reportAxisTitle(xlValue)

	def script_reportSeriesAxis(self, gesture):
		self.reportAxisTitle(xlSeriesAxis)

	def reportSeriesSummary(self ):
		count = self.excelChartObject.SeriesCollection().count
		if count>0:
			if count == 1:
				seriesValueString="There is %d series in this chart" %(count)
			else:
				seriesValueString="There are total %d series in this chart" %(count)

			for i in xrange(1, count+1):
				seriesValueString += ", Series %d %s" %(i, self.excelChartObject.SeriesCollection(i).Name)
			text=_(seriesValueString)	
		else:
			text=_("No Series defined.")
		ui.message(text)

	def script_reportSeriesSummary(self, gesture):
		self.reportSeriesSummary()

	def script_reportSeriesFormula(self, gesture):
		count = self.excelChartObject.SeriesCollection().count
		if count>0:
			seriesValueString="%d series in this chart" %(count)
			for i in xrange(1, count+1):
				seriesValueString += ", Series %d %s" %(i, self.excelChartObject.SeriesCollection(i).FormulaR1C1)
			text=_(seriesValueString)	
		else:
			text=_("No Series defined.")
		log.debugWarning(text)

	__gestures = {
		"kb:escape": "switchToCell",
		"kb:NVDA+t" : "reportTitle",
		"kb:NVDA+shift+1" : "reportCategoryAxis",
		"kb:NVDA+shift+2" : "reportValueAxis",
		"kb:NVDA+shift+3" : "reportSeriesAxis",
		"kb:NVDA+shift+4" : "reportSeriesSummary",
		"kb:NVDA+shift+5" : "reportSeriesFormula",
	}

	def script_changeSelection(self,gesture):
		oldSelection=self._getSelection()
		gesture.send()
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
			
	__changeSelectionGestures = {
		"kb:control+pageUp",
		"kb:control+pageDown",
		"kb:tab",
		"kb:shift+tab",
	}

	def elementChanged( self , ElementID ,arg1,arg2):

		if ElementID == xlSeries:
			selectedChartElement = ExcelChartElementSeries( windowHandle= self.windowHandle , excelChartObject= self.excelChartObject  , elementID=ElementID  , arg1=arg1 , arg2=arg2 )
			selectedChartElement.parent = self
			eventHandler.queueEvent("gainFocus", selectedChartElement )

		else:
			selectedChartElement = ExcelChartElementBase( windowHandle= self.windowHandle , excelChartObject= self.excelChartObject  , elementID=ElementID  , arg1=arg1 , arg2=arg2 )
			selectedChartElement.parent = self
			eventHandler.queueEvent("gainFocus", selectedChartElement )

class ExcelChartEventHandler(comtypes.COMObject):
	_com_interfaces_=[ChartEvents,IDispatch]

	def __init__(self, owner ):
		self.owner = weakref.proxy( owner )
		super(ExcelChartEventHandler ,self).__init__()

	def ChartEvents_Select(self, this, ElementID ,arg1,arg2):
		self.owner.elementChanged( ElementID ,arg1,arg2)

class ExcelChartElementBase(Window):

	def __init__(self, windowHandle=None , excelChartObject=None   , elementID=None  , arg1=None , arg2=None ):
		self.excelChartObject = excelChartObject
		self.elementID = elementID 
		self.arg1 = arg1
		self.arg2 = arg2
		super(ExcelChartElementBase ,self).__init__(windowHandle=windowHandle)

	def GetChartSegment(self):
		chartType = self.excelChartObject.ChartType
		if chartType in chartSegmentDict.keys():
			text= chartSegmentDict[chartType]
		else:
			text=_("item")
		return text

	#def event_stateChange(self):
		#self.reportFocus()

	def _get_role(self):
			return controlTypes.ROLE_UNKNOWN

	def _get_name(self):
		return self._Select(self.elementID , self.arg1 , self.arg2)

	def script_reportCurrentChartElementWithExtraInfo(self,gesture):
		ui.message( self._Select(self.elementID , self.arg1 , self.arg2 , True ) )

	def script_reportCurrentChartElementColor(self,gesture):
		if self.elementID == xlSeries:
			if self.arg2 == -1:
				ui.message ( _( "Series color: {} ").format(colors.RGB.fromCOLORREF(int( self.excelChartObject.SeriesCollection( self.arg1 ).Interior.Color ) )  ) )

	def _Select(self, ElementID ,arg1,arg2 , reportExtraInfo=False ):
		
		if ElementID == xlAxis:
			if arg1 == xlPrimary: 
				axisGroup = _("Primary")
			elif arg1 == xlSecondary :
				axisGroup = _("Secondary")

			if arg2 == xlCategory: 
				axisType= _("Category")
			elif arg2 == xlValue:
				axisType= _("Value")
			elif arg2 == xlSeriesAxis: 
				axisType= _("Series")

			axisTitle=""
			if self.excelChartObject.HasAxis( arg2 ) and self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += _("Chart Axis, type equals {}, group equals {}, Title equals {}").format( axisType , axisGroup , self.excelChartObject.Axes( arg2 , arg1 ).AxisTitle.Text ) 
			elif self.excelChartObject.HasAxis( arg2 ) and not self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += _("Chart Axis, type equals {}, group equals {}, Title equals {}").format( axisType , axisGroup , _("none")  ) 

			return  axisTitle 

		elif ElementID == xlAxisTitle:  

			axisTitle=""
			if self.excelChartObject.HasAxis( arg2 ) and self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += _("Chart Axis Title equals {} ").format( self.excelChartObject.Axes( arg2 , arg1 ).AxisTitle.Text  ) 
			elif self.excelChartObject.HasAxis( arg2 ) and not self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += _("Chart Axis Title equals {} ").format( _("none") ) 

			return  axisTitle 

		elif ElementID == xlDisplayUnitLabel:  
			return  _( "Display Unit Label") 

		elif ElementID == xlMajorGridlines:  
			return  _( "Major Gridlines" ) 

		elif ElementID == xlMinorGridlines:  
			return _( "Minor Gridlines" ) 

		elif ElementID == xlPivotChartDropZone:  
			return _( "Pivot Chart Drop Zone" ) 

		elif ElementID == xlPivotChartFieldButton:
			return _( "Pivot Chart Field Button" ) 

		elif ElementID == xlDownBars:
			return _( "Down Bars" ) 

		elif ElementID == xlDropLines:
			return _( "Drop Lines" )

		elif ElementID == xlHiLoLines:
			return  _( "Hi Lo Lines" )

		elif ElementID == xlRadarAxisLabels:
			return _( "Radar Axis Labels" )

		elif ElementID == xlSeriesLines:
			return _( "Series Lines" )

		elif ElementID == xlUpBars:
			return _( "Up Bars" )

		elif ElementID == xlChartArea:
			if reportExtraInfo:
				return _( "Chart area height equals {}, width equals {}, top equals {}, left equals {}").format ( self.excelChartObject.ChartArea.Height , self.excelChartObject.ChartArea.Width , self.excelChartObject.ChartArea.Top , self.excelChartObject.ChartArea.Left)
			else:
				return _( "Chart area ")
		elif ElementID == xlChartTitle:
			if self.excelChartObject.HasTitle:
				return _( "Chart Title equals {}").format ( self.excelChartObject.ChartTitle.Text )
			else:
				return _( "Untitled chart" )

		elif ElementID == xlCorners:
			return _( "Corners" )

		elif ElementID == xlDataTable:
			return _( "Data Table" )

		elif ElementID == xlFloor:
			return  _( "Floor" )

		elif ElementID == xlLegend:
			if self.excelChartObject.HasLegend:
				return _( "Legend" ) 
			else:
				return _( "No legend" )

		elif ElementID == xlNothing:
			return _( "xlNothing" )

		elif ElementID == xlPlotArea:
			if reportExtraInfo:
			# useing {:.0f} to remove fractions
				return _( "Plot Area inside height equals {:.0f}, inside width equals {:.0f}, inside top equals {:.0f}, inside left equals {:.0f}").format ( self.excelChartObject.PlotArea.InsideHeight , self.excelChartObject.PlotArea.InsideWidth , self.excelChartObject.PlotArea.InsideTop , self.excelChartObject.PlotArea.InsideLeft )
			else:
				return _( "Plot Area " )

		elif ElementID == xlWalls:
			return _( "Walls" )

		elif ElementID == xlDataLabel:
			return _( "Data Label" )

		elif ElementID == xlErrorBars:
			return _( "Error Bars" )

		elif ElementID == xlLegendEntry:
			return _( "Legend entry for Series {}, {} of {}").format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count ) 

		elif ElementID == xlLegendKey:
			return _( "Legend key for Series {} {} of {}").format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count )

		elif ElementID == xlTrendline:
			if self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DisplayEquation    or self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DisplayRSquared:
				trendlineText = unicode( self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DataLabel.Text ).encode("utf-8").replace("\xc2\xb2" , _( " square " ) )
				return  _( " trendline {} ").format( trendlineText ) 
			else:
				return _( "Trendline" ) 

		elif ElementID == xlXErrorBars:
			return _( "X Error Bars" )

		elif ElementID == xlYErrorBars:
			return _( "Y Error Bars" )

		elif ElementID == xlShape:
			return _( "Shape" )

	#end def _Select

	#redirects for implementations in parent excelChart object
	def script_changeSelection(self,gesture):
		self.parent.script_changeSelection(gesture)

	def script_switchToCell(self,gesture):
		self.parent.script_switchToCell(gesture)

	def script_reportTitle(self,gesture):
		self.parent.script_reportTitle(gesture)

	def script_reportCategoryAxis(self,gesture):
		self.parent.script_reportCategoryAxis(gesture)

	def script_reportValueAxis(self,gesture):
		self.parent.script_reportValueAxis(gesture)

	def script_reportSeriesAxis(self,gesture):
		self.parent.script_reportSeriesAxis(gesture)

	def script_reportSeriesSummary(self,gesture):
		self.parent.script_reportSeriesSummary(gesture)

	def script_reportSeriesFormula(self,gesture):
		self.parent.script_reportSeriesFormula(gesture)

	__gestures = {
		"kb:tab":"changeSelection",
		"kb:shift+tab":"changeSelection",
		"kb:escape": "switchToCell",
		"kb:NVDA+t" : "reportTitle",
		"kb:NVDA+shift+1" : "reportCategoryAxis",
		"kb:NVDA+shift+2" : "reportValueAxis",
		"kb:NVDA+shift+3" : "reportSeriesAxis",
		"kb:NVDA+shift+4" : "reportSeriesSummary",
		"kb:NVDA+shift+5" : "reportSeriesFormula",
		"kb:NVDA+d" : "reportCurrentChartElementWithExtraInfo",
		"kb:NVDA+f" : "reportCurrentChartElementColor",
	}




# end class ExcelChartEventHandler

class ExcelChartElementSeries(ExcelChartElementBase):

	def __init__(self, windowHandle=None , excelChartObject=None   , elementID=None  , arg1=None , arg2=None ):
		self.excelChartObject = excelChartObject
		self.elementID = elementID 
		self.arg1 = arg1
		self.arg2 = arg2
		super(ExcelChartElementSeries,self).__init__( windowHandle=windowHandle , excelChartObject=excelChartObject , elementID=elementID , arg1=arg1 , arg2=arg2 )


	def _Select(self, ElementID ,arg1,arg2 , reportExtraInfo=False ):
		if ElementID == xlSeries:
			if arg2 == -1:
				return _( "{} Series {} of {}").format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count )
			else:
# if XValue is a float, change it to int, else dates are shown with points. hope this does not introduce another bug
				if isinstance( self.excelChartObject.SeriesCollection(arg1).XValues[arg2 - 1] , float): 
					excelSeriesXValue = int(self.excelChartObject.SeriesCollection(arg1).XValues[arg2 - 1] )
				else:
					excelSeriesXValue = self.excelChartObject.SeriesCollection(arg1).XValues[arg2 - 1] 

				output=""
				if self.excelChartObject.ChartType == xlLine or self.excelChartObject.ChartType == xlLineMarkers  or self.excelChartObject.ChartType == xlLineMarkersStacked or self.excelChartObject.ChartType == xlLineMarkersStacked100 or self.excelChartObject.ChartType == xlLineStacked or self.excelChartObject.ChartType == xlLineStacked100: 
					if arg2 > 1:

						if self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] == self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2]: 
							output += _( "no change from point {}, ").format( arg2 - 1 )
						elif self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] > self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2]: 
							output += _( "Increased by {} from point {}, ").format( self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] - self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2] , arg2 - 1 ) 
						else:
							output += _( "decreased by {} from point {}, ").format( self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2] - self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] , arg2 - 1 ) 

				if self.excelChartObject.HasAxis(xlCategory) and self.excelChartObject.Axes(xlCategory).HasTitle:
					output += _( "{} {}: ").format( self.excelChartObject.Axes(xlCategory).AxisTitle.Text , excelSeriesXValue ) 
				else:
					output += _( "Category {}: ").format( excelSeriesXValue ) 

				if self.excelChartObject.HasAxis(xlValue) and self.excelChartObject.Axes(xlValue).HasTitle:
					output +=  _( "{} {}").format( self.excelChartObject.Axes(xlValue).AxisTitle.Text , self.excelChartObject.SeriesCollection(arg1).Values[arg2-1]) 
				else:
					output +=  _( "value {}").format( self.excelChartObject.SeriesCollection(arg1).Values[arg2-1]) 

				if self.excelChartObject.ChartType == xlPie or self.excelChartObject.ChartType == xlPieExploded or self.excelChartObject.ChartType == xlPieOfPie: 
					total = math.fsum( self.excelChartObject.SeriesCollection(arg1).Values ) 
					output += _( " fraction {:.2f} Percent {} {} of {}").format( self.excelChartObject.SeriesCollection(arg1).Values[arg2-1] / total *100.00 , self.GetChartSegment() ,  arg2 , len( self.excelChartObject.SeriesCollection(arg1).Values ) )
				else:
					output += _( " {} {} of {}").format( self.GetChartSegment() ,  arg2 , len( self.excelChartObject.SeriesCollection(arg1).Values ) )

				return  output 


