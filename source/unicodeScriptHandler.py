
import profile
import speech
from speech import ScriptChangeCommand
from speech import LangChangeCommand
import languageHandler
import config
from logHandler import log

# maintains list of priority languages 
languagePriorityListSpec = []

#reverse of langIDToScriptID, required to obtain language id for a specific script 
scriptIDToLangID = {}

def initialize():
	for languageID in langIDToScriptID.keys():
		scriptIDToLangID.setdefault( langIDToScriptID[languageID] , languageID )
	updateLanguagePriorityFromConfig()

def updateLanguagePriorityFromConfig():
	"""read string from config and convert it to list"""
	global languagePriorityListSpec 
	tempList = []
	languageList = config.conf["writingScriptsToLanguage"]["languagePriorityList"].split(",")
	for language in languageList: 
		tempList.append( [ language , getScriptIDFromLangID(language) , getLanguageDescription( language ) ]) 
	languagePriorityListSpec = tempList 

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

def getLanguagesWithDescriptions():
	"""generates a list of locale names, plus their full localized language and country names.
	@rtype: list of tuples
	"""
	#Make a list of all the languages found for language to script mapping
	allLanguages  = langIDToScriptID.keys()
	allLanguages.sort()
	languageCodes = [] 
	languageDescriptions = []
	for language in allLanguages:  
		if language in [j for i in languagePriorityListSpec for j in i]:
			continue
		else:
			languageCodes.append(language )
			desc=languageHandler.getLanguageDescription(language )
			label="%s, %s"%(desc,language ) if desc else language 
			languageDescriptions.append(label)
	return zip(languageCodes , languageDescriptions)

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
	# we are using loop during search to maintain priority
	for index in xrange( len( languagePriorityListSpec) ) :
		if scriptName == languagePriorityListSpec[index][1]: 
			return languagePriorityListSpec[index][0] 
	#language not found in the priority list, so look up in the default mapping
	try:
		return scriptIDToLangID.get (scriptName )
	except KeyError:
		return None

def getLanguageDescription(language ):
	desc=languageHandler.getLanguageDescription(language )
	label="%s, %s"%(desc,language ) if desc else language 
	return label

def getScriptIDFromLangID(langID ):
	try:
		return langIDToScriptID.get (langID )
	except KeyError:
		return None

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

def detectLanguage(text, defaultLanguageForScript  =None):
	"""splits a string if there are multiple languages in it. uses detectScript
	@param text: the text string
	@type text: string
	@param defaultLanguageForScript : the default language for a script 
	@type languageToBeIgnored: string or None
	@return: sequence of language commands and text
	@rtype: list"""
	sequenceWithLanguage= []
	tempSequence = detectScript(text)
	for index in xrange(len(tempSequence )):
		item= tempSequence [index]
		if isinstance(item,ScriptChangeCommand):
			# check if default language for a script is available, if yes, add that language instead of language from priority list
			if defaultLanguageForScript  and item.scriptCode == getScriptIDFromLangID( defaultLanguageForScript  ):
				if index == 0: continue # if it is first item and same as the default language, language code is already added.
				languageCode = defaultLanguageForScript
			else:
				languageCode = getLangID( item.scriptCode  )  
			if languageCode:
				sequenceWithLanguage.append( LangChangeCommand( languageHandler.normalizeLanguage( languageCode ) ) )
		else:
			sequenceWithLanguage.append(item)
	return sequenceWithLanguage

