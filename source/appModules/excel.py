#appModules/excel.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import appModuleHandler
import controlTypes
import api
import speech
import winUser
import ui                     

class AppModule(appModuleHandler.AppModule):
        
    def event_nameChange(self, obj, nextHandler):
        if obj.name== "Selection Mode Extend Selection" or obj.name== "Selection Mode Add to Selection":
            ui.message(obj.name)
            return
        nextHandler()
        
    def event_stateChange(self, obj, nextHandler):
        if obj.name== "Selection Mode Extend Selection" or obj.name== "Selection Mode Add to Selection":
            ui.message(obj.name)
            return
        nextHandler()

 
