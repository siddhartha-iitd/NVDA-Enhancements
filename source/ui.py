#ui.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2008 NVDA Contributors <http://www.nvda-project.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""User interface functionality.
This refers to the user interface presented by the screen reader alone, not the graphical user interface.
See L{gui} for the graphical user interface.
"""

import speech
import braille
from ctypes import windll, byref, POINTER, addressof
from comtypes import IUnknown
from comtypes import automation 
from logHandler import log
import os
import sys
import gui

# From urlmon.h
URL_MK_UNIFORM = 1

# Dialog box properties
DLG_OPTIONS = "dialogWidth:350px;dialogHeight:140px;resizable:yes;center:yes;help:no"

#dwDialogFlags for ShowHTMLDialogEx from mshtmhst.h
HTMLDLG_NOUI = 0x0010 
HTMLDLG_MODAL = 0x0020 
HTMLDLG_MODELESS = 0x0040 
HTMLDLG_PRINT_TEMPLATE = 0x0080 
HTMLDLG_VERIFY = 0x0100 

def HTMLMessage(text):
	"""Invoke ShowHTMLDialog."""
	htmlFileName  = os.path.realpath( 'htmlMessage.html' )
	if not os.path.isfile(htmlFileName ): 
		raise LookupError(htmlFileName )
	log.debugWarning("htmlMessage.html path: {}".format(  htmlFileName  ))
	moniker = POINTER(IUnknown)()
	windll.urlmon.CreateURLMonikerEx(0, unicode( htmlFileName ) , byref(moniker), URL_MK_UNIFORM)
	DLG_args = automation.VARIANT("NVDA Message;{}".format( text ) )
	gui.mainFrame.prePopup() 
	error_result = windll.mshtml.ShowHTMLDialogEx( gui.mainFrame.Handle , moniker , HTMLDLG_MODELESS , addressof( DLG_args ) , unicode(DLG_OPTIONS ), None)
	gui.mainFrame.postPopup() 

def message(text):
	"""Present a message to the user.
	The message will be presented in both speech and braille.
	@param text: The text of the message.
	@type text: str
	"""
	speech.speakMessage(text)
	braille.handler.message(text)


