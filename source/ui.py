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

import threading
from logHandler import log
import inspect
from logHandler import getCodePath

import os
import sys

showHTMLDialogThread = None

# From urlmon.h
URL_MK_UNIFORM = 1

# Dialog box properties
DLG_OPTIONS = "dialogWidth:350px;dialogHeight:140px;center:yes;help:no"

class HTMLDialogThread(threading.Thread):

	def __init__( self , message ):
		super( HTMLDialogThread , self ).__init__()
		self.message = message

	def run(self):

		dialogTemplatePath = os.path.dirname(sys.argv[0]) + "\\HTMLMessage.html" 

		moniker = POINTER(IUnknown)()
		windll.urlmon.CreateURLMonikerEx(0, unicode(dialogTemplatePath) , byref(moniker), URL_MK_UNIFORM)

		DLG_args = automation.VARIANT("NVDA Message;{}".format(self.message ) )

		error_result = windll.mshtml.ShowHTMLDialog(None, moniker, addressof( DLG_args ) , unicode(DLG_OPTIONS ), None)

def message(text):
	"""Present a message to the user.
	The message will be presented in both speech and braille.
	@param text: The text of the message.
	@type text: str
	"""
	speech.speakMessage(text)
	braille.handler.message(text)

def HTMLMessage(text):
	"""Invoke ShowHTMLDialog."""
	log.debugWarning("path: {}".format( os.path.dirname(sys.argv[0]) + "\\HTMLMessage.html" ) )
	showHTMLDialogThread = HTMLDialogThread(text )
	showHTMLDialogThread.start()
