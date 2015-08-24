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
        
    def event_stateChange(self, obj, nextHandler):
        if obj.name== "Selection Mode Extend Selection" or obj.name== "Selection Mode Add to Selection":
            return
        nextHandler()
        
    def event_nameChange(self, obj, nextHandler):
        #to report selection mode in version 2010 and above
        if obj.name== "Selection Mode Extend Selection" or obj.name== "Selection Mode Add to Selection":
            ui.message(obj.name)
            return
        
        #to report selection mode in version below 2010
        elif obj.value== "Extend Selection" or obj.value== "Add to Selection":
            ui.message(obj.name + obj.value)
            return
        nextHandler()
        
    #to report selection mode in version below 2010
    def event_valueChange(self, obj, nextHandler):
        if obj.value== "Extend Selection" or obj.value== "Add to Selection":
            ui.message(obj.name + obj.value)
            return
        nextHandler()
