
import profile
import speech
from speech import SpeechCommand
from speech import LangChangeCommand
import languageHandler
import config
from logHandler import log
from unicodeScriptData import scriptCode

# maintains list of priority languages as a list of languageID, ScriptName, and LanguageDescription
languagePriorityListSpec = []

def initialize():
	updateLanguagePriorityFromConfig()

def updateLanguagePriorityFromConfig():
	"""read string from config and convert it to list"""
	global languagePriorityListSpec 
	tempList = []
	try:
		languageList = config.conf["writingScripts"]["languagePriorityList"]
		for language in languageList: 
			tempList.append( [ language , getScriptIDFromLangID(language) , getLanguageDescription( language ) ]) 
		languagePriorityListSpec = tempList 
	except KeyError:
		pass

langIDToScriptID= {
	"af_ZA" : "Latin",
	"am" : "Armenian",
	"ar" : "Arabic",
	"as" : "Bengali",
	"bg" : "Cyrillic",
	"bn" : "Bengali",
	"ca" : "Latin",
	"cs" : "Latin",
	"da" : "Latin",
	"de" : "Latin",
	"el" : "Latin",
	"en" : "Latin",
	"es" : "Latin",
	"fr" : "Latin",
	"gu" : "Gujarati",
	"hi" : "Devanagari",
	"kn" : "Kannada",
	"ml" : "Malayalam",
	"mn" : "Mongolian",
	"mr" : "Devanagari",
	"ne" : "Devanagari",
	"or" : "Oriya",
	"pa" : "Gurmukhi",
	"sa" : "Devanagari",
	"sq" : "Caucasian_Albanian",
	"ta" : "Tamil",
	"te" : "Telugu",
}

#reverse of langIDToScriptID, required to obtain language id for a specific script 
scriptIDToLangID = {script: lang for lang, script in langIDToScriptID.iteritems()} 

def getLanguagesWithDescriptions():
	"""generates a list of locale names, plus their full localized language and country names.
	@rtype: list of tuples
	"""
	#Make a list of all the languages found for language to script mapping
	allLanguages  = langIDToScriptID.keys()
	allLanguages.sort()
	languageDescriptions = []
	addedLangs = {lang[0] for lang in languagePriorityListSpec}
	for language in allLanguages:  
		if language in addedLangs: 
			continue
		else:
			desc=languageHandler.getLanguageDescription(language )
			label="%s, %s"%(desc,language ) if desc else language 
			languageDescriptions.append((language , label))
	return languageDescriptions

def getScriptCode(chr):
	"""performs a binary search in scripCodes for unicode ranges
	@param chr: character for which a script should be found
	@type chr: string
	@return: script code
	@rtype: int"""
	mStart = 0
	mEnd = len(scriptCode)-1
	characterUnicodeCode = ord(chr)
	while( mEnd >= mStart ):
		midPoint = (mStart + mEnd ) >> 1
		if characterUnicodeCode < scriptCode[midPoint][0]: 
			mEnd = midPoint -1
		elif characterUnicodeCode > scriptCode[midPoint][1]: 
			mStart = midPoint + 1
		else:
			return scriptCode[midPoint][2] 
	return None

def getLangID(scriptName ):
	"""This function is the heart of determining which language is selected for a script
	@param scriptName: the unicode name of the  script
	@type scriptName: string
	@return: It returns languageID for a script. it first checks whether there is a language for the script in the languagePriorityListSpec. If not, then it checks whether default language script is same as the script. At last it returns languageID for the script from scriptIDToLangID.
	@rtype: string"""
	# we are using loop during search to maintain priority
	for priorityLanguage, priorityScript, priorityDescription in  languagePriorityListSpec:
		if scriptName == priorityScript: 
			return priorityLanguage
	#language not found in the languagePriorityListSpec, so check if default language can be applied for the script
	if scriptName == getScriptIDFromLangID(languageHandler.getLanguage() ):
		return  languageHandler.getLanguage()
	# default language is not applicable for this script, so look up in the scriptIDToLangID
	return scriptIDToLangID.get (scriptName )

def getLanguageDescription(language ):
	desc=languageHandler.getLanguageDescription(language )
	label="%s, %s"%(desc,language ) if desc else language 
	return label

def getScriptIDFromLangID(langID ):
	return langIDToScriptID.get (langID )

class ScriptChangeCommand(SpeechCommand):
	"""A command to switch the script during script detection ."""

	def __init__(self, scriptCode):
		"""
		@param scriptCode: the script identifier
		@type scriptCode: int
		"""
		self.scriptCode =scriptCode 

	def __repr__(self):
		return "ScriptChangeCommand (%r)"%self.scriptCode

def detectScript(text):
	"""splits a string if there are multiple scripts in it
	@param text: the text string
	@type string
	@return: sequence of script commands and text
	@rtype: list"""
	unicodeSequence = []
	currentScript = getScriptCode(  text[0])
	oldScript = currentScript
	unicodeSequence.append(ScriptChangeCommand(currentScript)) 
	beginIndex = 0
	for index in xrange( len(text) ) :
		currentScript = getScriptCode( text[index] ) 
		if currentScript == "Common": 
			continue

		if currentScript != oldScript:
			newText = text[beginIndex:index] 
			unicodeSequence.append( newText )
			beginIndex= index
			unicodeSequence.append(ScriptChangeCommand(currentScript)) 
		oldScript = currentScript

	unicodeSequence.append( text[beginIndex:] )
	return unicodeSequence

def detectLanguage(text, preferredLanguage =None):
	"""splits a string if there are multiple languages in it. uses detectScript
	@param text: the text string
	@type text: string
	@param preferredLanguage: the preferred language for a script 
	@type languageToBeIgnored: string or None
	@return: sequence of language commands and text
	@rtype: list"""
	sequenceWithLanguage= []
	tempSequence = detectScript(text)
	scriptIDForPreferredLanguage = getScriptIDFromLangID( preferredLanguage )
	for index in xrange(len(tempSequence )):
		item= tempSequence [index]
		if isinstance(item,ScriptChangeCommand):
			# check if priority language for a script is available, if yes, add that language instead of language from priority list
			if preferredLanguage and (item.scriptCode == scriptIDForPreferredLanguage): 
				if index == 0: continue # if it is first item and same as the priority language, language code is already added.
				languageCode = preferredLanguage 
			else:
				languageCode = getLangID( item.scriptCode  )  
			if languageCode:
				sequenceWithLanguage.append( LangChangeCommand( languageHandler.normalizeLanguage( languageCode ) ) )
		else:
			sequenceWithLanguage.append(item)
	return sequenceWithLanguage
