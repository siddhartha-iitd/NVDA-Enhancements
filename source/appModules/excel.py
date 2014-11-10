import appModuleHandler
from NVDAObjects.IAccessible import IAccessible
import controlTypes
import ui
from NVDAObjects.window.excelChart import ExcelChart

class AppModule(appModuleHandler.AppModule):
	oldChart = None

	def event_NVDAObject_init(self, obj):
		if ( type(obj).__name__ == "ExcelChart"): 
			if self.oldChart: 
				self.oldChart.clearExcelEvents()
			obj.initExcelEvents()
			self.oldChart = obj



