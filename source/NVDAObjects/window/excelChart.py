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

from comtypes.client import *

import comtypes.GUID
import _winreg
from comtypes.client._generate import GetModule
import math
from NVDAObjects import NVDAObject
import string
excelCLSID = comtypes.GUID.from_progid("Excel.Application")
#print excelCLSID 
regValue= ("\CLSID\%s\LocalServer32" %(excelCLSID))

excelRegHandle = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, regValue)
if  excelRegHandle:
	excelPath = _winreg.QueryValue( excelRegHandle , "")
	log.debugWarning("registry path: {}".format( excelPath ) )
	excelPath = excelPath.rstrip( " /automation" )
	log.debugWarning("registry path after strip: {}".format( excelPath ) )
	GetModule(excelPath) 
	from comtypes.gen import Excel
	_winreg.CloseKey( excelRegHandle )

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





class ExcelChart(excel.ExcelBase):
	def __init__(self,windowHandle=None,excelWindowObject=None,excelChartObject=None):
		self.excelWindowObject=excelWindowObject
		self.excelChartObject=excelChartObject
		self.excelChartEventHandlerObject = ExcelChartEventHandler( windowHandle=windowHandle)
		self.excelChartEventHandlerObject.excelChartObject= self.excelChartObject
		self.excelChartEventConnection = GetEvents( self.excelChartObject , self.excelChartEventHandlerObject , Excel.ChartEvents)
		super(ExcelChart,self).__init__(windowHandle=windowHandle)
		for gesture in self.__changeSelectionGestures:
			self.bindGesture(gesture, "changeSelection")

	def _isEqual(self, other):
		if not super(ExcelChart, self)._isEqual(other):
			return False
		return self.excelChartObject.Parent.Index == other.excelChartObject.Parent.Index

	def _get_name(self):
		name=self.excelChartObject.Name
		return _("%s chart" %(name))

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

	def script_speakSeriesInfo(self, gesture):
		count = self.excelChartObject.SeriesCollection().count
		if count>0:
			seriesValueString="%d series in this chart" %(count)
			for i in xrange(1, count+1):
				seriesValueString += ", Series %d %s" %(i, self.excelChartObject.SeriesCollection(i).Name)
			text=_(seriesValueString)	
		else:
			text=_("No Series defined.")
		speech.speak([text])


	def script_speakSummary(self, gesture):
		count = self.excelChartObject.SeriesCollection().count
		if count>0:
			seriesValueString="%d series in this chart" %(count)
			for i in xrange(1, count+1):
				seriesValueString += ", Series %d %s" %(i, self.excelChartObject.SeriesCollection(i).Name)
			text=_(seriesValueString)	
		else:
			text=_("No Series defined.")
		speech.speak([text])


	__gestures = {
		"kb:escape": "switchToCell",
		"kb:NVDA+t" : "speakTitle",
		"kb:NVDA+shift+1" : "speakType",		
		"kb:NVDA+shift+2" : "speakName",
		"kb:NVDA+shift+3" : "speakCategoryAxis",
		"kb:NVDA+shift+4" : "speakValueAxis",
		"kb:NVDA+shift+5" : "speakSeriesAxis",
		"kb:NVDA+shift+6" : "speakSeriesInfo",
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

class ExcelChartEventHandler(Window):

	def __init__(self, windowHandle  ):
		self.windowHandle=windowHandle 
		#self.excelChartObject = excelChartObject
		super(ExcelChartEventHandler ,self).__init__(windowHandle=windowHandle)


	def GetChartSegment(self):
		chartType = self.excelChartObject.ChartType
		if chartType in chartSegmentDict.keys():
			text= chartSegmentDict[chartType]
		else:
			text=_("item")
		return text

	def ChartEvents_Select(self, this, ElementID ,arg1,arg2):
		self.elementID = ElementID 
		self.arg1 = arg1
		self.arg2 = arg2
		eventHandler.queueEvent("stateChange", self )

	def event_stateChange(self):
		self._Select(self.elementID , self.arg1 , self.arg2)

	def _Select(self, ElementID ,arg1,arg2):
		
		if ElementID == Excel.xlAxis:
			if arg1 == xlPrimary: 
				axisGroup = "Primary"
			elif arg1 == xlSecondary :
				axisGroup = "Secondary"

			if arg2 == xlCategory: 
				axisType= "Category"
			elif arg2 == xlValue:
				axisType= "Value"
			elif arg2 == xlSeriesAxis: 
				axisType= "Series"

			axisTitle=""
			if self.excelChartObject.HasAxis( arg2 ) and self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += "Chart Axis, type equals {}, group equals {}, Title equals {}".format( axisType , axisGroup , self.excelChartObject.Axes( arg2 , arg1 ).AxisTitle.Text ) 
			elif self.excelChartObject.HasAxis( arg2 ) and not self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += "Chart Axis, type equals {}, group equals {}, Title equals {}".format( axisType , axisGroup , "none"  ) 

			ui.message ( axisTitle )

		elif ElementID == Excel.xlAxisTitle:  

			axisTitle=""
			if self.excelChartObject.HasAxis( arg2 ) and self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += "Chart Axis Title equals {} ".format( self.excelChartObject.Axes( arg2 , arg1 ).AxisTitle.Text  ) 
			elif self.excelChartObject.HasAxis( arg2 ) and not self.excelChartObject.Axes( arg2 ).HasTitle:
				axisTitle += "Chart Axis Title equals {} ".format( "none" ) 



			ui.message ( axisTitle )



		elif ElementID == Excel.xlDisplayUnitLabel:  
			ui.message ( _( "xlDisplayUnitLabel") )

		elif ElementID == Excel.xlDisplayUnitLabel:  
			ui.message ( _( "xlDisplayUnitLabel") )

		elif ElementID == Excel.xlMajorGridlines:  
			ui.message ( "xlMajorGridlines" )

		elif ElementID == Excel.xlMinorGridlines:  
			ui.message ( "xlMinorGridlines" )

		elif ElementID == Excel.xlPivotChartDropZone:  
			ui.message ( "xlPivotChartDropZone" )

		elif ElementID == Excel.xlPivotChartFieldButton:
			ui.message ( "xlPivotChartFieldButton" )

		elif ElementID == Excel.xlDownBars:
			ui.message ( "xlDownBars" )

		elif ElementID == Excel.xlDropLines:
			ui.message ( "xlDropLines" )

		elif ElementID == Excel.xlHiLoLines:
			ui.message ( "xlHiLoLines" )

		elif ElementID == Excel.xlRadarAxisLabels:
			ui.message ( "xlRadarAxisLabels" )

		elif ElementID == Excel.xlSeriesLines:
			ui.message ( "xlSeriesLines" )

		elif ElementID == Excel.xlUpBars:
			ui.message ( "xlUpBars" )

		elif ElementID == Excel.xlChartArea:
			ui.message ( "Chart area height equals {}, width equals {}, top equals {}, left equals {}".format ( self.excelChartObject.ChartArea.Height , self.excelChartObject.ChartArea.Width , self.excelChartObject.ChartArea.Top , self.excelChartObject.ChartArea.Left) )

		elif ElementID == Excel.xlChartTitle:
			if self.excelChartObject.HasTitle:
				ui.message ( "Chart Title equals {}".format ( self.excelChartObject.ChartTitle.Text ) )
			else:
				ui.message ( "Untitled chart" )

		elif ElementID == Excel.xlCorners:
			ui.message ( "xlCorners" )

		elif ElementID == Excel.xlDataTable:
			ui.message ( "xlDataTable" )

		elif ElementID == Excel.xlFloor:
			ui.message ( "xlFloor" )

		elif ElementID == Excel.xlLegend:
			if self.excelChartObject.HasLegend:
				ui.message ( "Legend") 
			else:
				ui.message ( "No legend" )




		elif ElementID == Excel.xlNothing:
			ui.message ( "xlNothing" )

		elif ElementID == Excel.xlPlotArea:
			ui.message ( "Plot Area inside height equals {:.0f}, inside width equals {:.0f}, inside top equals {:.0f}, inside left equals {:.0f}".format ( self.excelChartObject.PlotArea.InsideHeight , self.excelChartObject.PlotArea.InsideWidth , self.excelChartObject.PlotArea.InsideTop , self.excelChartObject.PlotArea.InsideLeft ))

		elif ElementID == Excel.xlWalls:
			ui.message ( "xlWalls" )

		elif ElementID == Excel.xlDataLabel:
			ui.message ( "xlDataLabel" )

		elif ElementID == Excel.xlErrorBars:
			ui.message ( "xlErrorBars" )

		elif ElementID == Excel.xlLegendEntry:
			ui.message ( "Legend entry for Series {}, {} of {}".format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count ) )

		elif ElementID == Excel.xlLegendKey:
			ui.message ( "Legend key for Series {} {} of {}".format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count ) )

		elif ElementID == Excel.xlSeries:
			if arg2 == -1:
				ui.message ( "{0} Series {1} of {2}".format( self.excelChartObject.SeriesCollection(arg1).Name , arg1 , self.excelChartObject.SeriesCollection().Count ) )
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
							output += "no change from point {}, ".format( arg2 - 1 )
						elif self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] > self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2]: 
							output += "Increased by {} from point {}, ".format( self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] - self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2] , arg2 - 1 ) 
						else:
							output += "decreased by {} from point {}, ".format( self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 2] - self.excelChartObject.SeriesCollection(arg1).Values[arg2 - 1] , arg2 - 1 ) 

				if self.excelChartObject.HasAxis(Excel.xlCategory) and self.excelChartObject.Axes(Excel.xlCategory).HasTitle:
					output += "{0} {1}: ".format( self.excelChartObject.Axes(Excel.xlCategory).AxisTitle.Text , excelSeriesXValue ) 
				else:
					output += "Category {0}: ".format( excelSeriesXValue ) 

				if self.excelChartObject.HasAxis(Excel.xlValue) and self.excelChartObject.Axes(Excel.xlValue).HasTitle:
					output +=  "{0} {1}".format( self.excelChartObject.Axes(Excel.xlValue).AxisTitle.Text , self.excelChartObject.SeriesCollection(arg1).Values[arg2-1]) 
				else:
					output +=  "value {0}".format( self.excelChartObject.SeriesCollection(arg1).Values[arg2-1]) 

				if self.excelChartObject.ChartType == xlPie or self.excelChartObject.ChartType == xlPieExploded or self.excelChartObject.ChartType == xlPieOfPie: 
					total = math.fsum( self.excelChartObject.SeriesCollection(arg1).Values ) 
					output += " fraction {0:.2f} Percent {1} {2} of {3}".format( self.excelChartObject.SeriesCollection(arg1).Values[arg2-1] / total *100.00 , self.GetChartSegment() ,  arg2 , len( self.excelChartObject.SeriesCollection(arg1).Values ) )
				else:
					output += " {0} {1} of {2}".format( self.GetChartSegment() ,  arg2 , len( self.excelChartObject.SeriesCollection(arg1).Values ) )

				ui.message ( output )


			#ui.message ( "xlSeries: SeriesIndex {0} PointIndex {1}".format( arg1 , arg2 ) )
			#ui.message ( self.excelChartObject.SeriesCollection(arg1).Points(arg2).DataLabel.Text )


		elif ElementID == Excel.xlTrendline:
			if self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DisplayEquation    or self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DisplayRSquared:
				trendlineText = unicode( self.excelChartObject.SeriesCollection(arg1).Trendlines(arg2).DataLabel.Text ).encode("utf-8").replace("\xc2\xb2"," square " )
				ui.message ( " trendline {0} ".format( trendlineText )) 
			else:
				ui.message ( "Trendline" )

		elif ElementID == Excel.xlXErrorBars:
			ui.message ( "xlXErrorBars" )

		elif ElementID == Excel.xlYErrorBars:
			ui.message ( "xlYErrorBars" )

		elif ElementID == Excel.xlShape:
			ui.message ( _("xlShape" ) )

		#print "selection changed: element {0}, arg1 {1}, arg2 {2}.".format(ElementID,arg1,arg2)
	#end def _Select
# end class ExcelChartEventHandler