# generated by unicodeScriptPrep.py
scriptCode= [
	( 0X0 , 0X40 , "Common" ), # Common
	( 0X41 , 0X5a , "Latin" ), # Latin
	( 0X5b , 0X60 , "Common" ), # Common
	( 0X61 , 0X7a , "Latin" ), # Latin
	( 0X7b , 0Xa9 , "Common" ), # Common
	( 0Xaa , 0Xaa , "Latin" ), # Latin
	( 0Xab , 0Xb9 , "Common" ), # Common
	( 0Xba , 0Xba , "Latin" ), # Latin
	( 0Xbb , 0Xbf , "Common" ), # Common
	( 0Xc0 , 0Xd6 , "Latin" ), # Latin
	( 0Xd7 , 0Xd7 , "Common" ), # Common
	( 0Xd8 , 0Xf6 , "Latin" ), # Latin
	( 0Xf7 , 0Xf7 , "Common" ), # Common
	( 0Xf8 , 0X2b8 , "Latin" ), # Latin
	( 0X2b9 , 0X2df , "Common" ), # Common
	( 0X2e0 , 0X2e4 , "Latin" ), # Latin
	( 0X2e5 , 0X2e9 , "Common" ), # Common
	( 0X2ea , 0X2eb , "Bopomofo" ), # Bopomofo
	( 0X2ec , 0X2ff , "Common" ), # Common
	( 0X300 , 0X36f , "Inherited" ), # Inherited
	( 0X370 , 0X373 , "Greek" ), # Greek
	( 0X374 , 0X374 , "Common" ), # Common
	( 0X375 , 0X377 , "Greek" ), # Greek
	( 0X37a , 0X37d , "Greek" ), # Greek
	( 0X37e , 0X37e , "Common" ), # Common
	( 0X37f , 0X37f , "Greek" ), # Greek
	( 0X384 , 0X384 , "Greek" ), # Greek
	( 0X385 , 0X385 , "Common" ), # Common
	( 0X386 , 0X386 , "Greek" ), # Greek
	( 0X387 , 0X387 , "Common" ), # Common
	( 0X388 , 0X38a , "Greek" ), # Greek
	( 0X38c , 0X38c , "Greek" ), # Greek
	( 0X38e , 0X3a1 , "Greek" ), # Greek
	( 0X3a3 , 0X3e1 , "Greek" ), # Greek
	( 0X3e2 , 0X3ef , "Coptic" ), # Coptic
	( 0X3f0 , 0X3ff , "Greek" ), # Greek
	( 0X400 , 0X484 , "Cyrillic" ), # Cyrillic
	( 0X485 , 0X486 , "Inherited" ), # Inherited
	( 0X487 , 0X52f , "Cyrillic" ), # Cyrillic
	( 0X531 , 0X556 , "Armenian" ), # Armenian
	( 0X559 , 0X55f , "Armenian" ), # Armenian
	( 0X561 , 0X587 , "Armenian" ), # Armenian
	( 0X589 , 0X589 , "Common" ), # Common
	( 0X58a , 0X58a , "Armenian" ), # Armenian
	( 0X58d , 0X58f , "Armenian" ), # Armenian
	( 0X591 , 0X5c7 , "Hebrew" ), # Hebrew
	( 0X5d0 , 0X5ea , "Hebrew" ), # Hebrew
	( 0X5f0 , 0X5f4 , "Hebrew" ), # Hebrew
	( 0X600 , 0X604 , "Arabic" ), # Arabic
	( 0X605 , 0X605 , "Common" ), # Common
	( 0X606 , 0X60b , "Arabic" ), # Arabic
	( 0X60c , 0X60c , "Common" ), # Common
	( 0X60d , 0X61a , "Arabic" ), # Arabic
	( 0X61b , 0X61c , "Common" ), # Common
	( 0X61e , 0X61e , "Arabic" ), # Arabic
	( 0X61f , 0X61f , "Common" ), # Common
	( 0X620 , 0X63f , "Arabic" ), # Arabic
	( 0X640 , 0X640 , "Common" ), # Common
	( 0X641 , 0X64a , "Arabic" ), # Arabic
	( 0X64b , 0X655 , "Inherited" ), # Inherited
	( 0X656 , 0X66f , "Arabic" ), # Arabic
	( 0X670 , 0X670 , "Inherited" ), # Inherited
	( 0X671 , 0X6dc , "Arabic" ), # Arabic
	( 0X6dd , 0X6dd , "Common" ), # Common
	( 0X6de , 0X6ff , "Arabic" ), # Arabic
	( 0X700 , 0X70d , "Syriac" ), # Syriac
	( 0X70f , 0X74a , "Syriac" ), # Syriac
	( 0X74d , 0X74f , "Syriac" ), # Syriac
	( 0X750 , 0X77f , "Arabic" ), # Arabic
	( 0X780 , 0X7b1 , "Thaana" ), # Thaana
	( 0X7c0 , 0X7fa , "Nko" ), # Nko
	( 0X800 , 0X82d , "Samaritan" ), # Samaritan
	( 0X830 , 0X83e , "Samaritan" ), # Samaritan
	( 0X840 , 0X85b , "Mandaic" ), # Mandaic
	( 0X85e , 0X85e , "Mandaic" ), # Mandaic
	( 0X8a0 , 0X8b4 , "Arabic" ), # Arabic
	( 0X8e3 , 0X8ff , "Arabic" ), # Arabic
	( 0X900 , 0X950 , "Devanagari" ), # Devanagari
	( 0X951 , 0X952 , "Inherited" ), # Inherited
	( 0X953 , 0X963 , "Devanagari" ), # Devanagari
	( 0X964 , 0X965 , "Common" ), # Common
	( 0X966 , 0X97f , "Devanagari" ), # Devanagari
	( 0X980 , 0X983 , "Bengali" ), # Bengali
	( 0X985 , 0X98c , "Bengali" ), # Bengali
	( 0X98f , 0X990 , "Bengali" ), # Bengali
	( 0X993 , 0X9a8 , "Bengali" ), # Bengali
	( 0X9aa , 0X9b0 , "Bengali" ), # Bengali
	( 0X9b2 , 0X9b2 , "Bengali" ), # Bengali
	( 0X9b6 , 0X9b9 , "Bengali" ), # Bengali
	( 0X9bc , 0X9c4 , "Bengali" ), # Bengali
	( 0X9c7 , 0X9c8 , "Bengali" ), # Bengali
	( 0X9cb , 0X9ce , "Bengali" ), # Bengali
	( 0X9d7 , 0X9d7 , "Bengali" ), # Bengali
	( 0X9dc , 0X9dd , "Bengali" ), # Bengali
	( 0X9df , 0X9e3 , "Bengali" ), # Bengali
	( 0X9e6 , 0X9fb , "Bengali" ), # Bengali
	( 0Xa01 , 0Xa03 , "Gurmukhi" ), # Gurmukhi
	( 0Xa05 , 0Xa0a , "Gurmukhi" ), # Gurmukhi
	( 0Xa0f , 0Xa10 , "Gurmukhi" ), # Gurmukhi
	( 0Xa13 , 0Xa28 , "Gurmukhi" ), # Gurmukhi
	( 0Xa2a , 0Xa30 , "Gurmukhi" ), # Gurmukhi
	( 0Xa32 , 0Xa33 , "Gurmukhi" ), # Gurmukhi
	( 0Xa35 , 0Xa36 , "Gurmukhi" ), # Gurmukhi
	( 0Xa38 , 0Xa39 , "Gurmukhi" ), # Gurmukhi
	( 0Xa3c , 0Xa3c , "Gurmukhi" ), # Gurmukhi
	( 0Xa3e , 0Xa42 , "Gurmukhi" ), # Gurmukhi
	( 0Xa47 , 0Xa48 , "Gurmukhi" ), # Gurmukhi
	( 0Xa4b , 0Xa4d , "Gurmukhi" ), # Gurmukhi
	( 0Xa51 , 0Xa51 , "Gurmukhi" ), # Gurmukhi
	( 0Xa59 , 0Xa5c , "Gurmukhi" ), # Gurmukhi
	( 0Xa5e , 0Xa5e , "Gurmukhi" ), # Gurmukhi
	( 0Xa66 , 0Xa75 , "Gurmukhi" ), # Gurmukhi
	( 0Xa81 , 0Xa83 , "Gujarati" ), # Gujarati
	( 0Xa85 , 0Xa8d , "Gujarati" ), # Gujarati
	( 0Xa8f , 0Xa91 , "Gujarati" ), # Gujarati
	( 0Xa93 , 0Xaa8 , "Gujarati" ), # Gujarati
	( 0Xaaa , 0Xab0 , "Gujarati" ), # Gujarati
	( 0Xab2 , 0Xab3 , "Gujarati" ), # Gujarati
	( 0Xab5 , 0Xab9 , "Gujarati" ), # Gujarati
	( 0Xabc , 0Xac5 , "Gujarati" ), # Gujarati
	( 0Xac7 , 0Xac9 , "Gujarati" ), # Gujarati
	( 0Xacb , 0Xacd , "Gujarati" ), # Gujarati
	( 0Xad0 , 0Xad0 , "Gujarati" ), # Gujarati
	( 0Xae0 , 0Xae3 , "Gujarati" ), # Gujarati
	( 0Xae6 , 0Xaf1 , "Gujarati" ), # Gujarati
	( 0Xaf9 , 0Xaf9 , "Gujarati" ), # Gujarati
	( 0Xb01 , 0Xb03 , "Oriya" ), # Oriya
	( 0Xb05 , 0Xb0c , "Oriya" ), # Oriya
	( 0Xb0f , 0Xb10 , "Oriya" ), # Oriya
	( 0Xb13 , 0Xb28 , "Oriya" ), # Oriya
	( 0Xb2a , 0Xb30 , "Oriya" ), # Oriya
	( 0Xb32 , 0Xb33 , "Oriya" ), # Oriya
	( 0Xb35 , 0Xb39 , "Oriya" ), # Oriya
	( 0Xb3c , 0Xb44 , "Oriya" ), # Oriya
	( 0Xb47 , 0Xb48 , "Oriya" ), # Oriya
	( 0Xb4b , 0Xb4d , "Oriya" ), # Oriya
	( 0Xb56 , 0Xb57 , "Oriya" ), # Oriya
	( 0Xb5c , 0Xb5d , "Oriya" ), # Oriya
	( 0Xb5f , 0Xb63 , "Oriya" ), # Oriya
	( 0Xb66 , 0Xb77 , "Oriya" ), # Oriya
	( 0Xb82 , 0Xb83 , "Tamil" ), # Tamil
	( 0Xb85 , 0Xb8a , "Tamil" ), # Tamil
	( 0Xb8e , 0Xb90 , "Tamil" ), # Tamil
	( 0Xb92 , 0Xb95 , "Tamil" ), # Tamil
	( 0Xb99 , 0Xb9a , "Tamil" ), # Tamil
	( 0Xb9c , 0Xb9c , "Tamil" ), # Tamil
	( 0Xb9e , 0Xb9f , "Tamil" ), # Tamil
	( 0Xba3 , 0Xba4 , "Tamil" ), # Tamil
	( 0Xba8 , 0Xbaa , "Tamil" ), # Tamil
	( 0Xbae , 0Xbb9 , "Tamil" ), # Tamil
	( 0Xbbe , 0Xbc2 , "Tamil" ), # Tamil
	( 0Xbc6 , 0Xbc8 , "Tamil" ), # Tamil
	( 0Xbca , 0Xbcd , "Tamil" ), # Tamil
	( 0Xbd0 , 0Xbd0 , "Tamil" ), # Tamil
	( 0Xbd7 , 0Xbd7 , "Tamil" ), # Tamil
	( 0Xbe6 , 0Xbfa , "Tamil" ), # Tamil
	( 0Xc00 , 0Xc03 , "Telugu" ), # Telugu
	( 0Xc05 , 0Xc0c , "Telugu" ), # Telugu
	( 0Xc0e , 0Xc10 , "Telugu" ), # Telugu
	( 0Xc12 , 0Xc28 , "Telugu" ), # Telugu
	( 0Xc2a , 0Xc39 , "Telugu" ), # Telugu
	( 0Xc3d , 0Xc44 , "Telugu" ), # Telugu
	( 0Xc46 , 0Xc48 , "Telugu" ), # Telugu
	( 0Xc4a , 0Xc4d , "Telugu" ), # Telugu
	( 0Xc55 , 0Xc56 , "Telugu" ), # Telugu
	( 0Xc58 , 0Xc5a , "Telugu" ), # Telugu
	( 0Xc60 , 0Xc63 , "Telugu" ), # Telugu
	( 0Xc66 , 0Xc6f , "Telugu" ), # Telugu
	( 0Xc78 , 0Xc7f , "Telugu" ), # Telugu
	( 0Xc81 , 0Xc83 , "Kannada" ), # Kannada
	( 0Xc85 , 0Xc8c , "Kannada" ), # Kannada
	( 0Xc8e , 0Xc90 , "Kannada" ), # Kannada
	( 0Xc92 , 0Xca8 , "Kannada" ), # Kannada
	( 0Xcaa , 0Xcb3 , "Kannada" ), # Kannada
	( 0Xcb5 , 0Xcb9 , "Kannada" ), # Kannada
	( 0Xcbc , 0Xcc4 , "Kannada" ), # Kannada
	( 0Xcc6 , 0Xcc8 , "Kannada" ), # Kannada
	( 0Xcca , 0Xccd , "Kannada" ), # Kannada
	( 0Xcd5 , 0Xcd6 , "Kannada" ), # Kannada
	( 0Xcde , 0Xcde , "Kannada" ), # Kannada
	( 0Xce0 , 0Xce3 , "Kannada" ), # Kannada
	( 0Xce6 , 0Xcef , "Kannada" ), # Kannada
	( 0Xcf1 , 0Xcf2 , "Kannada" ), # Kannada
	( 0Xd01 , 0Xd03 , "Malayalam" ), # Malayalam
	( 0Xd05 , 0Xd0c , "Malayalam" ), # Malayalam
	( 0Xd0e , 0Xd10 , "Malayalam" ), # Malayalam
	( 0Xd12 , 0Xd3a , "Malayalam" ), # Malayalam
	( 0Xd3d , 0Xd44 , "Malayalam" ), # Malayalam
	( 0Xd46 , 0Xd48 , "Malayalam" ), # Malayalam
	( 0Xd4a , 0Xd4e , "Malayalam" ), # Malayalam
	( 0Xd57 , 0Xd57 , "Malayalam" ), # Malayalam
	( 0Xd5f , 0Xd63 , "Malayalam" ), # Malayalam
	( 0Xd66 , 0Xd75 , "Malayalam" ), # Malayalam
	( 0Xd79 , 0Xd7f , "Malayalam" ), # Malayalam
	( 0Xd82 , 0Xd83 , "Sinhala" ), # Sinhala
	( 0Xd85 , 0Xd96 , "Sinhala" ), # Sinhala
	( 0Xd9a , 0Xdb1 , "Sinhala" ), # Sinhala
	( 0Xdb3 , 0Xdbb , "Sinhala" ), # Sinhala
	( 0Xdbd , 0Xdbd , "Sinhala" ), # Sinhala
	( 0Xdc0 , 0Xdc6 , "Sinhala" ), # Sinhala
	( 0Xdca , 0Xdca , "Sinhala" ), # Sinhala
	( 0Xdcf , 0Xdd4 , "Sinhala" ), # Sinhala
	( 0Xdd6 , 0Xdd6 , "Sinhala" ), # Sinhala
	( 0Xdd8 , 0Xddf , "Sinhala" ), # Sinhala
	( 0Xde6 , 0Xdef , "Sinhala" ), # Sinhala
	( 0Xdf2 , 0Xdf4 , "Sinhala" ), # Sinhala
	( 0Xe01 , 0Xe3a , "Thai" ), # Thai
	( 0Xe3f , 0Xe3f , "Common" ), # Common
	( 0Xe40 , 0Xe5b , "Thai" ), # Thai
	( 0Xe81 , 0Xe82 , "Lao" ), # Lao
	( 0Xe84 , 0Xe84 , "Lao" ), # Lao
	( 0Xe87 , 0Xe88 , "Lao" ), # Lao
	( 0Xe8a , 0Xe8a , "Lao" ), # Lao
	( 0Xe8d , 0Xe8d , "Lao" ), # Lao
	( 0Xe94 , 0Xe97 , "Lao" ), # Lao
	( 0Xe99 , 0Xe9f , "Lao" ), # Lao
	( 0Xea1 , 0Xea3 , "Lao" ), # Lao
	( 0Xea5 , 0Xea5 , "Lao" ), # Lao
	( 0Xea7 , 0Xea7 , "Lao" ), # Lao
	( 0Xeaa , 0Xeab , "Lao" ), # Lao
	( 0Xead , 0Xeb9 , "Lao" ), # Lao
	( 0Xebb , 0Xebd , "Lao" ), # Lao
	( 0Xec0 , 0Xec4 , "Lao" ), # Lao
	( 0Xec6 , 0Xec6 , "Lao" ), # Lao
	( 0Xec8 , 0Xecd , "Lao" ), # Lao
	( 0Xed0 , 0Xed9 , "Lao" ), # Lao
	( 0Xedc , 0Xedf , "Lao" ), # Lao
	( 0Xf00 , 0Xf47 , "Tibetan" ), # Tibetan
	( 0Xf49 , 0Xf6c , "Tibetan" ), # Tibetan
	( 0Xf71 , 0Xf97 , "Tibetan" ), # Tibetan
	( 0Xf99 , 0Xfbc , "Tibetan" ), # Tibetan
	( 0Xfbe , 0Xfcc , "Tibetan" ), # Tibetan
	( 0Xfce , 0Xfd4 , "Tibetan" ), # Tibetan
	( 0Xfd5 , 0Xfd8 , "Common" ), # Common
	( 0Xfd9 , 0Xfda , "Tibetan" ), # Tibetan
	( 0X1000 , 0X109f , "Myanmar" ), # Myanmar
	( 0X10a0 , 0X10c5 , "Georgian" ), # Georgian
	( 0X10c7 , 0X10c7 , "Georgian" ), # Georgian
	( 0X10cd , 0X10cd , "Georgian" ), # Georgian
	( 0X10d0 , 0X10fa , "Georgian" ), # Georgian
	( 0X10fb , 0X10fb , "Common" ), # Common
	( 0X10fc , 0X10ff , "Georgian" ), # Georgian
	( 0X1100 , 0X11ff , "Hangul" ), # Hangul
	( 0X1200 , 0X1248 , "Ethiopic" ), # Ethiopic
	( 0X124a , 0X124d , "Ethiopic" ), # Ethiopic
	( 0X1250 , 0X1256 , "Ethiopic" ), # Ethiopic
	( 0X1258 , 0X1258 , "Ethiopic" ), # Ethiopic
	( 0X125a , 0X125d , "Ethiopic" ), # Ethiopic
	( 0X1260 , 0X1288 , "Ethiopic" ), # Ethiopic
	( 0X128a , 0X128d , "Ethiopic" ), # Ethiopic
	( 0X1290 , 0X12b0 , "Ethiopic" ), # Ethiopic
	( 0X12b2 , 0X12b5 , "Ethiopic" ), # Ethiopic
	( 0X12b8 , 0X12be , "Ethiopic" ), # Ethiopic
	( 0X12c0 , 0X12c0 , "Ethiopic" ), # Ethiopic
	( 0X12c2 , 0X12c5 , "Ethiopic" ), # Ethiopic
	( 0X12c8 , 0X12d6 , "Ethiopic" ), # Ethiopic
	( 0X12d8 , 0X1310 , "Ethiopic" ), # Ethiopic
	( 0X1312 , 0X1315 , "Ethiopic" ), # Ethiopic
	( 0X1318 , 0X135a , "Ethiopic" ), # Ethiopic
	( 0X135d , 0X137c , "Ethiopic" ), # Ethiopic
	( 0X1380 , 0X1399 , "Ethiopic" ), # Ethiopic
	( 0X13a0 , 0X13f5 , "Cherokee" ), # Cherokee
	( 0X13f8 , 0X13fd , "Cherokee" ), # Cherokee
	( 0X1400 , 0X167f , "Canadian_Aboriginal" ), # Canadian_Aboriginal
	( 0X1680 , 0X169c , "Ogham" ), # Ogham
	( 0X16a0 , 0X16ea , "Runic" ), # Runic
	( 0X16eb , 0X16ed , "Common" ), # Common
	( 0X16ee , 0X16f8 , "Runic" ), # Runic
	( 0X1700 , 0X170c , "Tagalog" ), # Tagalog
	( 0X170e , 0X1714 , "Tagalog" ), # Tagalog
	( 0X1720 , 0X1734 , "Hanunoo" ), # Hanunoo
	( 0X1735 , 0X1736 , "Common" ), # Common
	( 0X1740 , 0X1753 , "Buhid" ), # Buhid
	( 0X1760 , 0X176c , "Tagbanwa" ), # Tagbanwa
	( 0X176e , 0X1770 , "Tagbanwa" ), # Tagbanwa
	( 0X1772 , 0X1773 , "Tagbanwa" ), # Tagbanwa
	( 0X1780 , 0X17dd , "Khmer" ), # Khmer
	( 0X17e0 , 0X17e9 , "Khmer" ), # Khmer
	( 0X17f0 , 0X17f9 , "Khmer" ), # Khmer
	( 0X1800 , 0X1801 , "Mongolian" ), # Mongolian
	( 0X1802 , 0X1803 , "Common" ), # Common
	( 0X1804 , 0X1804 , "Mongolian" ), # Mongolian
	( 0X1805 , 0X1805 , "Common" ), # Common
	( 0X1806 , 0X180e , "Mongolian" ), # Mongolian
	( 0X1810 , 0X1819 , "Mongolian" ), # Mongolian
	( 0X1820 , 0X1877 , "Mongolian" ), # Mongolian
	( 0X1880 , 0X18aa , "Mongolian" ), # Mongolian
	( 0X18b0 , 0X18f5 , "Canadian_Aboriginal" ), # Canadian_Aboriginal
	( 0X1900 , 0X191e , "Limbu" ), # Limbu
	( 0X1920 , 0X192b , "Limbu" ), # Limbu
	( 0X1930 , 0X193b , "Limbu" ), # Limbu
	( 0X1940 , 0X1940 , "Limbu" ), # Limbu
	( 0X1944 , 0X194f , "Limbu" ), # Limbu
	( 0X1950 , 0X196d , "Tai_Le" ), # Tai_Le
	( 0X1970 , 0X1974 , "Tai_Le" ), # Tai_Le
	( 0X1980 , 0X19ab , "New_Tai_Lue" ), # New_Tai_Lue
	( 0X19b0 , 0X19c9 , "New_Tai_Lue" ), # New_Tai_Lue
	( 0X19d0 , 0X19da , "New_Tai_Lue" ), # New_Tai_Lue
	( 0X19de , 0X19df , "New_Tai_Lue" ), # New_Tai_Lue
	( 0X19e0 , 0X19ff , "Khmer" ), # Khmer
	( 0X1a00 , 0X1a1b , "Buginese" ), # Buginese
	( 0X1a1e , 0X1a1f , "Buginese" ), # Buginese
	( 0X1a20 , 0X1a5e , "Tai_Tham" ), # Tai_Tham
	( 0X1a60 , 0X1a7c , "Tai_Tham" ), # Tai_Tham
	( 0X1a7f , 0X1a89 , "Tai_Tham" ), # Tai_Tham
	( 0X1a90 , 0X1a99 , "Tai_Tham" ), # Tai_Tham
	( 0X1aa0 , 0X1aad , "Tai_Tham" ), # Tai_Tham
	( 0X1ab0 , 0X1abe , "Inherited" ), # Inherited
	( 0X1b00 , 0X1b4b , "Balinese" ), # Balinese
	( 0X1b50 , 0X1b7c , "Balinese" ), # Balinese
	( 0X1b80 , 0X1bbf , "Sundanese" ), # Sundanese
	( 0X1bc0 , 0X1bf3 , "Batak" ), # Batak
	( 0X1bfc , 0X1bff , "Batak" ), # Batak
	( 0X1c00 , 0X1c37 , "Lepcha" ), # Lepcha
	( 0X1c3b , 0X1c49 , "Lepcha" ), # Lepcha
	( 0X1c4d , 0X1c4f , "Lepcha" ), # Lepcha
	( 0X1c50 , 0X1c7f , "Ol_Chiki" ), # Ol_Chiki
	( 0X1cc0 , 0X1cc7 , "Sundanese" ), # Sundanese
	( 0X1cd0 , 0X1cd2 , "Inherited" ), # Inherited
	( 0X1cd3 , 0X1cd3 , "Common" ), # Common
	( 0X1cd4 , 0X1ce0 , "Inherited" ), # Inherited
	( 0X1ce1 , 0X1ce1 , "Common" ), # Common
	( 0X1ce2 , 0X1ce8 , "Inherited" ), # Inherited
	( 0X1ce9 , 0X1cec , "Common" ), # Common
	( 0X1ced , 0X1ced , "Inherited" ), # Inherited
	( 0X1cee , 0X1cf3 , "Common" ), # Common
	( 0X1cf4 , 0X1cf4 , "Inherited" ), # Inherited
	( 0X1cf5 , 0X1cf6 , "Common" ), # Common
	( 0X1cf8 , 0X1cf9 , "Inherited" ), # Inherited
	( 0X1d00 , 0X1d25 , "Latin" ), # Latin
	( 0X1d26 , 0X1d2a , "Greek" ), # Greek
	( 0X1d2b , 0X1d2b , "Cyrillic" ), # Cyrillic
	( 0X1d2c , 0X1d5c , "Latin" ), # Latin
	( 0X1d5d , 0X1d61 , "Greek" ), # Greek
	( 0X1d62 , 0X1d65 , "Latin" ), # Latin
	( 0X1d66 , 0X1d6a , "Greek" ), # Greek
	( 0X1d6b , 0X1d77 , "Latin" ), # Latin
	( 0X1d78 , 0X1d78 , "Cyrillic" ), # Cyrillic
	( 0X1d79 , 0X1dbe , "Latin" ), # Latin
	( 0X1dbf , 0X1dbf , "Greek" ), # Greek
	( 0X1dc0 , 0X1df5 , "Inherited" ), # Inherited
	( 0X1dfc , 0X1dff , "Inherited" ), # Inherited
	( 0X1e00 , 0X1eff , "Latin" ), # Latin
	( 0X1f00 , 0X1f15 , "Greek" ), # Greek
	( 0X1f18 , 0X1f1d , "Greek" ), # Greek
	( 0X1f20 , 0X1f45 , "Greek" ), # Greek
	( 0X1f48 , 0X1f4d , "Greek" ), # Greek
	( 0X1f50 , 0X1f57 , "Greek" ), # Greek
	( 0X1f59 , 0X1f59 , "Greek" ), # Greek
	( 0X1f5b , 0X1f5b , "Greek" ), # Greek
	( 0X1f5d , 0X1f5d , "Greek" ), # Greek
	( 0X1f5f , 0X1f7d , "Greek" ), # Greek
	( 0X1f80 , 0X1fb4 , "Greek" ), # Greek
	( 0X1fb6 , 0X1fc4 , "Greek" ), # Greek
	( 0X1fc6 , 0X1fd3 , "Greek" ), # Greek
	( 0X1fd6 , 0X1fdb , "Greek" ), # Greek
	( 0X1fdd , 0X1fef , "Greek" ), # Greek
	( 0X1ff2 , 0X1ff4 , "Greek" ), # Greek
	( 0X1ff6 , 0X1ffe , "Greek" ), # Greek
	( 0X2000 , 0X200b , "Common" ), # Common
	( 0X200c , 0X200d , "Inherited" ), # Inherited
	( 0X200e , 0X2064 , "Common" ), # Common
	( 0X2066 , 0X2070 , "Common" ), # Common
	( 0X2071 , 0X2071 , "Latin" ), # Latin
	( 0X2074 , 0X207e , "Common" ), # Common
	( 0X207f , 0X207f , "Latin" ), # Latin
	( 0X2080 , 0X208e , "Common" ), # Common
	( 0X2090 , 0X209c , "Latin" ), # Latin
	( 0X20a0 , 0X20be , "Common" ), # Common
	( 0X20d0 , 0X20f0 , "Inherited" ), # Inherited
	( 0X2100 , 0X2125 , "Common" ), # Common
	( 0X2126 , 0X2126 , "Greek" ), # Greek
	( 0X2127 , 0X2129 , "Common" ), # Common
	( 0X212a , 0X212b , "Latin" ), # Latin
	( 0X212c , 0X2131 , "Common" ), # Common
	( 0X2132 , 0X2132 , "Latin" ), # Latin
	( 0X2133 , 0X214d , "Common" ), # Common
	( 0X214e , 0X214e , "Latin" ), # Latin
	( 0X214f , 0X215f , "Common" ), # Common
	( 0X2160 , 0X2188 , "Latin" ), # Latin
	( 0X2189 , 0X218b , "Common" ), # Common
	( 0X2190 , 0X23fa , "Common" ), # Common
	( 0X2400 , 0X2426 , "Common" ), # Common
	( 0X2440 , 0X244a , "Common" ), # Common
	( 0X2460 , 0X27ff , "Common" ), # Common
	( 0X2800 , 0X28ff , "Braille" ), # Braille
	( 0X2900 , 0X2b73 , "Common" ), # Common
	( 0X2b76 , 0X2b95 , "Common" ), # Common
	( 0X2b98 , 0X2bb9 , "Common" ), # Common
	( 0X2bbd , 0X2bc8 , "Common" ), # Common
	( 0X2bca , 0X2bd1 , "Common" ), # Common
	( 0X2bec , 0X2bef , "Common" ), # Common
	( 0X2c00 , 0X2c2e , "Glagolitic" ), # Glagolitic
	( 0X2c30 , 0X2c5e , "Glagolitic" ), # Glagolitic
	( 0X2c60 , 0X2c7f , "Latin" ), # Latin
	( 0X2c80 , 0X2cf3 , "Coptic" ), # Coptic
	( 0X2cf9 , 0X2cff , "Coptic" ), # Coptic
	( 0X2d00 , 0X2d25 , "Georgian" ), # Georgian
	( 0X2d27 , 0X2d27 , "Georgian" ), # Georgian
	( 0X2d2d , 0X2d2d , "Georgian" ), # Georgian
	( 0X2d30 , 0X2d67 , "Tifinagh" ), # Tifinagh
	( 0X2d6f , 0X2d70 , "Tifinagh" ), # Tifinagh
	( 0X2d7f , 0X2d7f , "Tifinagh" ), # Tifinagh
	( 0X2d80 , 0X2d96 , "Ethiopic" ), # Ethiopic
	( 0X2da0 , 0X2da6 , "Ethiopic" ), # Ethiopic
	( 0X2da8 , 0X2dae , "Ethiopic" ), # Ethiopic
	( 0X2db0 , 0X2db6 , "Ethiopic" ), # Ethiopic
	( 0X2db8 , 0X2dbe , "Ethiopic" ), # Ethiopic
	( 0X2dc0 , 0X2dc6 , "Ethiopic" ), # Ethiopic
	( 0X2dc8 , 0X2dce , "Ethiopic" ), # Ethiopic
	( 0X2dd0 , 0X2dd6 , "Ethiopic" ), # Ethiopic
	( 0X2dd8 , 0X2dde , "Ethiopic" ), # Ethiopic
	( 0X2de0 , 0X2dff , "Cyrillic" ), # Cyrillic
	( 0X2e00 , 0X2e42 , "Common" ), # Common
	( 0X2e80 , 0X2e99 , "Han" ), # Han
	( 0X2e9b , 0X2ef3 , "Han" ), # Han
	( 0X2f00 , 0X2fd5 , "Han" ), # Han
	( 0X2ff0 , 0X2ffb , "Common" ), # Common
	( 0X3000 , 0X3004 , "Common" ), # Common
	( 0X3005 , 0X3005 , "Han" ), # Han
	( 0X3006 , 0X3006 , "Common" ), # Common
	( 0X3007 , 0X3007 , "Han" ), # Han
	( 0X3008 , 0X3020 , "Common" ), # Common
	( 0X3021 , 0X3029 , "Han" ), # Han
	( 0X302a , 0X302d , "Inherited" ), # Inherited
	( 0X302e , 0X302f , "Hangul" ), # Hangul
	( 0X3030 , 0X3037 , "Common" ), # Common
	( 0X3038 , 0X303b , "Han" ), # Han
	( 0X303c , 0X303f , "Common" ), # Common
	( 0X3041 , 0X3096 , "Hiragana" ), # Hiragana
	( 0X3099 , 0X309a , "Inherited" ), # Inherited
	( 0X309b , 0X309c , "Common" ), # Common
	( 0X309d , 0X309f , "Hiragana" ), # Hiragana
	( 0X30a0 , 0X30a0 , "Common" ), # Common
	( 0X30a1 , 0X30fa , "Katakana" ), # Katakana
	( 0X30fb , 0X30fc , "Common" ), # Common
	( 0X30fd , 0X30ff , "Katakana" ), # Katakana
	( 0X3105 , 0X312d , "Bopomofo" ), # Bopomofo
	( 0X3131 , 0X318e , "Hangul" ), # Hangul
	( 0X3190 , 0X319f , "Common" ), # Common
	( 0X31a0 , 0X31ba , "Bopomofo" ), # Bopomofo
	( 0X31c0 , 0X31e3 , "Common" ), # Common
	( 0X31f0 , 0X31ff , "Katakana" ), # Katakana
	( 0X3200 , 0X321e , "Hangul" ), # Hangul
	( 0X3220 , 0X325f , "Common" ), # Common
	( 0X3260 , 0X327e , "Hangul" ), # Hangul
	( 0X327f , 0X32cf , "Common" ), # Common
	( 0X32d0 , 0X32fe , "Katakana" ), # Katakana
	( 0X3300 , 0X3357 , "Katakana" ), # Katakana
	( 0X3358 , 0X33ff , "Common" ), # Common
	( 0X3400 , 0X4db5 , "Han" ), # Han
	( 0X4dc0 , 0X4dff , "Common" ), # Common
	( 0X4e00 , 0X9fd5 , "Han" ), # Han
	( 0Xa000 , 0Xa48c , "Yi" ), # Yi
	( 0Xa490 , 0Xa4c6 , "Yi" ), # Yi
	( 0Xa4d0 , 0Xa4ff , "Lisu" ), # Lisu
	( 0Xa500 , 0Xa62b , "Vai" ), # Vai
	( 0Xa640 , 0Xa69f , "Cyrillic" ), # Cyrillic
	( 0Xa6a0 , 0Xa6f7 , "Bamum" ), # Bamum
	( 0Xa700 , 0Xa721 , "Common" ), # Common
	( 0Xa722 , 0Xa787 , "Latin" ), # Latin
	( 0Xa788 , 0Xa78a , "Common" ), # Common
	( 0Xa78b , 0Xa7ad , "Latin" ), # Latin
	( 0Xa7b0 , 0Xa7b7 , "Latin" ), # Latin
	( 0Xa7f7 , 0Xa7ff , "Latin" ), # Latin
	( 0Xa800 , 0Xa82b , "Syloti_Nagri" ), # Syloti_Nagri
	( 0Xa830 , 0Xa839 , "Common" ), # Common
	( 0Xa840 , 0Xa877 , "Phags_Pa" ), # Phags_Pa
	( 0Xa880 , 0Xa8c4 , "Saurashtra" ), # Saurashtra
	( 0Xa8ce , 0Xa8d9 , "Saurashtra" ), # Saurashtra
	( 0Xa8e0 , 0Xa8fd , "Devanagari" ), # Devanagari
	( 0Xa900 , 0Xa92d , "Kayah_Li" ), # Kayah_Li
	( 0Xa92e , 0Xa92e , "Common" ), # Common
	( 0Xa92f , 0Xa92f , "Kayah_Li" ), # Kayah_Li
	( 0Xa930 , 0Xa953 , "Rejang" ), # Rejang
	( 0Xa95f , 0Xa95f , "Rejang" ), # Rejang
	( 0Xa960 , 0Xa97c , "Hangul" ), # Hangul
	( 0Xa980 , 0Xa9cd , "Javanese" ), # Javanese
	( 0Xa9cf , 0Xa9cf , "Common" ), # Common
	( 0Xa9d0 , 0Xa9d9 , "Javanese" ), # Javanese
	( 0Xa9de , 0Xa9df , "Javanese" ), # Javanese
	( 0Xa9e0 , 0Xa9fe , "Myanmar" ), # Myanmar
	( 0Xaa00 , 0Xaa36 , "Cham" ), # Cham
	( 0Xaa40 , 0Xaa4d , "Cham" ), # Cham
	( 0Xaa50 , 0Xaa59 , "Cham" ), # Cham
	( 0Xaa5c , 0Xaa5f , "Cham" ), # Cham
	( 0Xaa60 , 0Xaa7f , "Myanmar" ), # Myanmar
	( 0Xaa80 , 0Xaac2 , "Tai_Viet" ), # Tai_Viet
	( 0Xaadb , 0Xaadf , "Tai_Viet" ), # Tai_Viet
	( 0Xaae0 , 0Xaaf6 , "Meetei_Mayek" ), # Meetei_Mayek
	( 0Xab01 , 0Xab06 , "Ethiopic" ), # Ethiopic
	( 0Xab09 , 0Xab0e , "Ethiopic" ), # Ethiopic
	( 0Xab11 , 0Xab16 , "Ethiopic" ), # Ethiopic
	( 0Xab20 , 0Xab26 , "Ethiopic" ), # Ethiopic
	( 0Xab28 , 0Xab2e , "Ethiopic" ), # Ethiopic
	( 0Xab30 , 0Xab5a , "Latin" ), # Latin
	( 0Xab5b , 0Xab5b , "Common" ), # Common
	( 0Xab5c , 0Xab64 , "Latin" ), # Latin
	( 0Xab65 , 0Xab65 , "Greek" ), # Greek
	( 0Xab70 , 0Xabbf , "Cherokee" ), # Cherokee
	( 0Xabc0 , 0Xabed , "Meetei_Mayek" ), # Meetei_Mayek
	( 0Xabf0 , 0Xabf9 , "Meetei_Mayek" ), # Meetei_Mayek
	( 0Xac00 , 0Xd7a3 , "Hangul" ), # Hangul
	( 0Xd7b0 , 0Xd7c6 , "Hangul" ), # Hangul
	( 0Xd7cb , 0Xd7fb , "Hangul" ), # Hangul
	( 0Xf900 , 0Xfa6d , "Han" ), # Han
	( 0Xfa70 , 0Xfad9 , "Han" ), # Han
	( 0Xfb00 , 0Xfb06 , "Latin" ), # Latin
	( 0Xfb13 , 0Xfb17 , "Armenian" ), # Armenian
	( 0Xfb1d , 0Xfb36 , "Hebrew" ), # Hebrew
	( 0Xfb38 , 0Xfb3c , "Hebrew" ), # Hebrew
	( 0Xfb3e , 0Xfb3e , "Hebrew" ), # Hebrew
	( 0Xfb40 , 0Xfb41 , "Hebrew" ), # Hebrew
	( 0Xfb43 , 0Xfb44 , "Hebrew" ), # Hebrew
	( 0Xfb46 , 0Xfb4f , "Hebrew" ), # Hebrew
	( 0Xfb50 , 0Xfbc1 , "Arabic" ), # Arabic
	( 0Xfbd3 , 0Xfd3d , "Arabic" ), # Arabic
	( 0Xfd3e , 0Xfd3f , "Common" ), # Common
	( 0Xfd50 , 0Xfd8f , "Arabic" ), # Arabic
	( 0Xfd92 , 0Xfdc7 , "Arabic" ), # Arabic
	( 0Xfdf0 , 0Xfdfd , "Arabic" ), # Arabic
	( 0Xfe00 , 0Xfe0f , "Inherited" ), # Inherited
	( 0Xfe10 , 0Xfe19 , "Common" ), # Common
	( 0Xfe20 , 0Xfe2d , "Inherited" ), # Inherited
	( 0Xfe2e , 0Xfe2f , "Cyrillic" ), # Cyrillic
	( 0Xfe30 , 0Xfe52 , "Common" ), # Common
	( 0Xfe54 , 0Xfe66 , "Common" ), # Common
	( 0Xfe68 , 0Xfe6b , "Common" ), # Common
	( 0Xfe70 , 0Xfe74 , "Arabic" ), # Arabic
	( 0Xfe76 , 0Xfefc , "Arabic" ), # Arabic
	( 0Xfeff , 0Xfeff , "Common" ), # Common
	( 0Xff01 , 0Xff20 , "Common" ), # Common
	( 0Xff21 , 0Xff3a , "Latin" ), # Latin
	( 0Xff3b , 0Xff40 , "Common" ), # Common
	( 0Xff41 , 0Xff5a , "Latin" ), # Latin
	( 0Xff5b , 0Xff65 , "Common" ), # Common
	( 0Xff66 , 0Xff6f , "Katakana" ), # Katakana
	( 0Xff70 , 0Xff70 , "Common" ), # Common
	( 0Xff71 , 0Xff9d , "Katakana" ), # Katakana
	( 0Xff9e , 0Xff9f , "Common" ), # Common
	( 0Xffa0 , 0Xffbe , "Hangul" ), # Hangul
	( 0Xffc2 , 0Xffc7 , "Hangul" ), # Hangul
	( 0Xffca , 0Xffcf , "Hangul" ), # Hangul
	( 0Xffd2 , 0Xffd7 , "Hangul" ), # Hangul
	( 0Xffda , 0Xffdc , "Hangul" ), # Hangul
	( 0Xffe0 , 0Xffe6 , "Common" ), # Common
	( 0Xffe8 , 0Xffee , "Common" ), # Common
	( 0Xfff9 , 0Xfffd , "Common" ), # Common
	( 0X10000 , 0X1000b , "Linear_B" ), # Linear_B
	( 0X1000d , 0X10026 , "Linear_B" ), # Linear_B
	( 0X10028 , 0X1003a , "Linear_B" ), # Linear_B
	( 0X1003c , 0X1003d , "Linear_B" ), # Linear_B
	( 0X1003f , 0X1004d , "Linear_B" ), # Linear_B
	( 0X10050 , 0X1005d , "Linear_B" ), # Linear_B
	( 0X10080 , 0X100fa , "Linear_B" ), # Linear_B
	( 0X10100 , 0X10102 , "Common" ), # Common
	( 0X10107 , 0X10133 , "Common" ), # Common
	( 0X10137 , 0X1013f , "Common" ), # Common
	( 0X10140 , 0X1018c , "Greek" ), # Greek
	( 0X10190 , 0X1019b , "Common" ), # Common
	( 0X101a0 , 0X101a0 , "Greek" ), # Greek
	( 0X101d0 , 0X101fc , "Common" ), # Common
	( 0X101fd , 0X101fd , "Inherited" ), # Inherited
	( 0X10280 , 0X1029c , "Lycian" ), # Lycian
	( 0X102a0 , 0X102d0 , "Carian" ), # Carian
	( 0X102e0 , 0X102e0 , "Inherited" ), # Inherited
	( 0X102e1 , 0X102fb , "Common" ), # Common
	( 0X10300 , 0X10323 , "Old_Italic" ), # Old_Italic
	( 0X10330 , 0X1034a , "Gothic" ), # Gothic
	( 0X10350 , 0X1037a , "Old_Permic" ), # Old_Permic
	( 0X10380 , 0X1039d , "Ugaritic" ), # Ugaritic
	( 0X1039f , 0X1039f , "Ugaritic" ), # Ugaritic
	( 0X103a0 , 0X103c3 , "Old_Persian" ), # Old_Persian
	( 0X103c8 , 0X103d5 , "Old_Persian" ), # Old_Persian
	( 0X10400 , 0X1044f , "Deseret" ), # Deseret
	( 0X10450 , 0X1047f , "Shavian" ), # Shavian
	( 0X10480 , 0X1049d , "Osmanya" ), # Osmanya
	( 0X104a0 , 0X104a9 , "Osmanya" ), # Osmanya
	( 0X10500 , 0X10527 , "Elbasan" ), # Elbasan
	( 0X10530 , 0X10563 , "Caucasian_Albanian" ), # Caucasian_Albanian
	( 0X1056f , 0X1056f , "Caucasian_Albanian" ), # Caucasian_Albanian
	( 0X10600 , 0X10736 , "Linear_A" ), # Linear_A
	( 0X10740 , 0X10755 , "Linear_A" ), # Linear_A
	( 0X10760 , 0X10767 , "Linear_A" ), # Linear_A
	( 0X10800 , 0X10805 , "Cypriot" ), # Cypriot
	( 0X10808 , 0X10808 , "Cypriot" ), # Cypriot
	( 0X1080a , 0X10835 , "Cypriot" ), # Cypriot
	( 0X10837 , 0X10838 , "Cypriot" ), # Cypriot
	( 0X1083c , 0X1083c , "Cypriot" ), # Cypriot
	( 0X1083f , 0X1083f , "Cypriot" ), # Cypriot
	( 0X10840 , 0X10855 , "Imperial_Aramaic" ), # Imperial_Aramaic
	( 0X10857 , 0X1085f , "Imperial_Aramaic" ), # Imperial_Aramaic
	( 0X10860 , 0X1087f , "Palmyrene" ), # Palmyrene
	( 0X10880 , 0X1089e , "Nabataean" ), # Nabataean
	( 0X108a7 , 0X108af , "Nabataean" ), # Nabataean
	( 0X108e0 , 0X108f2 , "Hatran" ), # Hatran
	( 0X108f4 , 0X108f5 , "Hatran" ), # Hatran
	( 0X108fb , 0X108ff , "Hatran" ), # Hatran
	( 0X10900 , 0X1091b , "Phoenician" ), # Phoenician
	( 0X1091f , 0X1091f , "Phoenician" ), # Phoenician
	( 0X10920 , 0X10939 , "Lydian" ), # Lydian
	( 0X1093f , 0X1093f , "Lydian" ), # Lydian
	( 0X10980 , 0X1099f , "Meroitic_Hieroglyphs" ), # Meroitic_Hieroglyphs
	( 0X109a0 , 0X109b7 , "Meroitic_Cursive" ), # Meroitic_Cursive
	( 0X109bc , 0X109cf , "Meroitic_Cursive" ), # Meroitic_Cursive
	( 0X109d2 , 0X109ff , "Meroitic_Cursive" ), # Meroitic_Cursive
	( 0X10a00 , 0X10a03 , "Kharoshthi" ), # Kharoshthi
	( 0X10a05 , 0X10a06 , "Kharoshthi" ), # Kharoshthi
	( 0X10a0c , 0X10a13 , "Kharoshthi" ), # Kharoshthi
	( 0X10a15 , 0X10a17 , "Kharoshthi" ), # Kharoshthi
	( 0X10a19 , 0X10a33 , "Kharoshthi" ), # Kharoshthi
	( 0X10a38 , 0X10a3a , "Kharoshthi" ), # Kharoshthi
	( 0X10a3f , 0X10a47 , "Kharoshthi" ), # Kharoshthi
	( 0X10a50 , 0X10a58 , "Kharoshthi" ), # Kharoshthi
	( 0X10a60 , 0X10a7f , "Old_South_Arabian" ), # Old_South_Arabian
	( 0X10a80 , 0X10a9f , "Old_North_Arabian" ), # Old_North_Arabian
	( 0X10ac0 , 0X10ae6 , "Manichaean" ), # Manichaean
	( 0X10aeb , 0X10af6 , "Manichaean" ), # Manichaean
	( 0X10b00 , 0X10b35 , "Avestan" ), # Avestan
	( 0X10b39 , 0X10b3f , "Avestan" ), # Avestan
	( 0X10b40 , 0X10b55 , "Inscriptional_Parthian" ), # Inscriptional_Parthian
	( 0X10b58 , 0X10b5f , "Inscriptional_Parthian" ), # Inscriptional_Parthian
	( 0X10b60 , 0X10b72 , "Inscriptional_Pahlavi" ), # Inscriptional_Pahlavi
	( 0X10b78 , 0X10b7f , "Inscriptional_Pahlavi" ), # Inscriptional_Pahlavi
	( 0X10b80 , 0X10b91 , "Psalter_Pahlavi" ), # Psalter_Pahlavi
	( 0X10b99 , 0X10b9c , "Psalter_Pahlavi" ), # Psalter_Pahlavi
	( 0X10ba9 , 0X10baf , "Psalter_Pahlavi" ), # Psalter_Pahlavi
	( 0X10c00 , 0X10c48 , "Old_Turkic" ), # Old_Turkic
	( 0X10c80 , 0X10cb2 , "Old_Hungarian" ), # Old_Hungarian
	( 0X10cc0 , 0X10cf2 , "Old_Hungarian" ), # Old_Hungarian
	( 0X10cfa , 0X10cff , "Old_Hungarian" ), # Old_Hungarian
	( 0X10e60 , 0X10e7e , "Arabic" ), # Arabic
	( 0X11000 , 0X1104d , "Brahmi" ), # Brahmi
	( 0X11052 , 0X1106f , "Brahmi" ), # Brahmi
	( 0X1107f , 0X1107f , "Brahmi" ), # Brahmi
	( 0X11080 , 0X110c1 , "Kaithi" ), # Kaithi
	( 0X110d0 , 0X110e8 , "Sora_Sompeng" ), # Sora_Sompeng
	( 0X110f0 , 0X110f9 , "Sora_Sompeng" ), # Sora_Sompeng
	( 0X11100 , 0X11134 , "Chakma" ), # Chakma
	( 0X11136 , 0X11143 , "Chakma" ), # Chakma
	( 0X11150 , 0X11176 , "Mahajani" ), # Mahajani
	( 0X11180 , 0X111cd , "Sharada" ), # Sharada
	( 0X111d0 , 0X111df , "Sharada" ), # Sharada
	( 0X111e1 , 0X111f4 , "Sinhala" ), # Sinhala
	( 0X11200 , 0X11211 , "Khojki" ), # Khojki
	( 0X11213 , 0X1123d , "Khojki" ), # Khojki
	( 0X11280 , 0X11286 , "Multani" ), # Multani
	( 0X11288 , 0X11288 , "Multani" ), # Multani
	( 0X1128a , 0X1128d , "Multani" ), # Multani
	( 0X1128f , 0X1129d , "Multani" ), # Multani
	( 0X1129f , 0X112a9 , "Multani" ), # Multani
	( 0X112b0 , 0X112ea , "Khudawadi" ), # Khudawadi
	( 0X112f0 , 0X112f9 , "Khudawadi" ), # Khudawadi
	( 0X11300 , 0X11303 , "Grantha" ), # Grantha
	( 0X11305 , 0X1130c , "Grantha" ), # Grantha
	( 0X1130f , 0X11310 , "Grantha" ), # Grantha
	( 0X11313 , 0X11328 , "Grantha" ), # Grantha
	( 0X1132a , 0X11330 , "Grantha" ), # Grantha
	( 0X11332 , 0X11333 , "Grantha" ), # Grantha
	( 0X11335 , 0X11339 , "Grantha" ), # Grantha
	( 0X1133c , 0X11344 , "Grantha" ), # Grantha
	( 0X11347 , 0X11348 , "Grantha" ), # Grantha
	( 0X1134b , 0X1134d , "Grantha" ), # Grantha
	( 0X11350 , 0X11350 , "Grantha" ), # Grantha
	( 0X11357 , 0X11357 , "Grantha" ), # Grantha
	( 0X1135d , 0X11363 , "Grantha" ), # Grantha
	( 0X11366 , 0X1136c , "Grantha" ), # Grantha
	( 0X11370 , 0X11374 , "Grantha" ), # Grantha
	( 0X11480 , 0X114c7 , "Tirhuta" ), # Tirhuta
	( 0X114d0 , 0X114d9 , "Tirhuta" ), # Tirhuta
	( 0X11580 , 0X115b5 , "Siddham" ), # Siddham
	( 0X115b8 , 0X115dd , "Siddham" ), # Siddham
	( 0X11600 , 0X11644 , "Modi" ), # Modi
	( 0X11650 , 0X11659 , "Modi" ), # Modi
	( 0X11680 , 0X116b7 , "Takri" ), # Takri
	( 0X116c0 , 0X116c9 , "Takri" ), # Takri
	( 0X11700 , 0X11719 , "Ahom" ), # Ahom
	( 0X1171d , 0X1172b , "Ahom" ), # Ahom
	( 0X11730 , 0X1173f , "Ahom" ), # Ahom
	( 0X118a0 , 0X118f2 , "Warang_Citi" ), # Warang_Citi
	( 0X118ff , 0X118ff , "Warang_Citi" ), # Warang_Citi
	( 0X11ac0 , 0X11af8 , "Pau_Cin_Hau" ), # Pau_Cin_Hau
	( 0X12000 , 0X12399 , "Cuneiform" ), # Cuneiform
	( 0X12400 , 0X1246e , "Cuneiform" ), # Cuneiform
	( 0X12470 , 0X12474 , "Cuneiform" ), # Cuneiform
	( 0X12480 , 0X12543 , "Cuneiform" ), # Cuneiform
	( 0X13000 , 0X1342e , "Egyptian_Hieroglyphs" ), # Egyptian_Hieroglyphs
	( 0X14400 , 0X14646 , "Anatolian_Hieroglyphs" ), # Anatolian_Hieroglyphs
	( 0X16800 , 0X16a38 , "Bamum" ), # Bamum
	( 0X16a40 , 0X16a5e , "Mro" ), # Mro
	( 0X16a60 , 0X16a69 , "Mro" ), # Mro
	( 0X16a6e , 0X16a6f , "Mro" ), # Mro
	( 0X16ad0 , 0X16aed , "Bassa_Vah" ), # Bassa_Vah
	( 0X16af0 , 0X16af5 , "Bassa_Vah" ), # Bassa_Vah
	( 0X16b00 , 0X16b45 , "Pahawh_Hmong" ), # Pahawh_Hmong
	( 0X16b50 , 0X16b59 , "Pahawh_Hmong" ), # Pahawh_Hmong
	( 0X16b5b , 0X16b61 , "Pahawh_Hmong" ), # Pahawh_Hmong
	( 0X16b63 , 0X16b77 , "Pahawh_Hmong" ), # Pahawh_Hmong
	( 0X16b7d , 0X16b8f , "Pahawh_Hmong" ), # Pahawh_Hmong
	( 0X16f00 , 0X16f44 , "Miao" ), # Miao
	( 0X16f50 , 0X16f7e , "Miao" ), # Miao
	( 0X16f8f , 0X16f9f , "Miao" ), # Miao
	( 0X1b000 , 0X1b000 , "Katakana" ), # Katakana
	( 0X1b001 , 0X1b001 , "Hiragana" ), # Hiragana
	( 0X1bc00 , 0X1bc6a , "Duployan" ), # Duployan
	( 0X1bc70 , 0X1bc7c , "Duployan" ), # Duployan
	( 0X1bc80 , 0X1bc88 , "Duployan" ), # Duployan
	( 0X1bc90 , 0X1bc99 , "Duployan" ), # Duployan
	( 0X1bc9c , 0X1bc9f , "Duployan" ), # Duployan
	( 0X1bca0 , 0X1bca3 , "Common" ), # Common
	( 0X1d000 , 0X1d0f5 , "Common" ), # Common
	( 0X1d100 , 0X1d126 , "Common" ), # Common
	( 0X1d129 , 0X1d166 , "Common" ), # Common
	( 0X1d167 , 0X1d169 , "Inherited" ), # Inherited
	( 0X1d16a , 0X1d17a , "Common" ), # Common
	( 0X1d17b , 0X1d182 , "Inherited" ), # Inherited
	( 0X1d183 , 0X1d184 , "Common" ), # Common
	( 0X1d185 , 0X1d18b , "Inherited" ), # Inherited
	( 0X1d18c , 0X1d1a9 , "Common" ), # Common
	( 0X1d1aa , 0X1d1ad , "Inherited" ), # Inherited
	( 0X1d1ae , 0X1d1e8 , "Common" ), # Common
	( 0X1d200 , 0X1d245 , "Greek" ), # Greek
	( 0X1d300 , 0X1d356 , "Common" ), # Common
	( 0X1d360 , 0X1d371 , "Common" ), # Common
	( 0X1d400 , 0X1d454 , "Common" ), # Common
	( 0X1d456 , 0X1d49c , "Common" ), # Common
	( 0X1d49e , 0X1d49f , "Common" ), # Common
	( 0X1d4a2 , 0X1d4a2 , "Common" ), # Common
	( 0X1d4a5 , 0X1d4a6 , "Common" ), # Common
	( 0X1d4a9 , 0X1d4ac , "Common" ), # Common
	( 0X1d4ae , 0X1d4b9 , "Common" ), # Common
	( 0X1d4bb , 0X1d4bb , "Common" ), # Common
	( 0X1d4bd , 0X1d4c3 , "Common" ), # Common
	( 0X1d4c5 , 0X1d505 , "Common" ), # Common
	( 0X1d507 , 0X1d50a , "Common" ), # Common
	( 0X1d50d , 0X1d514 , "Common" ), # Common
	( 0X1d516 , 0X1d51c , "Common" ), # Common
	( 0X1d51e , 0X1d539 , "Common" ), # Common
	( 0X1d53b , 0X1d53e , "Common" ), # Common
	( 0X1d540 , 0X1d544 , "Common" ), # Common
	( 0X1d546 , 0X1d546 , "Common" ), # Common
	( 0X1d54a , 0X1d550 , "Common" ), # Common
	( 0X1d552 , 0X1d6a5 , "Common" ), # Common
	( 0X1d6a8 , 0X1d7cb , "Common" ), # Common
	( 0X1d7ce , 0X1d7ff , "Common" ), # Common
	( 0X1d800 , 0X1da8b , "SignWriting" ), # SignWriting
	( 0X1da9b , 0X1da9f , "SignWriting" ), # SignWriting
	( 0X1daa1 , 0X1daaf , "SignWriting" ), # SignWriting
	( 0X1e800 , 0X1e8c4 , "Mende_Kikakui" ), # Mende_Kikakui
	( 0X1e8c7 , 0X1e8d6 , "Mende_Kikakui" ), # Mende_Kikakui
	( 0X1ee00 , 0X1ee03 , "Arabic" ), # Arabic
	( 0X1ee05 , 0X1ee1f , "Arabic" ), # Arabic
	( 0X1ee21 , 0X1ee22 , "Arabic" ), # Arabic
	( 0X1ee24 , 0X1ee24 , "Arabic" ), # Arabic
	( 0X1ee27 , 0X1ee27 , "Arabic" ), # Arabic
	( 0X1ee29 , 0X1ee32 , "Arabic" ), # Arabic
	( 0X1ee34 , 0X1ee37 , "Arabic" ), # Arabic
	( 0X1ee39 , 0X1ee39 , "Arabic" ), # Arabic
	( 0X1ee3b , 0X1ee3b , "Arabic" ), # Arabic
	( 0X1ee42 , 0X1ee42 , "Arabic" ), # Arabic
	( 0X1ee47 , 0X1ee47 , "Arabic" ), # Arabic
	( 0X1ee49 , 0X1ee49 , "Arabic" ), # Arabic
	( 0X1ee4b , 0X1ee4b , "Arabic" ), # Arabic
	( 0X1ee4d , 0X1ee4f , "Arabic" ), # Arabic
	( 0X1ee51 , 0X1ee52 , "Arabic" ), # Arabic
	( 0X1ee54 , 0X1ee54 , "Arabic" ), # Arabic
	( 0X1ee57 , 0X1ee57 , "Arabic" ), # Arabic
	( 0X1ee59 , 0X1ee59 , "Arabic" ), # Arabic
	( 0X1ee5b , 0X1ee5b , "Arabic" ), # Arabic
	( 0X1ee5d , 0X1ee5d , "Arabic" ), # Arabic
	( 0X1ee5f , 0X1ee5f , "Arabic" ), # Arabic
	( 0X1ee61 , 0X1ee62 , "Arabic" ), # Arabic
	( 0X1ee64 , 0X1ee64 , "Arabic" ), # Arabic
	( 0X1ee67 , 0X1ee6a , "Arabic" ), # Arabic
	( 0X1ee6c , 0X1ee72 , "Arabic" ), # Arabic
	( 0X1ee74 , 0X1ee77 , "Arabic" ), # Arabic
	( 0X1ee79 , 0X1ee7c , "Arabic" ), # Arabic
	( 0X1ee7e , 0X1ee7e , "Arabic" ), # Arabic
	( 0X1ee80 , 0X1ee89 , "Arabic" ), # Arabic
	( 0X1ee8b , 0X1ee9b , "Arabic" ), # Arabic
	( 0X1eea1 , 0X1eea3 , "Arabic" ), # Arabic
	( 0X1eea5 , 0X1eea9 , "Arabic" ), # Arabic
	( 0X1eeab , 0X1eebb , "Arabic" ), # Arabic
	( 0X1eef0 , 0X1eef1 , "Arabic" ), # Arabic
	( 0X1f000 , 0X1f02b , "Common" ), # Common
	( 0X1f030 , 0X1f093 , "Common" ), # Common
	( 0X1f0a0 , 0X1f0ae , "Common" ), # Common
	( 0X1f0b1 , 0X1f0bf , "Common" ), # Common
	( 0X1f0c1 , 0X1f0cf , "Common" ), # Common
	( 0X1f0d1 , 0X1f0f5 , "Common" ), # Common
	( 0X1f100 , 0X1f10c , "Common" ), # Common
	( 0X1f110 , 0X1f12e , "Common" ), # Common
	( 0X1f130 , 0X1f16b , "Common" ), # Common
	( 0X1f170 , 0X1f19a , "Common" ), # Common
	( 0X1f1e6 , 0X1f1ff , "Common" ), # Common
	( 0X1f200 , 0X1f200 , "Hiragana" ), # Hiragana
	( 0X1f201 , 0X1f202 , "Common" ), # Common
	( 0X1f210 , 0X1f23a , "Common" ), # Common
	( 0X1f240 , 0X1f248 , "Common" ), # Common
	( 0X1f250 , 0X1f251 , "Common" ), # Common
	( 0X1f300 , 0X1f579 , "Common" ), # Common
	( 0X1f57b , 0X1f5a3 , "Common" ), # Common
	( 0X1f5a5 , 0X1f6d0 , "Common" ), # Common
	( 0X1f6e0 , 0X1f6ec , "Common" ), # Common
	( 0X1f6f0 , 0X1f6f3 , "Common" ), # Common
	( 0X1f700 , 0X1f773 , "Common" ), # Common
	( 0X1f780 , 0X1f7d4 , "Common" ), # Common
	( 0X1f800 , 0X1f80b , "Common" ), # Common
	( 0X1f810 , 0X1f847 , "Common" ), # Common
	( 0X1f850 , 0X1f859 , "Common" ), # Common
	( 0X1f860 , 0X1f887 , "Common" ), # Common
	( 0X1f890 , 0X1f8ad , "Common" ), # Common
	( 0X1f910 , 0X1f918 , "Common" ), # Common
	( 0X1f980 , 0X1f984 , "Common" ), # Common
	( 0X1f9c0 , 0X1f9c0 , "Common" ), # Common
	( 0X20000 , 0X2a6d6 , "Han" ), # Han
	( 0X2a700 , 0X2b734 , "Han" ), # Han
	( 0X2b740 , 0X2b81d , "Han" ), # Han
	( 0X2b820 , 0X2cea1 , "Han" ), # Han
	( 0X2f800 , 0X2fa1d , "Han" ), # Han
	( 0Xe0001 , 0Xe0001 , "Common" ), # Common
	( 0Xe0020 , 0Xe007f , "Common" ), # Common
]
