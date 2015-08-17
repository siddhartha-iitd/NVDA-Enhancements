
import profile
import speech
from speech import ScriptChangeCommand
from speech import LangChangeCommand
import languageHandler
import config
from logHandler import log

# maintains list of priority languages 
languagePriorityListSpec = []

#reverse of unicodeScriptNamesToISO15924Dictionary, required to obtain unicode script names from numeric script codes 
ISO15924ToUnicodeScriptNamesDictionary = {}

#reverse of langIDToScriptID, required to obtain language id for a specific script 
scriptIDToLangID = {}

def initialize():
	# initializing reverse dictionary ISO15924ToUnicodeScriptNamesDictionary
	for scriptName in unicodeScriptNamesToISO15924Dictionary.keys():
		ISO15924ToUnicodeScriptNamesDictionary.setdefault( unicodeScriptNamesToISO15924Dictionary[scriptName] , scriptName )
	for languageID in langIDToScriptID.keys():
		scriptIDToLangID.setdefault( langIDToScriptID[languageID] , languageID )
	updateLanguagePriorityFromConfig()

def updateLanguagePriorityFromConfig():
	"""read string from config and convert it to list"""
	global languagePriorityListSpec 
	tempList = []
	languageList = config.conf["writingScriptsToLanguage"]["languagePriorityList"].split(",")
	for language in languageList: 
		tempList.append( [ language , getScriptName(language) , getLanguageDescription( language ) ]) 
	languagePriorityListSpec = tempList 

unicodeScriptNamesToISO15924Dictionary = {
	"Caucasian_Albanian":239, 
	"Arabic":160,
	"Imperial_Aramaic":124, 
	"Armenian":230,
	"Avestan":134,
	"Balinese":360,
	"Bamum":435,
	"Bassa_Vah":259,
	"Batak":365,
	"Bengali":325,
	"Bopomofo":285,
	"Brahmi":300,
	"Braille":570,
	"Buginese":367,
	"Buhid":372,
	"Chakma":349,
	"Canadian_Aboriginal":440,
	"Carian":201,
	"Cham":358,
	"Cherokee":445,
	"Coptic":204,
	"Cypriot":403,
	"Cyrillic":220,
	"Devanagari":315,
	"Deseret":250,
	"Duployan":755,
	"Egyptian_Hieroglyphs":50,
	"Elbasan":226,
	"Ethiopic":430,
	"Georgian":240,
	"Glagolitic":225,
	"Gothic":206,
	"Grantha":343,
	"Greek":200,
	"Gujarati":320,
	"Gurmukhi":310,
	"Hangul":286,
	"Han":500,
	"Hanunoo":371,
	"Hebrew":125,
	"Hiragana":410,
	"Pahawh_Hmong":450,
	"Old_Italic":210,
	"Javanese":361,
	"Kayah_Li":357,
	"Katakana":411,
	"Kharoshthi":305,
	"Khmer":355,
	"Khojki":322,
	"Kannada":345,
	"Kaithi":317,
	"Lao":356,
	"Latin":215,
	"Lepcha":335,
	"Limbu":336,
	"Linear_A":400,
	"Linear_B":401,
	"Lisu":399,
	"Lycian":202,
	"Lydian":116,
	"Mahajani":314,
	"Mandaic":140,
	"Manichaean":139,
	"Mende_Kikakui":438,
	"Meroitic_Cursive":101,
	"Meroitic_Hieroglyphs":100,
	"Malayalam":347,
	"Modi":324,
	"Mongolian":145,
	"Mro":199,
	"Meetei_Mayek":337,
	"Multani":323,
	"Myanmar":350,
	"Old_North_Arabian":106,
	"Nabataean":159,
	"Nko":165,
	"Ogham":212,
	"Ol_Chiki":261,
	"Old_Turkic":175,
	"Oriya":327,
	"Osage":219,
	"Osmanya":260,
	"Palmyrene":126,
	"Pau_Cin_Hau":263,
	"Old_Permic":227,
	"Phags_Pa":331,
	"Inscriptional_Pahlavi":131,
	"Psalter_Pahlavi":132,
	"Book_Pahlavi":133,
	"Phoenician":115,
	"Miao":282,
	"Inscriptional_Parthian":130,
	"Rejang":363,
	"Rongorongo":620,
	"Runic":211,
	"Samaritan":123,
	"Sarati":292,
	"Old_South_Arabian":105,
	"Saurashtra":344,
	"Shavian":281,
	"Sharada":319,
	"Siddham":302,
	"Khudawadi":318,
	"Sinhala":348,
	"Sora_Sompeng":398,
	"Sundanese":362,
	"Syloti_Nagri":316,
	"Syriac":135,
	"Tagbanwa":373,
	"Takri":321,
	"Tai_Le":353,
	"New_Tai_Lue":354,
	"Tamil":346,
	"Tangut":520,
	"Tai_Viet":359,
	"Telugu":340,
	"Tengwar":290,
	"Tifinagh":120,
	"Tagalog":370,
	"Thaana":170,
	"Thai":352,
	"Tibetan":330,
	"Tirhuta":326,
	"Ugaritic":40,
	"Vai":470,
	"Warang_Citi":262,
	"Woleai":480,
	"Old_Persian":30,
	"Cuneiform":20,
	"Yi":460,
	"Inherited":994,
	"Symbols":996,
	"Common":998,
	"Unknown":999,
}

langIDToScriptID= {
	'af_ZA':215, # south african
	'am':230, # Armenian 
	'ar':160, # Arabic 
	'as':325 , # Assamese 
	'bg':220, # Bulgarian 
	'bn':325, # Bangla 
	'ca':215, # Catalan 
	'cs':215, # Czech 
	'da':215, # Danish 
	'de':215, # German 
	'el':215, # Greek 
	'fr':215, # french
	'en':215, # english
	'es':215, # spanish
	'gu':320, # Gujarati 
	'hi':315, # Hindi (hi)
	'kn':345, # kanada
	'ml':347, # Malayalam 
	'mn':145, # mongolian
	'mr':315, # Marathi (mr),
	'ne':315, # Nepali (ne),
	'or':327, # Oriya
	'pa':310, # Punjabi
	'sa':315, # Sanskrit (sa)
	'sq':239, # Albanian 
	'ta':346, # Tamil
	'te':340, # Telugu 
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
	return 0

def getLangID(scriptCode):
	scriptName = ISO15924ToUnicodeScriptNamesDictionary[ scriptCode ] 
	for index in xrange( len( languagePriorityListSpec) ) :
		if scriptName == languagePriorityListSpec[index][1]: 
			return languagePriorityListSpec[index][0] 
	#language not found in the priority list, so look up in the default mapping
	langID = scriptIDToLangID.get (scriptCode )
	if langID:
		if isinstance( langID , tuple) and len(langID) > 0:
			return langID[0]
		else:
			return langID

def getLanguageDescription(language ):
	desc=languageHandler.getLanguageDescription(language )
	label="%s, %s"%(desc,language ) if desc else language 
	return label

def getScriptIDFromLangID(langID ):
	scriptID = langIDToScriptID.get (langID )
	if scriptID: 
		if isinstance( scriptID , tuple) and len(langID) > 0:
			return scriptID [0]
		else:
			return scriptID 


def getScriptName(languageID ):
	scriptID = getScriptIDFromLangID( languageID )
	if scriptID:
		return ISO15924ToUnicodeScriptNamesDictionary[ scriptID ]  

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
		if currentScript == 998: 
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
	( 0x0 , 0x40 , 998 ), # Common
	( 0x41 , 0x5a , 215 ), # Latin
	( 0x5b , 0x60 , 998 ), # Common
	( 0x61 , 0x7a , 215 ), # Latin
	( 0x7b , 0xa9 , 998 ), # Common
	( 0xaa , 0xaa , 215 ), # Latin
	( 0xab , 0xb9 , 998 ), # Common
	( 0xba , 0xba , 215 ), # Latin
	( 0xbb , 0xbf , 998 ), # Common
	( 0xc0 , 0xd6 , 215 ), # Latin
	( 0xd7 , 0xd7 , 998 ), # Common
	( 0xd8 , 0xf6 , 215 ), # Latin
	( 0xf7 , 0xf7 , 998 ), # Common
	( 0xf8 , 0x2b8 , 215 ), # Latin
	( 0x2b9 , 0x2df , 998 ), # Common
	( 0x2e0 , 0x2e4 , 215 ), # Latin
	( 0x2e5 , 0x2e9 , 998 ), # Common
	( 0x2ea , 0x2eb , 285 ), # Bopomofo
	( 0x2ec , 0x2ff , 998 ), # Common
	( 0x300 , 0x36f , 994 ), # Inherited
	( 0x370 , 0x373 , 200 ), # Greek
	( 0x374 , 0x374 , 998 ), # Common
	( 0x375 , 0x377 , 200 ), # Greek
	( 0x37a , 0x37d , 200 ), # Greek
	( 0x37e , 0x37e , 998 ), # Common
	( 0x37f , 0x37f , 200 ), # Greek
	( 0x384 , 0x384 , 200 ), # Greek
	( 0x385 , 0x385 , 998 ), # Common
	( 0x386 , 0x386 , 200 ), # Greek
	( 0x387 , 0x387 , 998 ), # Common
	( 0x388 , 0x38a , 200 ), # Greek
	( 0x38c , 0x38c , 200 ), # Greek
	( 0x38e , 0x3a1 , 200 ), # Greek
	( 0x3a3 , 0x3e1 , 200 ), # Greek
	( 0x3e2 , 0x3ef , 204 ), # Coptic
	( 0x3f0 , 0x3ff , 200 ), # Greek
	( 0x400 , 0x484 , 220 ), # Cyrillic
	( 0x485 , 0x486 , 994 ), # Inherited
	( 0x487 , 0x52f , 220 ), # Cyrillic
	( 0x531 , 0x556 , 230 ), # Armenian
	( 0x559 , 0x55f , 230 ), # Armenian
	( 0x561 , 0x587 , 230 ), # Armenian
	( 0x589 , 0x589 , 998 ), # Common
	( 0x58a , 0x58a , 230 ), # Armenian
	( 0x58d , 0x58f , 230 ), # Armenian
	( 0x591 , 0x5c7 , 125 ), # Hebrew
	( 0x5d0 , 0x5ea , 125 ), # Hebrew
	( 0x5f0 , 0x5f4 , 125 ), # Hebrew
	( 0x600 , 0x604 , 160 ), # Arabic
	( 0x605 , 0x605 , 998 ), # Common
	( 0x606 , 0x60b , 160 ), # Arabic
	( 0x60c , 0x60c , 998 ), # Common
	( 0x60d , 0x61a , 160 ), # Arabic
	( 0x61b , 0x61c , 998 ), # Common
	( 0x61e , 0x61e , 160 ), # Arabic
	( 0x61f , 0x61f , 998 ), # Common
	( 0x620 , 0x63f , 160 ), # Arabic
	( 0x640 , 0x640 , 998 ), # Common
	( 0x641 , 0x64a , 160 ), # Arabic
	( 0x64b , 0x655 , 994 ), # Inherited
	( 0x656 , 0x66f , 160 ), # Arabic
	( 0x670 , 0x670 , 994 ), # Inherited
	( 0x671 , 0x6dc , 160 ), # Arabic
	( 0x6dd , 0x6dd , 998 ), # Common
	( 0x6de , 0x6ff , 160 ), # Arabic
	( 0x700 , 0x70d , 135 ), # Syriac
	( 0x70f , 0x74a , 135 ), # Syriac
	( 0x74d , 0x74f , 135 ), # Syriac
	( 0x750 , 0x77f , 160 ), # Arabic
	( 0x780 , 0x7b1 , 170 ), # Thaana
	( 0x7c0 , 0x7fa , 165 ), # Nko
	( 0x800 , 0x82d , 123 ), # Samaritan
	( 0x830 , 0x83e , 123 ), # Samaritan
	( 0x840 , 0x85b , 140 ), # Mandaic
	( 0x85e , 0x85e , 140 ), # Mandaic
	( 0x8a0 , 0x8b4 , 160 ), # Arabic
	( 0x8e3 , 0x8ff , 160 ), # Arabic
	( 0x900 , 0x950 , 315 ), # Devanagari
	( 0x951 , 0x952 , 994 ), # Inherited
	( 0x953 , 0x963 , 315 ), # Devanagari
	( 0x964 , 0x965 , 998 ), # Common
	( 0x966 , 0x97f , 315 ), # Devanagari
	( 0x980 , 0x983 , 325 ), # Bengali
	( 0x985 , 0x98c , 325 ), # Bengali
	( 0x98f , 0x990 , 325 ), # Bengali
	( 0x993 , 0x9a8 , 325 ), # Bengali
	( 0x9aa , 0x9b0 , 325 ), # Bengali
	( 0x9b2 , 0x9b2 , 325 ), # Bengali
	( 0x9b6 , 0x9b9 , 325 ), # Bengali
	( 0x9bc , 0x9c4 , 325 ), # Bengali
	( 0x9c7 , 0x9c8 , 325 ), # Bengali
	( 0x9cb , 0x9ce , 325 ), # Bengali
	( 0x9d7 , 0x9d7 , 325 ), # Bengali
	( 0x9dc , 0x9dd , 325 ), # Bengali
	( 0x9df , 0x9e3 , 325 ), # Bengali
	( 0x9e6 , 0x9fb , 325 ), # Bengali
	( 0xa01 , 0xa03 , 310 ), # Gurmukhi
	( 0xa05 , 0xa0a , 310 ), # Gurmukhi
	( 0xa0f , 0xa10 , 310 ), # Gurmukhi
	( 0xa13 , 0xa28 , 310 ), # Gurmukhi
	( 0xa2a , 0xa30 , 310 ), # Gurmukhi
	( 0xa32 , 0xa33 , 310 ), # Gurmukhi
	( 0xa35 , 0xa36 , 310 ), # Gurmukhi
	( 0xa38 , 0xa39 , 310 ), # Gurmukhi
	( 0xa3c , 0xa3c , 310 ), # Gurmukhi
	( 0xa3e , 0xa42 , 310 ), # Gurmukhi
	( 0xa47 , 0xa48 , 310 ), # Gurmukhi
	( 0xa4b , 0xa4d , 310 ), # Gurmukhi
	( 0xa51 , 0xa51 , 310 ), # Gurmukhi
	( 0xa59 , 0xa5c , 310 ), # Gurmukhi
	( 0xa5e , 0xa5e , 310 ), # Gurmukhi
	( 0xa66 , 0xa75 , 310 ), # Gurmukhi
	( 0xa81 , 0xa83 , 320 ), # Gujarati
	( 0xa85 , 0xa8d , 320 ), # Gujarati
	( 0xa8f , 0xa91 , 320 ), # Gujarati
	( 0xa93 , 0xaa8 , 320 ), # Gujarati
	( 0xaaa , 0xab0 , 320 ), # Gujarati
	( 0xab2 , 0xab3 , 320 ), # Gujarati
	( 0xab5 , 0xab9 , 320 ), # Gujarati
	( 0xabc , 0xac5 , 320 ), # Gujarati
	( 0xac7 , 0xac9 , 320 ), # Gujarati
	( 0xacb , 0xacd , 320 ), # Gujarati
	( 0xad0 , 0xad0 , 320 ), # Gujarati
	( 0xae0 , 0xae3 , 320 ), # Gujarati
	( 0xae6 , 0xaf1 , 320 ), # Gujarati
	( 0xaf9 , 0xaf9 , 320 ), # Gujarati
	( 0xb01 , 0xb03 , 327 ), # Oriya
	( 0xb05 , 0xb0c , 327 ), # Oriya
	( 0xb0f , 0xb10 , 327 ), # Oriya
	( 0xb13 , 0xb28 , 327 ), # Oriya
	( 0xb2a , 0xb30 , 327 ), # Oriya
	( 0xb32 , 0xb33 , 327 ), # Oriya
	( 0xb35 , 0xb39 , 327 ), # Oriya
	( 0xb3c , 0xb44 , 327 ), # Oriya
	( 0xb47 , 0xb48 , 327 ), # Oriya
	( 0xb4b , 0xb4d , 327 ), # Oriya
	( 0xb56 , 0xb57 , 327 ), # Oriya
	( 0xb5c , 0xb5d , 327 ), # Oriya
	( 0xb5f , 0xb63 , 327 ), # Oriya
	( 0xb66 , 0xb77 , 327 ), # Oriya
	( 0xb82 , 0xb83 , 346 ), # Tamil
	( 0xb85 , 0xb8a , 346 ), # Tamil
	( 0xb8e , 0xb90 , 346 ), # Tamil
	( 0xb92 , 0xb95 , 346 ), # Tamil
	( 0xb99 , 0xb9a , 346 ), # Tamil
	( 0xb9c , 0xb9c , 346 ), # Tamil
	( 0xb9e , 0xb9f , 346 ), # Tamil
	( 0xba3 , 0xba4 , 346 ), # Tamil
	( 0xba8 , 0xbaa , 346 ), # Tamil
	( 0xbae , 0xbb9 , 346 ), # Tamil
	( 0xbbe , 0xbc2 , 346 ), # Tamil
	( 0xbc6 , 0xbc8 , 346 ), # Tamil
	( 0xbca , 0xbcd , 346 ), # Tamil
	( 0xbd0 , 0xbd0 , 346 ), # Tamil
	( 0xbd7 , 0xbd7 , 346 ), # Tamil
	( 0xbe6 , 0xbfa , 346 ), # Tamil
	( 0xc00 , 0xc03 , 340 ), # Telugu
	( 0xc05 , 0xc0c , 340 ), # Telugu
	( 0xc0e , 0xc10 , 340 ), # Telugu
	( 0xc12 , 0xc28 , 340 ), # Telugu
	( 0xc2a , 0xc39 , 340 ), # Telugu
	( 0xc3d , 0xc44 , 340 ), # Telugu
	( 0xc46 , 0xc48 , 340 ), # Telugu
	( 0xc4a , 0xc4d , 340 ), # Telugu
	( 0xc55 , 0xc56 , 340 ), # Telugu
	( 0xc58 , 0xc5a , 340 ), # Telugu
	( 0xc60 , 0xc63 , 340 ), # Telugu
	( 0xc66 , 0xc6f , 340 ), # Telugu
	( 0xc78 , 0xc7f , 340 ), # Telugu
	( 0xc81 , 0xc83 , 345 ), # Kannada
	( 0xc85 , 0xc8c , 345 ), # Kannada
	( 0xc8e , 0xc90 , 345 ), # Kannada
	( 0xc92 , 0xca8 , 345 ), # Kannada
	( 0xcaa , 0xcb3 , 345 ), # Kannada
	( 0xcb5 , 0xcb9 , 345 ), # Kannada
	( 0xcbc , 0xcc4 , 345 ), # Kannada
	( 0xcc6 , 0xcc8 , 345 ), # Kannada
	( 0xcca , 0xccd , 345 ), # Kannada
	( 0xcd5 , 0xcd6 , 345 ), # Kannada
	( 0xcde , 0xcde , 345 ), # Kannada
	( 0xce0 , 0xce3 , 345 ), # Kannada
	( 0xce6 , 0xcef , 345 ), # Kannada
	( 0xcf1 , 0xcf2 , 345 ), # Kannada
	( 0xd01 , 0xd03 , 347 ), # Malayalam
	( 0xd05 , 0xd0c , 347 ), # Malayalam
	( 0xd0e , 0xd10 , 347 ), # Malayalam
	( 0xd12 , 0xd3a , 347 ), # Malayalam
	( 0xd3d , 0xd44 , 347 ), # Malayalam
	( 0xd46 , 0xd48 , 347 ), # Malayalam
	( 0xd4a , 0xd4e , 347 ), # Malayalam
	( 0xd57 , 0xd57 , 347 ), # Malayalam
	( 0xd5f , 0xd63 , 347 ), # Malayalam
	( 0xd66 , 0xd75 , 347 ), # Malayalam
	( 0xd79 , 0xd7f , 347 ), # Malayalam
	( 0xd82 , 0xd83 , 348 ), # Sinhala
	( 0xd85 , 0xd96 , 348 ), # Sinhala
	( 0xd9a , 0xdb1 , 348 ), # Sinhala
	( 0xdb3 , 0xdbb , 348 ), # Sinhala
	( 0xdbd , 0xdbd , 348 ), # Sinhala
	( 0xdc0 , 0xdc6 , 348 ), # Sinhala
	( 0xdca , 0xdca , 348 ), # Sinhala
	( 0xdcf , 0xdd4 , 348 ), # Sinhala
	( 0xdd6 , 0xdd6 , 348 ), # Sinhala
	( 0xdd8 , 0xddf , 348 ), # Sinhala
	( 0xde6 , 0xdef , 348 ), # Sinhala
	( 0xdf2 , 0xdf4 , 348 ), # Sinhala
	( 0xe01 , 0xe3a , 352 ), # Thai
	( 0xe3f , 0xe3f , 998 ), # Common
	( 0xe40 , 0xe5b , 352 ), # Thai
	( 0xe81 , 0xe82 , 356 ), # Lao
	( 0xe84 , 0xe84 , 356 ), # Lao
	( 0xe87 , 0xe88 , 356 ), # Lao
	( 0xe8a , 0xe8a , 356 ), # Lao
	( 0xe8d , 0xe8d , 356 ), # Lao
	( 0xe94 , 0xe97 , 356 ), # Lao
	( 0xe99 , 0xe9f , 356 ), # Lao
	( 0xea1 , 0xea3 , 356 ), # Lao
	( 0xea5 , 0xea5 , 356 ), # Lao
	( 0xea7 , 0xea7 , 356 ), # Lao
	( 0xeaa , 0xeab , 356 ), # Lao
	( 0xead , 0xeb9 , 356 ), # Lao
	( 0xebb , 0xebd , 356 ), # Lao
	( 0xec0 , 0xec4 , 356 ), # Lao
	( 0xec6 , 0xec6 , 356 ), # Lao
	( 0xec8 , 0xecd , 356 ), # Lao
	( 0xed0 , 0xed9 , 356 ), # Lao
	( 0xedc , 0xedf , 356 ), # Lao
	( 0xf00 , 0xf47 , 330 ), # Tibetan
	( 0xf49 , 0xf6c , 330 ), # Tibetan
	( 0xf71 , 0xf97 , 330 ), # Tibetan
	( 0xf99 , 0xfbc , 330 ), # Tibetan
	( 0xfbe , 0xfcc , 330 ), # Tibetan
	( 0xfce , 0xfd4 , 330 ), # Tibetan
	( 0xfd5 , 0xfd8 , 998 ), # Common
	( 0xfd9 , 0xfda , 330 ), # Tibetan
	( 0x1000 , 0x109f , 350 ), # Myanmar
	( 0x10a0 , 0x10c5 , 240 ), # Georgian
	( 0x10c7 , 0x10c7 , 240 ), # Georgian
	( 0x10cd , 0x10cd , 240 ), # Georgian
	( 0x10d0 , 0x10fa , 240 ), # Georgian
	( 0x10fb , 0x10fb , 998 ), # Common
	( 0x10fc , 0x10ff , 240 ), # Georgian
	( 0x1100 , 0x11ff , 286 ), # Hangul
	( 0x1200 , 0x1248 , 430 ), # Ethiopic
	( 0x124a , 0x124d , 430 ), # Ethiopic
	( 0x1250 , 0x1256 , 430 ), # Ethiopic
	( 0x1258 , 0x1258 , 430 ), # Ethiopic
	( 0x125a , 0x125d , 430 ), # Ethiopic
	( 0x1260 , 0x1288 , 430 ), # Ethiopic
	( 0x128a , 0x128d , 430 ), # Ethiopic
	( 0x1290 , 0x12b0 , 430 ), # Ethiopic
	( 0x12b2 , 0x12b5 , 430 ), # Ethiopic
	( 0x12b8 , 0x12be , 430 ), # Ethiopic
	( 0x12c0 , 0x12c0 , 430 ), # Ethiopic
	( 0x12c2 , 0x12c5 , 430 ), # Ethiopic
	( 0x12c8 , 0x12d6 , 430 ), # Ethiopic
	( 0x12d8 , 0x1310 , 430 ), # Ethiopic
	( 0x1312 , 0x1315 , 430 ), # Ethiopic
	( 0x1318 , 0x135a , 430 ), # Ethiopic
	( 0x135d , 0x137c , 430 ), # Ethiopic
	( 0x1380 , 0x1399 , 430 ), # Ethiopic
	( 0x13a0 , 0x13f5 , 445 ), # Cherokee
	( 0x13f8 , 0x13fd , 445 ), # Cherokee
	( 0x1400 , 0x167f , 440 ), # Canadian_Aboriginal
	( 0x1680 , 0x169c , 212 ), # Ogham
	( 0x16a0 , 0x16ea , 211 ), # Runic
	( 0x16eb , 0x16ed , 998 ), # Common
	( 0x16ee , 0x16f8 , 211 ), # Runic
	( 0x1700 , 0x170c , 370 ), # Tagalog
	( 0x170e , 0x1714 , 370 ), # Tagalog
	( 0x1720 , 0x1734 , 371 ), # Hanunoo
	( 0x1735 , 0x1736 , 998 ), # Common
	( 0x1740 , 0x1753 , 372 ), # Buhid
	( 0x1760 , 0x176c , 373 ), # Tagbanwa
	( 0x176e , 0x1770 , 373 ), # Tagbanwa
	( 0x1772 , 0x1773 , 373 ), # Tagbanwa
	( 0x1780 , 0x17dd , 355 ), # Khmer
	( 0x17e0 , 0x17e9 , 355 ), # Khmer
	( 0x17f0 , 0x17f9 , 355 ), # Khmer
	( 0x1800 , 0x1801 , 145 ), # Mongolian
	( 0x1802 , 0x1803 , 998 ), # Common
	( 0x1804 , 0x1804 , 145 ), # Mongolian
	( 0x1805 , 0x1805 , 998 ), # Common
	( 0x1806 , 0x180e , 145 ), # Mongolian
	( 0x1810 , 0x1819 , 145 ), # Mongolian
	( 0x1820 , 0x1877 , 145 ), # Mongolian
	( 0x1880 , 0x18aa , 145 ), # Mongolian
	( 0x18b0 , 0x18f5 , 440 ), # Canadian_Aboriginal
	( 0x1900 , 0x191e , 336 ), # Limbu
	( 0x1920 , 0x192b , 336 ), # Limbu
	( 0x1930 , 0x193b , 336 ), # Limbu
	( 0x1940 , 0x1940 , 336 ), # Limbu
	( 0x1944 , 0x194f , 336 ), # Limbu
	( 0x1950 , 0x196d , 353 ), # Tai_Le
	( 0x1970 , 0x1974 , 353 ), # Tai_Le
	( 0x1980 , 0x19ab , 354 ), # New_Tai_Lue
	( 0x19b0 , 0x19c9 , 354 ), # New_Tai_Lue
	( 0x19d0 , 0x19da , 354 ), # New_Tai_Lue
	( 0x19de , 0x19df , 354 ), # New_Tai_Lue
	( 0x19e0 , 0x19ff , 355 ), # Khmer
	( 0x1a00 , 0x1a1b , 367 ), # Buginese
	( 0x1a1e , 0x1a1f , 367 ), # Buginese
	( 0x1ab0 , 0x1abe , 994 ), # Inherited
	( 0x1b00 , 0x1b4b , 360 ), # Balinese
	( 0x1b50 , 0x1b7c , 360 ), # Balinese
	( 0x1b80 , 0x1bbf , 362 ), # Sundanese
	( 0x1bc0 , 0x1bf3 , 365 ), # Batak
	( 0x1bfc , 0x1bff , 365 ), # Batak
	( 0x1c00 , 0x1c37 , 335 ), # Lepcha
	( 0x1c3b , 0x1c49 , 335 ), # Lepcha
	( 0x1c4d , 0x1c4f , 335 ), # Lepcha
	( 0x1c50 , 0x1c7f , 261 ), # Ol_Chiki
	( 0x1cc0 , 0x1cc7 , 362 ), # Sundanese
	( 0x1cd0 , 0x1cd2 , 994 ), # Inherited
	( 0x1cd3 , 0x1cd3 , 998 ), # Common
	( 0x1cd4 , 0x1ce0 , 994 ), # Inherited
	( 0x1ce1 , 0x1ce1 , 998 ), # Common
	( 0x1ce2 , 0x1ce8 , 994 ), # Inherited
	( 0x1ce9 , 0x1cec , 998 ), # Common
	( 0x1ced , 0x1ced , 994 ), # Inherited
	( 0x1cee , 0x1cf3 , 998 ), # Common
	( 0x1cf4 , 0x1cf4 , 994 ), # Inherited
	( 0x1cf5 , 0x1cf6 , 998 ), # Common
	( 0x1cf8 , 0x1cf9 , 994 ), # Inherited
	( 0x1d00 , 0x1d25 , 215 ), # Latin
	( 0x1d26 , 0x1d2a , 200 ), # Greek
	( 0x1d2b , 0x1d2b , 220 ), # Cyrillic
	( 0x1d2c , 0x1d5c , 215 ), # Latin
	( 0x1d5d , 0x1d61 , 200 ), # Greek
	( 0x1d62 , 0x1d65 , 215 ), # Latin
	( 0x1d66 , 0x1d6a , 200 ), # Greek
	( 0x1d6b , 0x1d77 , 215 ), # Latin
	( 0x1d78 , 0x1d78 , 220 ), # Cyrillic
	( 0x1d79 , 0x1dbe , 215 ), # Latin
	( 0x1dbf , 0x1dbf , 200 ), # Greek
	( 0x1dc0 , 0x1df5 , 994 ), # Inherited
	( 0x1dfc , 0x1dff , 994 ), # Inherited
	( 0x1e00 , 0x1eff , 215 ), # Latin
	( 0x1f00 , 0x1f15 , 200 ), # Greek
	( 0x1f18 , 0x1f1d , 200 ), # Greek
	( 0x1f20 , 0x1f45 , 200 ), # Greek
	( 0x1f48 , 0x1f4d , 200 ), # Greek
	( 0x1f50 , 0x1f57 , 200 ), # Greek
	( 0x1f59 , 0x1f59 , 200 ), # Greek
	( 0x1f5b , 0x1f5b , 200 ), # Greek
	( 0x1f5d , 0x1f5d , 200 ), # Greek
	( 0x1f5f , 0x1f7d , 200 ), # Greek
	( 0x1f80 , 0x1fb4 , 200 ), # Greek
	( 0x1fb6 , 0x1fc4 , 200 ), # Greek
	( 0x1fc6 , 0x1fd3 , 200 ), # Greek
	( 0x1fd6 , 0x1fdb , 200 ), # Greek
	( 0x1fdd , 0x1fef , 200 ), # Greek
	( 0x1ff2 , 0x1ff4 , 200 ), # Greek
	( 0x1ff6 , 0x1ffe , 200 ), # Greek
	( 0x2000 , 0x200b , 998 ), # Common
	( 0x200c , 0x200d , 994 ), # Inherited
	( 0x200e , 0x2064 , 998 ), # Common
	( 0x2066 , 0x2070 , 998 ), # Common
	( 0x2071 , 0x2071 , 215 ), # Latin
	( 0x2074 , 0x207e , 998 ), # Common
	( 0x207f , 0x207f , 215 ), # Latin
	( 0x2080 , 0x208e , 998 ), # Common
	( 0x2090 , 0x209c , 215 ), # Latin
	( 0x20a0 , 0x20be , 998 ), # Common
	( 0x20d0 , 0x20f0 , 994 ), # Inherited
	( 0x2100 , 0x2125 , 998 ), # Common
	( 0x2126 , 0x2126 , 200 ), # Greek
	( 0x2127 , 0x2129 , 998 ), # Common
	( 0x212a , 0x212b , 215 ), # Latin
	( 0x212c , 0x2131 , 998 ), # Common
	( 0x2132 , 0x2132 , 215 ), # Latin
	( 0x2133 , 0x214d , 998 ), # Common
	( 0x214e , 0x214e , 215 ), # Latin
	( 0x214f , 0x215f , 998 ), # Common
	( 0x2160 , 0x2188 , 215 ), # Latin
	( 0x2189 , 0x218b , 998 ), # Common
	( 0x2190 , 0x23fa , 998 ), # Common
	( 0x2400 , 0x2426 , 998 ), # Common
	( 0x2440 , 0x244a , 998 ), # Common
	( 0x2460 , 0x27ff , 998 ), # Common
	( 0x2800 , 0x28ff , 570 ), # Braille
	( 0x2900 , 0x2b73 , 998 ), # Common
	( 0x2b76 , 0x2b95 , 998 ), # Common
	( 0x2b98 , 0x2bb9 , 998 ), # Common
	( 0x2bbd , 0x2bc8 , 998 ), # Common
	( 0x2bca , 0x2bd1 , 998 ), # Common
	( 0x2bec , 0x2bef , 998 ), # Common
	( 0x2c00 , 0x2c2e , 225 ), # Glagolitic
	( 0x2c30 , 0x2c5e , 225 ), # Glagolitic
	( 0x2c60 , 0x2c7f , 215 ), # Latin
	( 0x2c80 , 0x2cf3 , 204 ), # Coptic
	( 0x2cf9 , 0x2cff , 204 ), # Coptic
	( 0x2d00 , 0x2d25 , 240 ), # Georgian
	( 0x2d27 , 0x2d27 , 240 ), # Georgian
	( 0x2d2d , 0x2d2d , 240 ), # Georgian
	( 0x2d30 , 0x2d67 , 120 ), # Tifinagh
	( 0x2d6f , 0x2d70 , 120 ), # Tifinagh
	( 0x2d7f , 0x2d7f , 120 ), # Tifinagh
	( 0x2d80 , 0x2d96 , 430 ), # Ethiopic
	( 0x2da0 , 0x2da6 , 430 ), # Ethiopic
	( 0x2da8 , 0x2dae , 430 ), # Ethiopic
	( 0x2db0 , 0x2db6 , 430 ), # Ethiopic
	( 0x2db8 , 0x2dbe , 430 ), # Ethiopic
	( 0x2dc0 , 0x2dc6 , 430 ), # Ethiopic
	( 0x2dc8 , 0x2dce , 430 ), # Ethiopic
	( 0x2dd0 , 0x2dd6 , 430 ), # Ethiopic
	( 0x2dd8 , 0x2dde , 430 ), # Ethiopic
	( 0x2de0 , 0x2dff , 220 ), # Cyrillic
	( 0x2e00 , 0x2e42 , 998 ), # Common
	( 0x2e80 , 0x2e99 , 500 ), # Han
	( 0x2e9b , 0x2ef3 , 500 ), # Han
	( 0x2f00 , 0x2fd5 , 500 ), # Han
	( 0x2ff0 , 0x2ffb , 998 ), # Common
	( 0x3000 , 0x3004 , 998 ), # Common
	( 0x3005 , 0x3005 , 500 ), # Han
	( 0x3006 , 0x3006 , 998 ), # Common
	( 0x3007 , 0x3007 , 500 ), # Han
	( 0x3008 , 0x3020 , 998 ), # Common
	( 0x3021 , 0x3029 , 500 ), # Han
	( 0x302a , 0x302d , 994 ), # Inherited
	( 0x302e , 0x302f , 286 ), # Hangul
	( 0x3030 , 0x3037 , 998 ), # Common
	( 0x3038 , 0x303b , 500 ), # Han
	( 0x303c , 0x303f , 998 ), # Common
	( 0x3041 , 0x3096 , 410 ), # Hiragana
	( 0x3099 , 0x309a , 994 ), # Inherited
	( 0x309b , 0x309c , 998 ), # Common
	( 0x309d , 0x309f , 410 ), # Hiragana
	( 0x30a0 , 0x30a0 , 998 ), # Common
	( 0x30a1 , 0x30fa , 411 ), # Katakana
	( 0x30fb , 0x30fc , 998 ), # Common
	( 0x30fd , 0x30ff , 411 ), # Katakana
	( 0x3105 , 0x312d , 285 ), # Bopomofo
	( 0x3131 , 0x318e , 286 ), # Hangul
	( 0x3190 , 0x319f , 998 ), # Common
	( 0x31a0 , 0x31ba , 285 ), # Bopomofo
	( 0x31c0 , 0x31e3 , 998 ), # Common
	( 0x31f0 , 0x31ff , 411 ), # Katakana
	( 0x3200 , 0x321e , 286 ), # Hangul
	( 0x3220 , 0x325f , 998 ), # Common
	( 0x3260 , 0x327e , 286 ), # Hangul
	( 0x327f , 0x32cf , 998 ), # Common
	( 0x32d0 , 0x32fe , 411 ), # Katakana
	( 0x3300 , 0x3357 , 411 ), # Katakana
	( 0x3358 , 0x33ff , 998 ), # Common
	( 0x3400 , 0x4db5 , 500 ), # Han
	( 0x4dc0 , 0x4dff , 998 ), # Common
	( 0x4e00 , 0x9fd5 , 500 ), # Han
	( 0xa000 , 0xa48c , 460 ), # Yi
	( 0xa490 , 0xa4c6 , 460 ), # Yi
	( 0xa4d0 , 0xa4ff , 399 ), # Lisu
	( 0xa500 , 0xa62b , 470 ), # Vai
	( 0xa640 , 0xa69f , 220 ), # Cyrillic
	( 0xa6a0 , 0xa6f7 , 435 ), # Bamum
	( 0xa700 , 0xa721 , 998 ), # Common
	( 0xa722 , 0xa787 , 215 ), # Latin
	( 0xa788 , 0xa78a , 998 ), # Common
	( 0xa78b , 0xa7ad , 215 ), # Latin
	( 0xa7b0 , 0xa7b7 , 215 ), # Latin
	( 0xa7f7 , 0xa7ff , 215 ), # Latin
	( 0xa800 , 0xa82b , 316 ), # Syloti_Nagri
	( 0xa830 , 0xa839 , 998 ), # Common
	( 0xa840 , 0xa877 , 331 ), # Phags_Pa
	( 0xa880 , 0xa8c4 , 344 ), # Saurashtra
	( 0xa8ce , 0xa8d9 , 344 ), # Saurashtra
	( 0xa8e0 , 0xa8fd , 315 ), # Devanagari
	( 0xa900 , 0xa92d , 357 ), # Kayah_Li
	( 0xa92e , 0xa92e , 998 ), # Common
	( 0xa92f , 0xa92f , 357 ), # Kayah_Li
	( 0xa930 , 0xa953 , 363 ), # Rejang
	( 0xa95f , 0xa95f , 363 ), # Rejang
	( 0xa960 , 0xa97c , 286 ), # Hangul
	( 0xa980 , 0xa9cd , 361 ), # Javanese
	( 0xa9cf , 0xa9cf , 998 ), # Common
	( 0xa9d0 , 0xa9d9 , 361 ), # Javanese
	( 0xa9de , 0xa9df , 361 ), # Javanese
	( 0xa9e0 , 0xa9fe , 350 ), # Myanmar
	( 0xaa00 , 0xaa36 , 358 ), # Cham
	( 0xaa40 , 0xaa4d , 358 ), # Cham
	( 0xaa50 , 0xaa59 , 358 ), # Cham
	( 0xaa5c , 0xaa5f , 358 ), # Cham
	( 0xaa60 , 0xaa7f , 350 ), # Myanmar
	( 0xaa80 , 0xaac2 , 359 ), # Tai_Viet
	( 0xaadb , 0xaadf , 359 ), # Tai_Viet
	( 0xaae0 , 0xaaf6 , 337 ), # Meetei_Mayek
	( 0xab01 , 0xab06 , 430 ), # Ethiopic
	( 0xab09 , 0xab0e , 430 ), # Ethiopic
	( 0xab11 , 0xab16 , 430 ), # Ethiopic
	( 0xab20 , 0xab26 , 430 ), # Ethiopic
	( 0xab28 , 0xab2e , 430 ), # Ethiopic
	( 0xab30 , 0xab5a , 215 ), # Latin
	( 0xab5b , 0xab5b , 998 ), # Common
	( 0xab5c , 0xab64 , 215 ), # Latin
	( 0xab65 , 0xab65 , 200 ), # Greek
	( 0xab70 , 0xabbf , 445 ), # Cherokee
	( 0xabc0 , 0xabed , 337 ), # Meetei_Mayek
	( 0xabf0 , 0xabf9 , 337 ), # Meetei_Mayek
	( 0xac00 , 0xd7a3 , 286 ), # Hangul
	( 0xd7b0 , 0xd7c6 , 286 ), # Hangul
	( 0xd7cb , 0xd7fb , 286 ), # Hangul
	( 0xf900 , 0xfa6d , 500 ), # Han
	( 0xfa70 , 0xfad9 , 500 ), # Han
	( 0xfb00 , 0xfb06 , 215 ), # Latin
	( 0xfb13 , 0xfb17 , 230 ), # Armenian
	( 0xfb1d , 0xfb36 , 125 ), # Hebrew
	( 0xfb38 , 0xfb3c , 125 ), # Hebrew
	( 0xfb3e , 0xfb3e , 125 ), # Hebrew
	( 0xfb40 , 0xfb41 , 125 ), # Hebrew
	( 0xfb43 , 0xfb44 , 125 ), # Hebrew
	( 0xfb46 , 0xfb4f , 125 ), # Hebrew
	( 0xfb50 , 0xfbc1 , 160 ), # Arabic
	( 0xfbd3 , 0xfd3d , 160 ), # Arabic
	( 0xfd3e , 0xfd3f , 998 ), # Common
	( 0xfd50 , 0xfd8f , 160 ), # Arabic
	( 0xfd92 , 0xfdc7 , 160 ), # Arabic
	( 0xfdf0 , 0xfdfd , 160 ), # Arabic
	( 0xfe00 , 0xfe0f , 994 ), # Inherited
	( 0xfe10 , 0xfe19 , 998 ), # Common
	( 0xfe20 , 0xfe2d , 994 ), # Inherited
	( 0xfe2e , 0xfe2f , 220 ), # Cyrillic
	( 0xfe30 , 0xfe52 , 998 ), # Common
	( 0xfe54 , 0xfe66 , 998 ), # Common
	( 0xfe68 , 0xfe6b , 998 ), # Common
	( 0xfe70 , 0xfe74 , 160 ), # Arabic
	( 0xfe76 , 0xfefc , 160 ), # Arabic
	( 0xfeff , 0xfeff , 998 ), # Common
	( 0xff01 , 0xff20 , 998 ), # Common
	( 0xff21 , 0xff3a , 215 ), # Latin
	( 0xff3b , 0xff40 , 998 ), # Common
	( 0xff41 , 0xff5a , 215 ), # Latin
	( 0xff5b , 0xff65 , 998 ), # Common
	( 0xff66 , 0xff6f , 411 ), # Katakana
	( 0xff70 , 0xff70 , 998 ), # Common
	( 0xff71 , 0xff9d , 411 ), # Katakana
	( 0xff9e , 0xff9f , 998 ), # Common
	( 0xffa0 , 0xffbe , 286 ), # Hangul
	( 0xffc2 , 0xffc7 , 286 ), # Hangul
	( 0xffca , 0xffcf , 286 ), # Hangul
	( 0xffd2 , 0xffd7 , 286 ), # Hangul
	( 0xffda , 0xffdc , 286 ), # Hangul
	( 0xffe0 , 0xffe6 , 998 ), # Common
	( 0xffe8 , 0xffee , 998 ), # Common
	( 0xfff9 , 0xfffd , 998 ), # Common
	( 0x10000 , 0x1000b , 401 ), # Linear_B
	( 0x1000d , 0x10026 , 401 ), # Linear_B
	( 0x10028 , 0x1003a , 401 ), # Linear_B
	( 0x1003c , 0x1003d , 401 ), # Linear_B
	( 0x1003f , 0x1004d , 401 ), # Linear_B
	( 0x10050 , 0x1005d , 401 ), # Linear_B
	( 0x10080 , 0x100fa , 401 ), # Linear_B
	( 0x10100 , 0x10102 , 998 ), # Common
	( 0x10107 , 0x10133 , 998 ), # Common
	( 0x10137 , 0x1013f , 998 ), # Common
	( 0x10140 , 0x1018c , 200 ), # Greek
	( 0x10190 , 0x1019b , 998 ), # Common
	( 0x101a0 , 0x101a0 , 200 ), # Greek
	( 0x101d0 , 0x101fc , 998 ), # Common
	( 0x101fd , 0x101fd , 994 ), # Inherited
	( 0x10280 , 0x1029c , 202 ), # Lycian
	( 0x102a0 , 0x102d0 , 201 ), # Carian
	( 0x102e0 , 0x102e0 , 994 ), # Inherited
	( 0x102e1 , 0x102fb , 998 ), # Common
	( 0x10300 , 0x10323 , 210 ), # Old_Italic
	( 0x10330 , 0x1034a , 206 ), # Gothic
	( 0x10350 , 0x1037a , 227 ), # Old_Permic
	( 0x10380 , 0x1039d , 40 ), # Ugaritic
	( 0x1039f , 0x1039f , 40 ), # Ugaritic
	( 0x103a0 , 0x103c3 , 30 ), # Old_Persian
	( 0x103c8 , 0x103d5 , 30 ), # Old_Persian
	( 0x10400 , 0x1044f , 250 ), # Deseret
	( 0x10450 , 0x1047f , 281 ), # Shavian
	( 0x10480 , 0x1049d , 260 ), # Osmanya
	( 0x104a0 , 0x104a9 , 260 ), # Osmanya
	( 0x10500 , 0x10527 , 226 ), # Elbasan
	( 0x10530 , 0x10563 , 239 ), # Caucasian_Albanian
	( 0x1056f , 0x1056f , 239 ), # Caucasian_Albanian
	( 0x10600 , 0x10736 , 400 ), # Linear_A
	( 0x10740 , 0x10755 , 400 ), # Linear_A
	( 0x10760 , 0x10767 , 400 ), # Linear_A
	( 0x10800 , 0x10805 , 403 ), # Cypriot
	( 0x10808 , 0x10808 , 403 ), # Cypriot
	( 0x1080a , 0x10835 , 403 ), # Cypriot
	( 0x10837 , 0x10838 , 403 ), # Cypriot
	( 0x1083c , 0x1083c , 403 ), # Cypriot
	( 0x1083f , 0x1083f , 403 ), # Cypriot
	( 0x10840 , 0x10855 , 124 ), # Imperial_Aramaic
	( 0x10857 , 0x1085f , 124 ), # Imperial_Aramaic
	( 0x10860 , 0x1087f , 126 ), # Palmyrene
	( 0x10880 , 0x1089e , 159 ), # Nabataean
	( 0x108a7 , 0x108af , 159 ), # Nabataean
	( 0x10900 , 0x1091b , 115 ), # Phoenician
	( 0x1091f , 0x1091f , 115 ), # Phoenician
	( 0x10920 , 0x10939 , 116 ), # Lydian
	( 0x1093f , 0x1093f , 116 ), # Lydian
	( 0x10980 , 0x1099f , 100 ), # Meroitic_Hieroglyphs
	( 0x109a0 , 0x109b7 , 101 ), # Meroitic_Cursive
	( 0x109bc , 0x109cf , 101 ), # Meroitic_Cursive
	( 0x109d2 , 0x109ff , 101 ), # Meroitic_Cursive
	( 0x10a00 , 0x10a03 , 305 ), # Kharoshthi
	( 0x10a05 , 0x10a06 , 305 ), # Kharoshthi
	( 0x10a0c , 0x10a13 , 305 ), # Kharoshthi
	( 0x10a15 , 0x10a17 , 305 ), # Kharoshthi
	( 0x10a19 , 0x10a33 , 305 ), # Kharoshthi
	( 0x10a38 , 0x10a3a , 305 ), # Kharoshthi
	( 0x10a3f , 0x10a47 , 305 ), # Kharoshthi
	( 0x10a50 , 0x10a58 , 305 ), # Kharoshthi
	( 0x10a60 , 0x10a7f , 105 ), # Old_South_Arabian
	( 0x10a80 , 0x10a9f , 106 ), # Old_North_Arabian
	( 0x10ac0 , 0x10ae6 , 139 ), # Manichaean
	( 0x10aeb , 0x10af6 , 139 ), # Manichaean
	( 0x10b00 , 0x10b35 , 134 ), # Avestan
	( 0x10b39 , 0x10b3f , 134 ), # Avestan
	( 0x10b40 , 0x10b55 , 130 ), # Inscriptional_Parthian
	( 0x10b58 , 0x10b5f , 130 ), # Inscriptional_Parthian
	( 0x10b60 , 0x10b72 , 131 ), # Inscriptional_Pahlavi
	( 0x10b78 , 0x10b7f , 131 ), # Inscriptional_Pahlavi
	( 0x10b80 , 0x10b91 , 132 ), # Psalter_Pahlavi
	( 0x10b99 , 0x10b9c , 132 ), # Psalter_Pahlavi
	( 0x10ba9 , 0x10baf , 132 ), # Psalter_Pahlavi
	( 0x10c00 , 0x10c48 , 175 ), # Old_Turkic
	( 0x10e60 , 0x10e7e , 160 ), # Arabic
	( 0x11000 , 0x1104d , 300 ), # Brahmi
	( 0x11052 , 0x1106f , 300 ), # Brahmi
	( 0x1107f , 0x1107f , 300 ), # Brahmi
	( 0x11080 , 0x110c1 , 317 ), # Kaithi
	( 0x110d0 , 0x110e8 , 398 ), # Sora_Sompeng
	( 0x110f0 , 0x110f9 , 398 ), # Sora_Sompeng
	( 0x11100 , 0x11134 , 349 ), # Chakma
	( 0x11136 , 0x11143 , 349 ), # Chakma
	( 0x11150 , 0x11176 , 314 ), # Mahajani
	( 0x11180 , 0x111cd , 319 ), # Sharada
	( 0x111d0 , 0x111df , 319 ), # Sharada
	( 0x111e1 , 0x111f4 , 348 ), # Sinhala
	( 0x11200 , 0x11211 , 322 ), # Khojki
	( 0x11213 , 0x1123d , 322 ), # Khojki
	( 0x11280 , 0x11286 , 323 ), # Multani
	( 0x11288 , 0x11288 , 323 ), # Multani
	( 0x1128a , 0x1128d , 323 ), # Multani
	( 0x1128f , 0x1129d , 323 ), # Multani
	( 0x1129f , 0x112a9 , 323 ), # Multani
	( 0x112b0 , 0x112ea , 318 ), # Khudawadi
	( 0x112f0 , 0x112f9 , 318 ), # Khudawadi
	( 0x11300 , 0x11303 , 343 ), # Grantha
	( 0x11305 , 0x1130c , 343 ), # Grantha
	( 0x1130f , 0x11310 , 343 ), # Grantha
	( 0x11313 , 0x11328 , 343 ), # Grantha
	( 0x1132a , 0x11330 , 343 ), # Grantha
	( 0x11332 , 0x11333 , 343 ), # Grantha
	( 0x11335 , 0x11339 , 343 ), # Grantha
	( 0x1133c , 0x11344 , 343 ), # Grantha
	( 0x11347 , 0x11348 , 343 ), # Grantha
	( 0x1134b , 0x1134d , 343 ), # Grantha
	( 0x11350 , 0x11350 , 343 ), # Grantha
	( 0x11357 , 0x11357 , 343 ), # Grantha
	( 0x1135d , 0x11363 , 343 ), # Grantha
	( 0x11366 , 0x1136c , 343 ), # Grantha
	( 0x11370 , 0x11374 , 343 ), # Grantha
	( 0x11480 , 0x114c7 , 326 ), # Tirhuta
	( 0x114d0 , 0x114d9 , 326 ), # Tirhuta
	( 0x11580 , 0x115b5 , 302 ), # Siddham
	( 0x115b8 , 0x115dd , 302 ), # Siddham
	( 0x11600 , 0x11644 , 324 ), # Modi
	( 0x11650 , 0x11659 , 324 ), # Modi
	( 0x11680 , 0x116b7 , 321 ), # Takri
	( 0x116c0 , 0x116c9 , 321 ), # Takri
	( 0x118a0 , 0x118f2 , 262 ), # Warang_Citi
	( 0x118ff , 0x118ff , 262 ), # Warang_Citi
	( 0x11ac0 , 0x11af8 , 263 ), # Pau_Cin_Hau
	( 0x12000 , 0x12399 , 20 ), # Cuneiform
	( 0x12400 , 0x1246e , 20 ), # Cuneiform
	( 0x12470 , 0x12474 , 20 ), # Cuneiform
	( 0x12480 , 0x12543 , 20 ), # Cuneiform
	( 0x13000 , 0x1342e , 50 ), # Egyptian_Hieroglyphs
	( 0x16800 , 0x16a38 , 435 ), # Bamum
	( 0x16a40 , 0x16a5e , 199 ), # Mro
	( 0x16a60 , 0x16a69 , 199 ), # Mro
	( 0x16a6e , 0x16a6f , 199 ), # Mro
	( 0x16ad0 , 0x16aed , 259 ), # Bassa_Vah
	( 0x16af0 , 0x16af5 , 259 ), # Bassa_Vah
	( 0x16b00 , 0x16b45 , 450 ), # Pahawh_Hmong
	( 0x16b50 , 0x16b59 , 450 ), # Pahawh_Hmong
	( 0x16b5b , 0x16b61 , 450 ), # Pahawh_Hmong
	( 0x16b63 , 0x16b77 , 450 ), # Pahawh_Hmong
	( 0x16b7d , 0x16b8f , 450 ), # Pahawh_Hmong
	( 0x16f00 , 0x16f44 , 282 ), # Miao
	( 0x16f50 , 0x16f7e , 282 ), # Miao
	( 0x16f8f , 0x16f9f , 282 ), # Miao
	( 0x1b000 , 0x1b000 , 411 ), # Katakana
	( 0x1b001 , 0x1b001 , 410 ), # Hiragana
	( 0x1bc00 , 0x1bc6a , 755 ), # Duployan
	( 0x1bc70 , 0x1bc7c , 755 ), # Duployan
	( 0x1bc80 , 0x1bc88 , 755 ), # Duployan
	( 0x1bc90 , 0x1bc99 , 755 ), # Duployan
	( 0x1bc9c , 0x1bc9f , 755 ), # Duployan
	( 0x1bca0 , 0x1bca3 , 998 ), # Common
	( 0x1d000 , 0x1d0f5 , 998 ), # Common
	( 0x1d100 , 0x1d126 , 998 ), # Common
	( 0x1d129 , 0x1d166 , 998 ), # Common
	( 0x1d167 , 0x1d169 , 994 ), # Inherited
	( 0x1d16a , 0x1d17a , 998 ), # Common
	( 0x1d17b , 0x1d182 , 994 ), # Inherited
	( 0x1d183 , 0x1d184 , 998 ), # Common
	( 0x1d185 , 0x1d18b , 994 ), # Inherited
	( 0x1d18c , 0x1d1a9 , 998 ), # Common
	( 0x1d1aa , 0x1d1ad , 994 ), # Inherited
	( 0x1d1ae , 0x1d1e8 , 998 ), # Common
	( 0x1d200 , 0x1d245 , 200 ), # Greek
	( 0x1d300 , 0x1d356 , 998 ), # Common
	( 0x1d360 , 0x1d371 , 998 ), # Common
	( 0x1d400 , 0x1d454 , 998 ), # Common
	( 0x1d456 , 0x1d49c , 998 ), # Common
	( 0x1d49e , 0x1d49f , 998 ), # Common
	( 0x1d4a2 , 0x1d4a2 , 998 ), # Common
	( 0x1d4a5 , 0x1d4a6 , 998 ), # Common
	( 0x1d4a9 , 0x1d4ac , 998 ), # Common
	( 0x1d4ae , 0x1d4b9 , 998 ), # Common
	( 0x1d4bb , 0x1d4bb , 998 ), # Common
	( 0x1d4bd , 0x1d4c3 , 998 ), # Common
	( 0x1d4c5 , 0x1d505 , 998 ), # Common
	( 0x1d507 , 0x1d50a , 998 ), # Common
	( 0x1d50d , 0x1d514 , 998 ), # Common
	( 0x1d516 , 0x1d51c , 998 ), # Common
	( 0x1d51e , 0x1d539 , 998 ), # Common
	( 0x1d53b , 0x1d53e , 998 ), # Common
	( 0x1d540 , 0x1d544 , 998 ), # Common
	( 0x1d546 , 0x1d546 , 998 ), # Common
	( 0x1d54a , 0x1d550 , 998 ), # Common
	( 0x1d552 , 0x1d6a5 , 998 ), # Common
	( 0x1d6a8 , 0x1d7cb , 998 ), # Common
	( 0x1d7ce , 0x1d7ff , 998 ), # Common
	( 0x1e800 , 0x1e8c4 , 438 ), # Mende_Kikakui
	( 0x1e8c7 , 0x1e8d6 , 438 ), # Mende_Kikakui
	( 0x1ee00 , 0x1ee03 , 160 ), # Arabic
	( 0x1ee05 , 0x1ee1f , 160 ), # Arabic
	( 0x1ee21 , 0x1ee22 , 160 ), # Arabic
	( 0x1ee24 , 0x1ee24 , 160 ), # Arabic
	( 0x1ee27 , 0x1ee27 , 160 ), # Arabic
	( 0x1ee29 , 0x1ee32 , 160 ), # Arabic
	( 0x1ee34 , 0x1ee37 , 160 ), # Arabic
	( 0x1ee39 , 0x1ee39 , 160 ), # Arabic
	( 0x1ee3b , 0x1ee3b , 160 ), # Arabic
	( 0x1ee42 , 0x1ee42 , 160 ), # Arabic
	( 0x1ee47 , 0x1ee47 , 160 ), # Arabic
	( 0x1ee49 , 0x1ee49 , 160 ), # Arabic
	( 0x1ee4b , 0x1ee4b , 160 ), # Arabic
	( 0x1ee4d , 0x1ee4f , 160 ), # Arabic
	( 0x1ee51 , 0x1ee52 , 160 ), # Arabic
	( 0x1ee54 , 0x1ee54 , 160 ), # Arabic
	( 0x1ee57 , 0x1ee57 , 160 ), # Arabic
	( 0x1ee59 , 0x1ee59 , 160 ), # Arabic
	( 0x1ee5b , 0x1ee5b , 160 ), # Arabic
	( 0x1ee5d , 0x1ee5d , 160 ), # Arabic
	( 0x1ee5f , 0x1ee5f , 160 ), # Arabic
	( 0x1ee61 , 0x1ee62 , 160 ), # Arabic
	( 0x1ee64 , 0x1ee64 , 160 ), # Arabic
	( 0x1ee67 , 0x1ee6a , 160 ), # Arabic
	( 0x1ee6c , 0x1ee72 , 160 ), # Arabic
	( 0x1ee74 , 0x1ee77 , 160 ), # Arabic
	( 0x1ee79 , 0x1ee7c , 160 ), # Arabic
	( 0x1ee7e , 0x1ee7e , 160 ), # Arabic
	( 0x1ee80 , 0x1ee89 , 160 ), # Arabic
	( 0x1ee8b , 0x1ee9b , 160 ), # Arabic
	( 0x1eea1 , 0x1eea3 , 160 ), # Arabic
	( 0x1eea5 , 0x1eea9 , 160 ), # Arabic
	( 0x1eeab , 0x1eebb , 160 ), # Arabic
	( 0x1eef0 , 0x1eef1 , 160 ), # Arabic
	( 0x1f000 , 0x1f02b , 998 ), # Common
	( 0x1f030 , 0x1f093 , 998 ), # Common
	( 0x1f0a0 , 0x1f0ae , 998 ), # Common
	( 0x1f0b1 , 0x1f0bf , 998 ), # Common
	( 0x1f0c1 , 0x1f0cf , 998 ), # Common
	( 0x1f0d1 , 0x1f0f5 , 998 ), # Common
	( 0x1f100 , 0x1f10c , 998 ), # Common
	( 0x1f110 , 0x1f12e , 998 ), # Common
	( 0x1f130 , 0x1f16b , 998 ), # Common
	( 0x1f170 , 0x1f19a , 998 ), # Common
	( 0x1f1e6 , 0x1f1ff , 998 ), # Common
	( 0x1f200 , 0x1f200 , 410 ), # Hiragana
	( 0x1f201 , 0x1f202 , 998 ), # Common
	( 0x1f210 , 0x1f23a , 998 ), # Common
	( 0x1f240 , 0x1f248 , 998 ), # Common
	( 0x1f250 , 0x1f251 , 998 ), # Common
	( 0x1f300 , 0x1f579 , 998 ), # Common
	( 0x1f57b , 0x1f5a3 , 998 ), # Common
	( 0x1f5a5 , 0x1f6d0 , 998 ), # Common
	( 0x1f6e0 , 0x1f6ec , 998 ), # Common
	( 0x1f6f0 , 0x1f6f3 , 998 ), # Common
	( 0x1f700 , 0x1f773 , 998 ), # Common
	( 0x1f780 , 0x1f7d4 , 998 ), # Common
	( 0x1f800 , 0x1f80b , 998 ), # Common
	( 0x1f810 , 0x1f847 , 998 ), # Common
	( 0x1f850 , 0x1f859 , 998 ), # Common
	( 0x1f860 , 0x1f887 , 998 ), # Common
	( 0x1f890 , 0x1f8ad , 998 ), # Common
	( 0x1f910 , 0x1f918 , 998 ), # Common
	( 0x1f980 , 0x1f984 , 998 ), # Common
	( 0x1f9c0 , 0x1f9c0 , 998 ), # Common
	( 0x20000 , 0x2a6d6 , 500 ), # Han
	( 0x2a700 , 0x2b734 , 500 ), # Han
	( 0x2b740 , 0x2b81d , 500 ), # Han
	( 0x2b820 , 0x2cea1 , 500 ), # Han
	( 0x2f800 , 0x2fa1d , 500 ), # Han
	( 0xe0001 , 0xe0001 , 998 ), # Common
	( 0xe0020 , 0xe007f , 998 ), # Common
]
scriptCode= [
	( 0x0 , 0x40 , 998 ), # Common
	( 0x41 , 0x5a , 215 ), # Latin
	( 0x5b , 0x60 , 998 ), # Common
	( 0x61 , 0x7a , 215 ), # Latin
	( 0x7b , 0xa9 , 998 ), # Common
	( 0xaa , 0xaa , 215 ), # Latin
	( 0xab , 0xb9 , 998 ), # Common
	( 0xba , 0xba , 215 ), # Latin
	( 0xbb , 0xbf , 998 ), # Common
	( 0xc0 , 0xd6 , 215 ), # Latin
	( 0xd7 , 0xd7 , 998 ), # Common
	( 0xd8 , 0xf6 , 215 ), # Latin
	( 0xf7 , 0xf7 , 998 ), # Common
	( 0xf8 , 0x2b8 , 215 ), # Latin
	( 0x2b9 , 0x2df , 998 ), # Common
	( 0x2e0 , 0x2e4 , 215 ), # Latin
	( 0x2e5 , 0x2e9 , 998 ), # Common
	( 0x2ea , 0x2eb , 285 ), # Bopomofo
	( 0x2ec , 0x2ff , 998 ), # Common
	( 0x300 , 0x36f , 994 ), # Inherited
	( 0x370 , 0x373 , 200 ), # Greek
	( 0x374 , 0x374 , 998 ), # Common
	( 0x375 , 0x377 , 200 ), # Greek
	( 0x37a , 0x37d , 200 ), # Greek
	( 0x37e , 0x37e , 998 ), # Common
	( 0x37f , 0x37f , 200 ), # Greek
	( 0x384 , 0x384 , 200 ), # Greek
	( 0x385 , 0x385 , 998 ), # Common
	( 0x386 , 0x386 , 200 ), # Greek
	( 0x387 , 0x387 , 998 ), # Common
	( 0x388 , 0x38a , 200 ), # Greek
	( 0x38c , 0x38c , 200 ), # Greek
	( 0x38e , 0x3a1 , 200 ), # Greek
	( 0x3a3 , 0x3e1 , 200 ), # Greek
	( 0x3e2 , 0x3ef , 204 ), # Coptic
	( 0x3f0 , 0x3ff , 200 ), # Greek
	( 0x400 , 0x484 , 220 ), # Cyrillic
	( 0x485 , 0x486 , 994 ), # Inherited
	( 0x487 , 0x52f , 220 ), # Cyrillic
	( 0x531 , 0x556 , 230 ), # Armenian
	( 0x559 , 0x55f , 230 ), # Armenian
	( 0x561 , 0x587 , 230 ), # Armenian
	( 0x589 , 0x589 , 998 ), # Common
	( 0x58a , 0x58a , 230 ), # Armenian
	( 0x58d , 0x58f , 230 ), # Armenian
	( 0x591 , 0x5c7 , 125 ), # Hebrew
	( 0x5d0 , 0x5ea , 125 ), # Hebrew
	( 0x5f0 , 0x5f4 , 125 ), # Hebrew
	( 0x600 , 0x604 , 160 ), # Arabic
	( 0x605 , 0x605 , 998 ), # Common
	( 0x606 , 0x60b , 160 ), # Arabic
	( 0x60c , 0x60c , 998 ), # Common
	( 0x60d , 0x61a , 160 ), # Arabic
	( 0x61b , 0x61c , 998 ), # Common
	( 0x61e , 0x61e , 160 ), # Arabic
	( 0x61f , 0x61f , 998 ), # Common
	( 0x620 , 0x63f , 160 ), # Arabic
	( 0x640 , 0x640 , 998 ), # Common
	( 0x641 , 0x64a , 160 ), # Arabic
	( 0x64b , 0x655 , 994 ), # Inherited
	( 0x656 , 0x66f , 160 ), # Arabic
	( 0x670 , 0x670 , 994 ), # Inherited
	( 0x671 , 0x6dc , 160 ), # Arabic
	( 0x6dd , 0x6dd , 998 ), # Common
	( 0x6de , 0x6ff , 160 ), # Arabic
	( 0x700 , 0x70d , 135 ), # Syriac
	( 0x70f , 0x74a , 135 ), # Syriac
	( 0x74d , 0x74f , 135 ), # Syriac
	( 0x750 , 0x77f , 160 ), # Arabic
	( 0x780 , 0x7b1 , 170 ), # Thaana
	( 0x7c0 , 0x7fa , 165 ), # Nko
	( 0x800 , 0x82d , 123 ), # Samaritan
	( 0x830 , 0x83e , 123 ), # Samaritan
	( 0x840 , 0x85b , 140 ), # Mandaic
	( 0x85e , 0x85e , 140 ), # Mandaic
	( 0x8a0 , 0x8b4 , 160 ), # Arabic
	( 0x8e3 , 0x8ff , 160 ), # Arabic
	( 0x900 , 0x950 , 315 ), # Devanagari
	( 0x951 , 0x952 , 994 ), # Inherited
	( 0x953 , 0x963 , 315 ), # Devanagari
	( 0x964 , 0x965 , 998 ), # Common
	( 0x966 , 0x97f , 315 ), # Devanagari
	( 0x980 , 0x983 , 325 ), # Bengali
	( 0x985 , 0x98c , 325 ), # Bengali
	( 0x98f , 0x990 , 325 ), # Bengali
	( 0x993 , 0x9a8 , 325 ), # Bengali
	( 0x9aa , 0x9b0 , 325 ), # Bengali
	( 0x9b2 , 0x9b2 , 325 ), # Bengali
	( 0x9b6 , 0x9b9 , 325 ), # Bengali
	( 0x9bc , 0x9c4 , 325 ), # Bengali
	( 0x9c7 , 0x9c8 , 325 ), # Bengali
	( 0x9cb , 0x9ce , 325 ), # Bengali
	( 0x9d7 , 0x9d7 , 325 ), # Bengali
	( 0x9dc , 0x9dd , 325 ), # Bengali
	( 0x9df , 0x9e3 , 325 ), # Bengali
	( 0x9e6 , 0x9fb , 325 ), # Bengali
	( 0xa01 , 0xa03 , 310 ), # Gurmukhi
	( 0xa05 , 0xa0a , 310 ), # Gurmukhi
	( 0xa0f , 0xa10 , 310 ), # Gurmukhi
	( 0xa13 , 0xa28 , 310 ), # Gurmukhi
	( 0xa2a , 0xa30 , 310 ), # Gurmukhi
	( 0xa32 , 0xa33 , 310 ), # Gurmukhi
	( 0xa35 , 0xa36 , 310 ), # Gurmukhi
	( 0xa38 , 0xa39 , 310 ), # Gurmukhi
	( 0xa3c , 0xa3c , 310 ), # Gurmukhi
	( 0xa3e , 0xa42 , 310 ), # Gurmukhi
	( 0xa47 , 0xa48 , 310 ), # Gurmukhi
	( 0xa4b , 0xa4d , 310 ), # Gurmukhi
	( 0xa51 , 0xa51 , 310 ), # Gurmukhi
	( 0xa59 , 0xa5c , 310 ), # Gurmukhi
	( 0xa5e , 0xa5e , 310 ), # Gurmukhi
	( 0xa66 , 0xa75 , 310 ), # Gurmukhi
	( 0xa81 , 0xa83 , 320 ), # Gujarati
	( 0xa85 , 0xa8d , 320 ), # Gujarati
	( 0xa8f , 0xa91 , 320 ), # Gujarati
	( 0xa93 , 0xaa8 , 320 ), # Gujarati
	( 0xaaa , 0xab0 , 320 ), # Gujarati
	( 0xab2 , 0xab3 , 320 ), # Gujarati
	( 0xab5 , 0xab9 , 320 ), # Gujarati
	( 0xabc , 0xac5 , 320 ), # Gujarati
	( 0xac7 , 0xac9 , 320 ), # Gujarati
	( 0xacb , 0xacd , 320 ), # Gujarati
	( 0xad0 , 0xad0 , 320 ), # Gujarati
	( 0xae0 , 0xae3 , 320 ), # Gujarati
	( 0xae6 , 0xaf1 , 320 ), # Gujarati
	( 0xaf9 , 0xaf9 , 320 ), # Gujarati
	( 0xb01 , 0xb03 , 327 ), # Oriya
	( 0xb05 , 0xb0c , 327 ), # Oriya
	( 0xb0f , 0xb10 , 327 ), # Oriya
	( 0xb13 , 0xb28 , 327 ), # Oriya
	( 0xb2a , 0xb30 , 327 ), # Oriya
	( 0xb32 , 0xb33 , 327 ), # Oriya
	( 0xb35 , 0xb39 , 327 ), # Oriya
	( 0xb3c , 0xb44 , 327 ), # Oriya
	( 0xb47 , 0xb48 , 327 ), # Oriya
	( 0xb4b , 0xb4d , 327 ), # Oriya
	( 0xb56 , 0xb57 , 327 ), # Oriya
	( 0xb5c , 0xb5d , 327 ), # Oriya
	( 0xb5f , 0xb63 , 327 ), # Oriya
	( 0xb66 , 0xb77 , 327 ), # Oriya
	( 0xb82 , 0xb83 , 346 ), # Tamil
	( 0xb85 , 0xb8a , 346 ), # Tamil
	( 0xb8e , 0xb90 , 346 ), # Tamil
	( 0xb92 , 0xb95 , 346 ), # Tamil
	( 0xb99 , 0xb9a , 346 ), # Tamil
	( 0xb9c , 0xb9c , 346 ), # Tamil
	( 0xb9e , 0xb9f , 346 ), # Tamil
	( 0xba3 , 0xba4 , 346 ), # Tamil
	( 0xba8 , 0xbaa , 346 ), # Tamil
	( 0xbae , 0xbb9 , 346 ), # Tamil
	( 0xbbe , 0xbc2 , 346 ), # Tamil
	( 0xbc6 , 0xbc8 , 346 ), # Tamil
	( 0xbca , 0xbcd , 346 ), # Tamil
	( 0xbd0 , 0xbd0 , 346 ), # Tamil
	( 0xbd7 , 0xbd7 , 346 ), # Tamil
	( 0xbe6 , 0xbfa , 346 ), # Tamil
	( 0xc00 , 0xc03 , 340 ), # Telugu
	( 0xc05 , 0xc0c , 340 ), # Telugu
	( 0xc0e , 0xc10 , 340 ), # Telugu
	( 0xc12 , 0xc28 , 340 ), # Telugu
	( 0xc2a , 0xc39 , 340 ), # Telugu
	( 0xc3d , 0xc44 , 340 ), # Telugu
	( 0xc46 , 0xc48 , 340 ), # Telugu
	( 0xc4a , 0xc4d , 340 ), # Telugu
	( 0xc55 , 0xc56 , 340 ), # Telugu
	( 0xc58 , 0xc5a , 340 ), # Telugu
	( 0xc60 , 0xc63 , 340 ), # Telugu
	( 0xc66 , 0xc6f , 340 ), # Telugu
	( 0xc78 , 0xc7f , 340 ), # Telugu
	( 0xc81 , 0xc83 , 345 ), # Kannada
	( 0xc85 , 0xc8c , 345 ), # Kannada
	( 0xc8e , 0xc90 , 345 ), # Kannada
	( 0xc92 , 0xca8 , 345 ), # Kannada
	( 0xcaa , 0xcb3 , 345 ), # Kannada
	( 0xcb5 , 0xcb9 , 345 ), # Kannada
	( 0xcbc , 0xcc4 , 345 ), # Kannada
	( 0xcc6 , 0xcc8 , 345 ), # Kannada
	( 0xcca , 0xccd , 345 ), # Kannada
	( 0xcd5 , 0xcd6 , 345 ), # Kannada
	( 0xcde , 0xcde , 345 ), # Kannada
	( 0xce0 , 0xce3 , 345 ), # Kannada
	( 0xce6 , 0xcef , 345 ), # Kannada
	( 0xcf1 , 0xcf2 , 345 ), # Kannada
	( 0xd01 , 0xd03 , 347 ), # Malayalam
	( 0xd05 , 0xd0c , 347 ), # Malayalam
	( 0xd0e , 0xd10 , 347 ), # Malayalam
	( 0xd12 , 0xd3a , 347 ), # Malayalam
	( 0xd3d , 0xd44 , 347 ), # Malayalam
	( 0xd46 , 0xd48 , 347 ), # Malayalam
	( 0xd4a , 0xd4e , 347 ), # Malayalam
	( 0xd57 , 0xd57 , 347 ), # Malayalam
	( 0xd5f , 0xd63 , 347 ), # Malayalam
	( 0xd66 , 0xd75 , 347 ), # Malayalam
	( 0xd79 , 0xd7f , 347 ), # Malayalam
	( 0xd82 , 0xd83 , 348 ), # Sinhala
	( 0xd85 , 0xd96 , 348 ), # Sinhala
	( 0xd9a , 0xdb1 , 348 ), # Sinhala
	( 0xdb3 , 0xdbb , 348 ), # Sinhala
	( 0xdbd , 0xdbd , 348 ), # Sinhala
	( 0xdc0 , 0xdc6 , 348 ), # Sinhala
	( 0xdca , 0xdca , 348 ), # Sinhala
	( 0xdcf , 0xdd4 , 348 ), # Sinhala
	( 0xdd6 , 0xdd6 , 348 ), # Sinhala
	( 0xdd8 , 0xddf , 348 ), # Sinhala
	( 0xde6 , 0xdef , 348 ), # Sinhala
	( 0xdf2 , 0xdf4 , 348 ), # Sinhala
	( 0xe01 , 0xe3a , 352 ), # Thai
	( 0xe3f , 0xe3f , 998 ), # Common
	( 0xe40 , 0xe5b , 352 ), # Thai
	( 0xe81 , 0xe82 , 356 ), # Lao
	( 0xe84 , 0xe84 , 356 ), # Lao
	( 0xe87 , 0xe88 , 356 ), # Lao
	( 0xe8a , 0xe8a , 356 ), # Lao
	( 0xe8d , 0xe8d , 356 ), # Lao
	( 0xe94 , 0xe97 , 356 ), # Lao
	( 0xe99 , 0xe9f , 356 ), # Lao
	( 0xea1 , 0xea3 , 356 ), # Lao
	( 0xea5 , 0xea5 , 356 ), # Lao
	( 0xea7 , 0xea7 , 356 ), # Lao
	( 0xeaa , 0xeab , 356 ), # Lao
	( 0xead , 0xeb9 , 356 ), # Lao
	( 0xebb , 0xebd , 356 ), # Lao
	( 0xec0 , 0xec4 , 356 ), # Lao
	( 0xec6 , 0xec6 , 356 ), # Lao
	( 0xec8 , 0xecd , 356 ), # Lao
	( 0xed0 , 0xed9 , 356 ), # Lao
	( 0xedc , 0xedf , 356 ), # Lao
	( 0xf00 , 0xf47 , 330 ), # Tibetan
	( 0xf49 , 0xf6c , 330 ), # Tibetan
	( 0xf71 , 0xf97 , 330 ), # Tibetan
	( 0xf99 , 0xfbc , 330 ), # Tibetan
	( 0xfbe , 0xfcc , 330 ), # Tibetan
	( 0xfce , 0xfd4 , 330 ), # Tibetan
	( 0xfd5 , 0xfd8 , 998 ), # Common
	( 0xfd9 , 0xfda , 330 ), # Tibetan
	( 0x1000 , 0x109f , 350 ), # Myanmar
	( 0x10a0 , 0x10c5 , 240 ), # Georgian
	( 0x10c7 , 0x10c7 , 240 ), # Georgian
	( 0x10cd , 0x10cd , 240 ), # Georgian
	( 0x10d0 , 0x10fa , 240 ), # Georgian
	( 0x10fb , 0x10fb , 998 ), # Common
	( 0x10fc , 0x10ff , 240 ), # Georgian
	( 0x1100 , 0x11ff , 286 ), # Hangul
	( 0x1200 , 0x1248 , 430 ), # Ethiopic
	( 0x124a , 0x124d , 430 ), # Ethiopic
	( 0x1250 , 0x1256 , 430 ), # Ethiopic
	( 0x1258 , 0x1258 , 430 ), # Ethiopic
	( 0x125a , 0x125d , 430 ), # Ethiopic
	( 0x1260 , 0x1288 , 430 ), # Ethiopic
	( 0x128a , 0x128d , 430 ), # Ethiopic
	( 0x1290 , 0x12b0 , 430 ), # Ethiopic
	( 0x12b2 , 0x12b5 , 430 ), # Ethiopic
	( 0x12b8 , 0x12be , 430 ), # Ethiopic
	( 0x12c0 , 0x12c0 , 430 ), # Ethiopic
	( 0x12c2 , 0x12c5 , 430 ), # Ethiopic
	( 0x12c8 , 0x12d6 , 430 ), # Ethiopic
	( 0x12d8 , 0x1310 , 430 ), # Ethiopic
	( 0x1312 , 0x1315 , 430 ), # Ethiopic
	( 0x1318 , 0x135a , 430 ), # Ethiopic
	( 0x135d , 0x137c , 430 ), # Ethiopic
	( 0x1380 , 0x1399 , 430 ), # Ethiopic
	( 0x13a0 , 0x13f5 , 445 ), # Cherokee
	( 0x13f8 , 0x13fd , 445 ), # Cherokee
	( 0x1400 , 0x167f , 440 ), # Canadian_Aboriginal
	( 0x1680 , 0x169c , 212 ), # Ogham
	( 0x16a0 , 0x16ea , 211 ), # Runic
	( 0x16eb , 0x16ed , 998 ), # Common
	( 0x16ee , 0x16f8 , 211 ), # Runic
	( 0x1700 , 0x170c , 370 ), # Tagalog
	( 0x170e , 0x1714 , 370 ), # Tagalog
	( 0x1720 , 0x1734 , 371 ), # Hanunoo
	( 0x1735 , 0x1736 , 998 ), # Common
	( 0x1740 , 0x1753 , 372 ), # Buhid
	( 0x1760 , 0x176c , 373 ), # Tagbanwa
	( 0x176e , 0x1770 , 373 ), # Tagbanwa
	( 0x1772 , 0x1773 , 373 ), # Tagbanwa
	( 0x1780 , 0x17dd , 355 ), # Khmer
	( 0x17e0 , 0x17e9 , 355 ), # Khmer
	( 0x17f0 , 0x17f9 , 355 ), # Khmer
	( 0x1800 , 0x1801 , 145 ), # Mongolian
	( 0x1802 , 0x1803 , 998 ), # Common
	( 0x1804 , 0x1804 , 145 ), # Mongolian
	( 0x1805 , 0x1805 , 998 ), # Common
	( 0x1806 , 0x180e , 145 ), # Mongolian
	( 0x1810 , 0x1819 , 145 ), # Mongolian
	( 0x1820 , 0x1877 , 145 ), # Mongolian
	( 0x1880 , 0x18aa , 145 ), # Mongolian
	( 0x18b0 , 0x18f5 , 440 ), # Canadian_Aboriginal
	( 0x1900 , 0x191e , 336 ), # Limbu
	( 0x1920 , 0x192b , 336 ), # Limbu
	( 0x1930 , 0x193b , 336 ), # Limbu
	( 0x1940 , 0x1940 , 336 ), # Limbu
	( 0x1944 , 0x194f , 336 ), # Limbu
	( 0x1950 , 0x196d , 353 ), # Tai_Le
	( 0x1970 , 0x1974 , 353 ), # Tai_Le
	( 0x1980 , 0x19ab , 354 ), # New_Tai_Lue
	( 0x19b0 , 0x19c9 , 354 ), # New_Tai_Lue
	( 0x19d0 , 0x19da , 354 ), # New_Tai_Lue
	( 0x19de , 0x19df , 354 ), # New_Tai_Lue
	( 0x19e0 , 0x19ff , 355 ), # Khmer
	( 0x1a00 , 0x1a1b , 367 ), # Buginese
	( 0x1a1e , 0x1a1f , 367 ), # Buginese
	( 0x1ab0 , 0x1abe , 994 ), # Inherited
	( 0x1b00 , 0x1b4b , 360 ), # Balinese
	( 0x1b50 , 0x1b7c , 360 ), # Balinese
	( 0x1b80 , 0x1bbf , 362 ), # Sundanese
	( 0x1bc0 , 0x1bf3 , 365 ), # Batak
	( 0x1bfc , 0x1bff , 365 ), # Batak
	( 0x1c00 , 0x1c37 , 335 ), # Lepcha
	( 0x1c3b , 0x1c49 , 335 ), # Lepcha
	( 0x1c4d , 0x1c4f , 335 ), # Lepcha
	( 0x1c50 , 0x1c7f , 261 ), # Ol_Chiki
	( 0x1cc0 , 0x1cc7 , 362 ), # Sundanese
	( 0x1cd0 , 0x1cd2 , 994 ), # Inherited
	( 0x1cd3 , 0x1cd3 , 998 ), # Common
	( 0x1cd4 , 0x1ce0 , 994 ), # Inherited
	( 0x1ce1 , 0x1ce1 , 998 ), # Common
	( 0x1ce2 , 0x1ce8 , 994 ), # Inherited
	( 0x1ce9 , 0x1cec , 998 ), # Common
	( 0x1ced , 0x1ced , 994 ), # Inherited
	( 0x1cee , 0x1cf3 , 998 ), # Common
	( 0x1cf4 , 0x1cf4 , 994 ), # Inherited
	( 0x1cf5 , 0x1cf6 , 998 ), # Common
	( 0x1cf8 , 0x1cf9 , 994 ), # Inherited
	( 0x1d00 , 0x1d25 , 215 ), # Latin
	( 0x1d26 , 0x1d2a , 200 ), # Greek
	( 0x1d2b , 0x1d2b , 220 ), # Cyrillic
	( 0x1d2c , 0x1d5c , 215 ), # Latin
	( 0x1d5d , 0x1d61 , 200 ), # Greek
	( 0x1d62 , 0x1d65 , 215 ), # Latin
	( 0x1d66 , 0x1d6a , 200 ), # Greek
	( 0x1d6b , 0x1d77 , 215 ), # Latin
	( 0x1d78 , 0x1d78 , 220 ), # Cyrillic
	( 0x1d79 , 0x1dbe , 215 ), # Latin
	( 0x1dbf , 0x1dbf , 200 ), # Greek
	( 0x1dc0 , 0x1df5 , 994 ), # Inherited
	( 0x1dfc , 0x1dff , 994 ), # Inherited
	( 0x1e00 , 0x1eff , 215 ), # Latin
	( 0x1f00 , 0x1f15 , 200 ), # Greek
	( 0x1f18 , 0x1f1d , 200 ), # Greek
	( 0x1f20 , 0x1f45 , 200 ), # Greek
	( 0x1f48 , 0x1f4d , 200 ), # Greek
	( 0x1f50 , 0x1f57 , 200 ), # Greek
	( 0x1f59 , 0x1f59 , 200 ), # Greek
	( 0x1f5b , 0x1f5b , 200 ), # Greek
	( 0x1f5d , 0x1f5d , 200 ), # Greek
	( 0x1f5f , 0x1f7d , 200 ), # Greek
	( 0x1f80 , 0x1fb4 , 200 ), # Greek
	( 0x1fb6 , 0x1fc4 , 200 ), # Greek
	( 0x1fc6 , 0x1fd3 , 200 ), # Greek
	( 0x1fd6 , 0x1fdb , 200 ), # Greek
	( 0x1fdd , 0x1fef , 200 ), # Greek
	( 0x1ff2 , 0x1ff4 , 200 ), # Greek
	( 0x1ff6 , 0x1ffe , 200 ), # Greek
	( 0x2000 , 0x200b , 998 ), # Common
	( 0x200c , 0x200d , 994 ), # Inherited
	( 0x200e , 0x2064 , 998 ), # Common
	( 0x2066 , 0x2070 , 998 ), # Common
	( 0x2071 , 0x2071 , 215 ), # Latin
	( 0x2074 , 0x207e , 998 ), # Common
	( 0x207f , 0x207f , 215 ), # Latin
	( 0x2080 , 0x208e , 998 ), # Common
	( 0x2090 , 0x209c , 215 ), # Latin
	( 0x20a0 , 0x20be , 998 ), # Common
	( 0x20d0 , 0x20f0 , 994 ), # Inherited
	( 0x2100 , 0x2125 , 998 ), # Common
	( 0x2126 , 0x2126 , 200 ), # Greek
	( 0x2127 , 0x2129 , 998 ), # Common
	( 0x212a , 0x212b , 215 ), # Latin
	( 0x212c , 0x2131 , 998 ), # Common
	( 0x2132 , 0x2132 , 215 ), # Latin
	( 0x2133 , 0x214d , 998 ), # Common
	( 0x214e , 0x214e , 215 ), # Latin
	( 0x214f , 0x215f , 998 ), # Common
	( 0x2160 , 0x2188 , 215 ), # Latin
	( 0x2189 , 0x218b , 998 ), # Common
	( 0x2190 , 0x23fa , 998 ), # Common
	( 0x2400 , 0x2426 , 998 ), # Common
	( 0x2440 , 0x244a , 998 ), # Common
	( 0x2460 , 0x27ff , 998 ), # Common
	( 0x2800 , 0x28ff , 570 ), # Braille
	( 0x2900 , 0x2b73 , 998 ), # Common
	( 0x2b76 , 0x2b95 , 998 ), # Common
	( 0x2b98 , 0x2bb9 , 998 ), # Common
	( 0x2bbd , 0x2bc8 , 998 ), # Common
	( 0x2bca , 0x2bd1 , 998 ), # Common
	( 0x2bec , 0x2bef , 998 ), # Common
	( 0x2c00 , 0x2c2e , 225 ), # Glagolitic
	( 0x2c30 , 0x2c5e , 225 ), # Glagolitic
	( 0x2c60 , 0x2c7f , 215 ), # Latin
	( 0x2c80 , 0x2cf3 , 204 ), # Coptic
	( 0x2cf9 , 0x2cff , 204 ), # Coptic
	( 0x2d00 , 0x2d25 , 240 ), # Georgian
	( 0x2d27 , 0x2d27 , 240 ), # Georgian
	( 0x2d2d , 0x2d2d , 240 ), # Georgian
	( 0x2d30 , 0x2d67 , 120 ), # Tifinagh
	( 0x2d6f , 0x2d70 , 120 ), # Tifinagh
	( 0x2d7f , 0x2d7f , 120 ), # Tifinagh
	( 0x2d80 , 0x2d96 , 430 ), # Ethiopic
	( 0x2da0 , 0x2da6 , 430 ), # Ethiopic
	( 0x2da8 , 0x2dae , 430 ), # Ethiopic
	( 0x2db0 , 0x2db6 , 430 ), # Ethiopic
	( 0x2db8 , 0x2dbe , 430 ), # Ethiopic
	( 0x2dc0 , 0x2dc6 , 430 ), # Ethiopic
	( 0x2dc8 , 0x2dce , 430 ), # Ethiopic
	( 0x2dd0 , 0x2dd6 , 430 ), # Ethiopic
	( 0x2dd8 , 0x2dde , 430 ), # Ethiopic
	( 0x2de0 , 0x2dff , 220 ), # Cyrillic
	( 0x2e00 , 0x2e42 , 998 ), # Common
	( 0x2e80 , 0x2e99 , 500 ), # Han
	( 0x2e9b , 0x2ef3 , 500 ), # Han
	( 0x2f00 , 0x2fd5 , 500 ), # Han
	( 0x2ff0 , 0x2ffb , 998 ), # Common
	( 0x3000 , 0x3004 , 998 ), # Common
	( 0x3005 , 0x3005 , 500 ), # Han
	( 0x3006 , 0x3006 , 998 ), # Common
	( 0x3007 , 0x3007 , 500 ), # Han
	( 0x3008 , 0x3020 , 998 ), # Common
	( 0x3021 , 0x3029 , 500 ), # Han
	( 0x302a , 0x302d , 994 ), # Inherited
	( 0x302e , 0x302f , 286 ), # Hangul
	( 0x3030 , 0x3037 , 998 ), # Common
	( 0x3038 , 0x303b , 500 ), # Han
	( 0x303c , 0x303f , 998 ), # Common
	( 0x3041 , 0x3096 , 410 ), # Hiragana
	( 0x3099 , 0x309a , 994 ), # Inherited
	( 0x309b , 0x309c , 998 ), # Common
	( 0x309d , 0x309f , 410 ), # Hiragana
	( 0x30a0 , 0x30a0 , 998 ), # Common
	( 0x30a1 , 0x30fa , 411 ), # Katakana
	( 0x30fb , 0x30fc , 998 ), # Common
	( 0x30fd , 0x30ff , 411 ), # Katakana
	( 0x3105 , 0x312d , 285 ), # Bopomofo
	( 0x3131 , 0x318e , 286 ), # Hangul
	( 0x3190 , 0x319f , 998 ), # Common
	( 0x31a0 , 0x31ba , 285 ), # Bopomofo
	( 0x31c0 , 0x31e3 , 998 ), # Common
	( 0x31f0 , 0x31ff , 411 ), # Katakana
	( 0x3200 , 0x321e , 286 ), # Hangul
	( 0x3220 , 0x325f , 998 ), # Common
	( 0x3260 , 0x327e , 286 ), # Hangul
	( 0x327f , 0x32cf , 998 ), # Common
	( 0x32d0 , 0x32fe , 411 ), # Katakana
	( 0x3300 , 0x3357 , 411 ), # Katakana
	( 0x3358 , 0x33ff , 998 ), # Common
	( 0x3400 , 0x4db5 , 500 ), # Han
	( 0x4dc0 , 0x4dff , 998 ), # Common
	( 0x4e00 , 0x9fd5 , 500 ), # Han
	( 0xa000 , 0xa48c , 460 ), # Yi
	( 0xa490 , 0xa4c6 , 460 ), # Yi
	( 0xa4d0 , 0xa4ff , 399 ), # Lisu
	( 0xa500 , 0xa62b , 470 ), # Vai
	( 0xa640 , 0xa69f , 220 ), # Cyrillic
	( 0xa6a0 , 0xa6f7 , 435 ), # Bamum
	( 0xa700 , 0xa721 , 998 ), # Common
	( 0xa722 , 0xa787 , 215 ), # Latin
	( 0xa788 , 0xa78a , 998 ), # Common
	( 0xa78b , 0xa7ad , 215 ), # Latin
	( 0xa7b0 , 0xa7b7 , 215 ), # Latin
	( 0xa7f7 , 0xa7ff , 215 ), # Latin
	( 0xa800 , 0xa82b , 316 ), # Syloti_Nagri
	( 0xa830 , 0xa839 , 998 ), # Common
	( 0xa840 , 0xa877 , 331 ), # Phags_Pa
	( 0xa880 , 0xa8c4 , 344 ), # Saurashtra
	( 0xa8ce , 0xa8d9 , 344 ), # Saurashtra
	( 0xa8e0 , 0xa8fd , 315 ), # Devanagari
	( 0xa900 , 0xa92d , 357 ), # Kayah_Li
	( 0xa92e , 0xa92e , 998 ), # Common
	( 0xa92f , 0xa92f , 357 ), # Kayah_Li
	( 0xa930 , 0xa953 , 363 ), # Rejang
	( 0xa95f , 0xa95f , 363 ), # Rejang
	( 0xa960 , 0xa97c , 286 ), # Hangul
	( 0xa980 , 0xa9cd , 361 ), # Javanese
	( 0xa9cf , 0xa9cf , 998 ), # Common
	( 0xa9d0 , 0xa9d9 , 361 ), # Javanese
	( 0xa9de , 0xa9df , 361 ), # Javanese
	( 0xa9e0 , 0xa9fe , 350 ), # Myanmar
	( 0xaa00 , 0xaa36 , 358 ), # Cham
	( 0xaa40 , 0xaa4d , 358 ), # Cham
	( 0xaa50 , 0xaa59 , 358 ), # Cham
	( 0xaa5c , 0xaa5f , 358 ), # Cham
	( 0xaa60 , 0xaa7f , 350 ), # Myanmar
	( 0xaa80 , 0xaac2 , 359 ), # Tai_Viet
	( 0xaadb , 0xaadf , 359 ), # Tai_Viet
	( 0xaae0 , 0xaaf6 , 337 ), # Meetei_Mayek
	( 0xab01 , 0xab06 , 430 ), # Ethiopic
	( 0xab09 , 0xab0e , 430 ), # Ethiopic
	( 0xab11 , 0xab16 , 430 ), # Ethiopic
	( 0xab20 , 0xab26 , 430 ), # Ethiopic
	( 0xab28 , 0xab2e , 430 ), # Ethiopic
	( 0xab30 , 0xab5a , 215 ), # Latin
	( 0xab5b , 0xab5b , 998 ), # Common
	( 0xab5c , 0xab64 , 215 ), # Latin
	( 0xab65 , 0xab65 , 200 ), # Greek
	( 0xab70 , 0xabbf , 445 ), # Cherokee
	( 0xabc0 , 0xabed , 337 ), # Meetei_Mayek
	( 0xabf0 , 0xabf9 , 337 ), # Meetei_Mayek
	( 0xac00 , 0xd7a3 , 286 ), # Hangul
	( 0xd7b0 , 0xd7c6 , 286 ), # Hangul
	( 0xd7cb , 0xd7fb , 286 ), # Hangul
	( 0xf900 , 0xfa6d , 500 ), # Han
	( 0xfa70 , 0xfad9 , 500 ), # Han
	( 0xfb00 , 0xfb06 , 215 ), # Latin
	( 0xfb13 , 0xfb17 , 230 ), # Armenian
	( 0xfb1d , 0xfb36 , 125 ), # Hebrew
	( 0xfb38 , 0xfb3c , 125 ), # Hebrew
	( 0xfb3e , 0xfb3e , 125 ), # Hebrew
	( 0xfb40 , 0xfb41 , 125 ), # Hebrew
	( 0xfb43 , 0xfb44 , 125 ), # Hebrew
	( 0xfb46 , 0xfb4f , 125 ), # Hebrew
	( 0xfb50 , 0xfbc1 , 160 ), # Arabic
	( 0xfbd3 , 0xfd3d , 160 ), # Arabic
	( 0xfd3e , 0xfd3f , 998 ), # Common
	( 0xfd50 , 0xfd8f , 160 ), # Arabic
	( 0xfd92 , 0xfdc7 , 160 ), # Arabic
	( 0xfdf0 , 0xfdfd , 160 ), # Arabic
	( 0xfe00 , 0xfe0f , 994 ), # Inherited
	( 0xfe10 , 0xfe19 , 998 ), # Common
	( 0xfe20 , 0xfe2d , 994 ), # Inherited
	( 0xfe2e , 0xfe2f , 220 ), # Cyrillic
	( 0xfe30 , 0xfe52 , 998 ), # Common
	( 0xfe54 , 0xfe66 , 998 ), # Common
	( 0xfe68 , 0xfe6b , 998 ), # Common
	( 0xfe70 , 0xfe74 , 160 ), # Arabic
	( 0xfe76 , 0xfefc , 160 ), # Arabic
	( 0xfeff , 0xfeff , 998 ), # Common
	( 0xff01 , 0xff20 , 998 ), # Common
	( 0xff21 , 0xff3a , 215 ), # Latin
	( 0xff3b , 0xff40 , 998 ), # Common
	( 0xff41 , 0xff5a , 215 ), # Latin
	( 0xff5b , 0xff65 , 998 ), # Common
	( 0xff66 , 0xff6f , 411 ), # Katakana
	( 0xff70 , 0xff70 , 998 ), # Common
	( 0xff71 , 0xff9d , 411 ), # Katakana
	( 0xff9e , 0xff9f , 998 ), # Common
	( 0xffa0 , 0xffbe , 286 ), # Hangul
	( 0xffc2 , 0xffc7 , 286 ), # Hangul
	( 0xffca , 0xffcf , 286 ), # Hangul
	( 0xffd2 , 0xffd7 , 286 ), # Hangul
	( 0xffda , 0xffdc , 286 ), # Hangul
	( 0xffe0 , 0xffe6 , 998 ), # Common
	( 0xffe8 , 0xffee , 998 ), # Common
	( 0xfff9 , 0xfffd , 998 ), # Common
	( 0x10000 , 0x1000b , 401 ), # Linear_B
	( 0x1000d , 0x10026 , 401 ), # Linear_B
	( 0x10028 , 0x1003a , 401 ), # Linear_B
	( 0x1003c , 0x1003d , 401 ), # Linear_B
	( 0x1003f , 0x1004d , 401 ), # Linear_B
	( 0x10050 , 0x1005d , 401 ), # Linear_B
	( 0x10080 , 0x100fa , 401 ), # Linear_B
	( 0x10100 , 0x10102 , 998 ), # Common
	( 0x10107 , 0x10133 , 998 ), # Common
	( 0x10137 , 0x1013f , 998 ), # Common
	( 0x10140 , 0x1018c , 200 ), # Greek
	( 0x10190 , 0x1019b , 998 ), # Common
	( 0x101a0 , 0x101a0 , 200 ), # Greek
	( 0x101d0 , 0x101fc , 998 ), # Common
	( 0x101fd , 0x101fd , 994 ), # Inherited
	( 0x10280 , 0x1029c , 202 ), # Lycian
	( 0x102a0 , 0x102d0 , 201 ), # Carian
	( 0x102e0 , 0x102e0 , 994 ), # Inherited
	( 0x102e1 , 0x102fb , 998 ), # Common
	( 0x10300 , 0x10323 , 210 ), # Old_Italic
	( 0x10330 , 0x1034a , 206 ), # Gothic
	( 0x10350 , 0x1037a , 227 ), # Old_Permic
	( 0x10380 , 0x1039d , 40 ), # Ugaritic
	( 0x1039f , 0x1039f , 40 ), # Ugaritic
	( 0x103a0 , 0x103c3 , 30 ), # Old_Persian
	( 0x103c8 , 0x103d5 , 30 ), # Old_Persian
	( 0x10400 , 0x1044f , 250 ), # Deseret
	( 0x10450 , 0x1047f , 281 ), # Shavian
	( 0x10480 , 0x1049d , 260 ), # Osmanya
	( 0x104a0 , 0x104a9 , 260 ), # Osmanya
	( 0x10500 , 0x10527 , 226 ), # Elbasan
	( 0x10530 , 0x10563 , 239 ), # Caucasian_Albanian
	( 0x1056f , 0x1056f , 239 ), # Caucasian_Albanian
	( 0x10600 , 0x10736 , 400 ), # Linear_A
	( 0x10740 , 0x10755 , 400 ), # Linear_A
	( 0x10760 , 0x10767 , 400 ), # Linear_A
	( 0x10800 , 0x10805 , 403 ), # Cypriot
	( 0x10808 , 0x10808 , 403 ), # Cypriot
	( 0x1080a , 0x10835 , 403 ), # Cypriot
	( 0x10837 , 0x10838 , 403 ), # Cypriot
	( 0x1083c , 0x1083c , 403 ), # Cypriot
	( 0x1083f , 0x1083f , 403 ), # Cypriot
	( 0x10840 , 0x10855 , 124 ), # Imperial_Aramaic
	( 0x10857 , 0x1085f , 124 ), # Imperial_Aramaic
	( 0x10860 , 0x1087f , 126 ), # Palmyrene
	( 0x10880 , 0x1089e , 159 ), # Nabataean
	( 0x108a7 , 0x108af , 159 ), # Nabataean
	( 0x10900 , 0x1091b , 115 ), # Phoenician
	( 0x1091f , 0x1091f , 115 ), # Phoenician
	( 0x10920 , 0x10939 , 116 ), # Lydian
	( 0x1093f , 0x1093f , 116 ), # Lydian
	( 0x10980 , 0x1099f , 100 ), # Meroitic_Hieroglyphs
	( 0x109a0 , 0x109b7 , 101 ), # Meroitic_Cursive
	( 0x109bc , 0x109cf , 101 ), # Meroitic_Cursive
	( 0x109d2 , 0x109ff , 101 ), # Meroitic_Cursive
	( 0x10a00 , 0x10a03 , 305 ), # Kharoshthi
	( 0x10a05 , 0x10a06 , 305 ), # Kharoshthi
	( 0x10a0c , 0x10a13 , 305 ), # Kharoshthi
	( 0x10a15 , 0x10a17 , 305 ), # Kharoshthi
	( 0x10a19 , 0x10a33 , 305 ), # Kharoshthi
	( 0x10a38 , 0x10a3a , 305 ), # Kharoshthi
	( 0x10a3f , 0x10a47 , 305 ), # Kharoshthi
	( 0x10a50 , 0x10a58 , 305 ), # Kharoshthi
	( 0x10a60 , 0x10a7f , 105 ), # Old_South_Arabian
	( 0x10a80 , 0x10a9f , 106 ), # Old_North_Arabian
	( 0x10ac0 , 0x10ae6 , 139 ), # Manichaean
	( 0x10aeb , 0x10af6 , 139 ), # Manichaean
	( 0x10b00 , 0x10b35 , 134 ), # Avestan
	( 0x10b39 , 0x10b3f , 134 ), # Avestan
	( 0x10b40 , 0x10b55 , 130 ), # Inscriptional_Parthian
	( 0x10b58 , 0x10b5f , 130 ), # Inscriptional_Parthian
	( 0x10b60 , 0x10b72 , 131 ), # Inscriptional_Pahlavi
	( 0x10b78 , 0x10b7f , 131 ), # Inscriptional_Pahlavi
	( 0x10b80 , 0x10b91 , 132 ), # Psalter_Pahlavi
	( 0x10b99 , 0x10b9c , 132 ), # Psalter_Pahlavi
	( 0x10ba9 , 0x10baf , 132 ), # Psalter_Pahlavi
	( 0x10c00 , 0x10c48 , 175 ), # Old_Turkic
	( 0x10e60 , 0x10e7e , 160 ), # Arabic
	( 0x11000 , 0x1104d , 300 ), # Brahmi
	( 0x11052 , 0x1106f , 300 ), # Brahmi
	( 0x1107f , 0x1107f , 300 ), # Brahmi
	( 0x11080 , 0x110c1 , 317 ), # Kaithi
	( 0x110d0 , 0x110e8 , 398 ), # Sora_Sompeng
	( 0x110f0 , 0x110f9 , 398 ), # Sora_Sompeng
	( 0x11100 , 0x11134 , 349 ), # Chakma
	( 0x11136 , 0x11143 , 349 ), # Chakma
	( 0x11150 , 0x11176 , 314 ), # Mahajani
	( 0x11180 , 0x111cd , 319 ), # Sharada
	( 0x111d0 , 0x111df , 319 ), # Sharada
	( 0x111e1 , 0x111f4 , 348 ), # Sinhala
	( 0x11200 , 0x11211 , 322 ), # Khojki
	( 0x11213 , 0x1123d , 322 ), # Khojki
	( 0x11280 , 0x11286 , 323 ), # Multani
	( 0x11288 , 0x11288 , 323 ), # Multani
	( 0x1128a , 0x1128d , 323 ), # Multani
	( 0x1128f , 0x1129d , 323 ), # Multani
	( 0x1129f , 0x112a9 , 323 ), # Multani
	( 0x112b0 , 0x112ea , 318 ), # Khudawadi
	( 0x112f0 , 0x112f9 , 318 ), # Khudawadi
	( 0x11300 , 0x11303 , 343 ), # Grantha
	( 0x11305 , 0x1130c , 343 ), # Grantha
	( 0x1130f , 0x11310 , 343 ), # Grantha
	( 0x11313 , 0x11328 , 343 ), # Grantha
	( 0x1132a , 0x11330 , 343 ), # Grantha
	( 0x11332 , 0x11333 , 343 ), # Grantha
	( 0x11335 , 0x11339 , 343 ), # Grantha
	( 0x1133c , 0x11344 , 343 ), # Grantha
	( 0x11347 , 0x11348 , 343 ), # Grantha
	( 0x1134b , 0x1134d , 343 ), # Grantha
	( 0x11350 , 0x11350 , 343 ), # Grantha
	( 0x11357 , 0x11357 , 343 ), # Grantha
	( 0x1135d , 0x11363 , 343 ), # Grantha
	( 0x11366 , 0x1136c , 343 ), # Grantha
	( 0x11370 , 0x11374 , 343 ), # Grantha
	( 0x11480 , 0x114c7 , 326 ), # Tirhuta
	( 0x114d0 , 0x114d9 , 326 ), # Tirhuta
	( 0x11580 , 0x115b5 , 302 ), # Siddham
	( 0x115b8 , 0x115dd , 302 ), # Siddham
	( 0x11600 , 0x11644 , 324 ), # Modi
	( 0x11650 , 0x11659 , 324 ), # Modi
	( 0x11680 , 0x116b7 , 321 ), # Takri
	( 0x116c0 , 0x116c9 , 321 ), # Takri
	( 0x118a0 , 0x118f2 , 262 ), # Warang_Citi
	( 0x118ff , 0x118ff , 262 ), # Warang_Citi
	( 0x11ac0 , 0x11af8 , 263 ), # Pau_Cin_Hau
	( 0x12000 , 0x12399 , 20 ), # Cuneiform
	( 0x12400 , 0x1246e , 20 ), # Cuneiform
	( 0x12470 , 0x12474 , 20 ), # Cuneiform
	( 0x12480 , 0x12543 , 20 ), # Cuneiform
	( 0x13000 , 0x1342e , 50 ), # Egyptian_Hieroglyphs
	( 0x16800 , 0x16a38 , 435 ), # Bamum
	( 0x16a40 , 0x16a5e , 199 ), # Mro
	( 0x16a60 , 0x16a69 , 199 ), # Mro
	( 0x16a6e , 0x16a6f , 199 ), # Mro
	( 0x16ad0 , 0x16aed , 259 ), # Bassa_Vah
	( 0x16af0 , 0x16af5 , 259 ), # Bassa_Vah
	( 0x16b00 , 0x16b45 , 450 ), # Pahawh_Hmong
	( 0x16b50 , 0x16b59 , 450 ), # Pahawh_Hmong
	( 0x16b5b , 0x16b61 , 450 ), # Pahawh_Hmong
	( 0x16b63 , 0x16b77 , 450 ), # Pahawh_Hmong
	( 0x16b7d , 0x16b8f , 450 ), # Pahawh_Hmong
	( 0x16f00 , 0x16f44 , 282 ), # Miao
	( 0x16f50 , 0x16f7e , 282 ), # Miao
	( 0x16f8f , 0x16f9f , 282 ), # Miao
	( 0x1b000 , 0x1b000 , 411 ), # Katakana
	( 0x1b001 , 0x1b001 , 410 ), # Hiragana
	( 0x1bc00 , 0x1bc6a , 755 ), # Duployan
	( 0x1bc70 , 0x1bc7c , 755 ), # Duployan
	( 0x1bc80 , 0x1bc88 , 755 ), # Duployan
	( 0x1bc90 , 0x1bc99 , 755 ), # Duployan
	( 0x1bc9c , 0x1bc9f , 755 ), # Duployan
	( 0x1bca0 , 0x1bca3 , 998 ), # Common
	( 0x1d000 , 0x1d0f5 , 998 ), # Common
	( 0x1d100 , 0x1d126 , 998 ), # Common
	( 0x1d129 , 0x1d166 , 998 ), # Common
	( 0x1d167 , 0x1d169 , 994 ), # Inherited
	( 0x1d16a , 0x1d17a , 998 ), # Common
	( 0x1d17b , 0x1d182 , 994 ), # Inherited
	( 0x1d183 , 0x1d184 , 998 ), # Common
	( 0x1d185 , 0x1d18b , 994 ), # Inherited
	( 0x1d18c , 0x1d1a9 , 998 ), # Common
	( 0x1d1aa , 0x1d1ad , 994 ), # Inherited
	( 0x1d1ae , 0x1d1e8 , 998 ), # Common
	( 0x1d200 , 0x1d245 , 200 ), # Greek
	( 0x1d300 , 0x1d356 , 998 ), # Common
	( 0x1d360 , 0x1d371 , 998 ), # Common
	( 0x1d400 , 0x1d454 , 998 ), # Common
	( 0x1d456 , 0x1d49c , 998 ), # Common
	( 0x1d49e , 0x1d49f , 998 ), # Common
	( 0x1d4a2 , 0x1d4a2 , 998 ), # Common
	( 0x1d4a5 , 0x1d4a6 , 998 ), # Common
	( 0x1d4a9 , 0x1d4ac , 998 ), # Common
	( 0x1d4ae , 0x1d4b9 , 998 ), # Common
	( 0x1d4bb , 0x1d4bb , 998 ), # Common
	( 0x1d4bd , 0x1d4c3 , 998 ), # Common
	( 0x1d4c5 , 0x1d505 , 998 ), # Common
	( 0x1d507 , 0x1d50a , 998 ), # Common
	( 0x1d50d , 0x1d514 , 998 ), # Common
	( 0x1d516 , 0x1d51c , 998 ), # Common
	( 0x1d51e , 0x1d539 , 998 ), # Common
	( 0x1d53b , 0x1d53e , 998 ), # Common
	( 0x1d540 , 0x1d544 , 998 ), # Common
	( 0x1d546 , 0x1d546 , 998 ), # Common
	( 0x1d54a , 0x1d550 , 998 ), # Common
	( 0x1d552 , 0x1d6a5 , 998 ), # Common
	( 0x1d6a8 , 0x1d7cb , 998 ), # Common
	( 0x1d7ce , 0x1d7ff , 998 ), # Common
	( 0x1e800 , 0x1e8c4 , 438 ), # Mende_Kikakui
	( 0x1e8c7 , 0x1e8d6 , 438 ), # Mende_Kikakui
	( 0x1ee00 , 0x1ee03 , 160 ), # Arabic
	( 0x1ee05 , 0x1ee1f , 160 ), # Arabic
	( 0x1ee21 , 0x1ee22 , 160 ), # Arabic
	( 0x1ee24 , 0x1ee24 , 160 ), # Arabic
	( 0x1ee27 , 0x1ee27 , 160 ), # Arabic
	( 0x1ee29 , 0x1ee32 , 160 ), # Arabic
	( 0x1ee34 , 0x1ee37 , 160 ), # Arabic
	( 0x1ee39 , 0x1ee39 , 160 ), # Arabic
	( 0x1ee3b , 0x1ee3b , 160 ), # Arabic
	( 0x1ee42 , 0x1ee42 , 160 ), # Arabic
	( 0x1ee47 , 0x1ee47 , 160 ), # Arabic
	( 0x1ee49 , 0x1ee49 , 160 ), # Arabic
	( 0x1ee4b , 0x1ee4b , 160 ), # Arabic
	( 0x1ee4d , 0x1ee4f , 160 ), # Arabic
	( 0x1ee51 , 0x1ee52 , 160 ), # Arabic
	( 0x1ee54 , 0x1ee54 , 160 ), # Arabic
	( 0x1ee57 , 0x1ee57 , 160 ), # Arabic
	( 0x1ee59 , 0x1ee59 , 160 ), # Arabic
	( 0x1ee5b , 0x1ee5b , 160 ), # Arabic
	( 0x1ee5d , 0x1ee5d , 160 ), # Arabic
	( 0x1ee5f , 0x1ee5f , 160 ), # Arabic
	( 0x1ee61 , 0x1ee62 , 160 ), # Arabic
	( 0x1ee64 , 0x1ee64 , 160 ), # Arabic
	( 0x1ee67 , 0x1ee6a , 160 ), # Arabic
	( 0x1ee6c , 0x1ee72 , 160 ), # Arabic
	( 0x1ee74 , 0x1ee77 , 160 ), # Arabic
	( 0x1ee79 , 0x1ee7c , 160 ), # Arabic
	( 0x1ee7e , 0x1ee7e , 160 ), # Arabic
	( 0x1ee80 , 0x1ee89 , 160 ), # Arabic
	( 0x1ee8b , 0x1ee9b , 160 ), # Arabic
	( 0x1eea1 , 0x1eea3 , 160 ), # Arabic
	( 0x1eea5 , 0x1eea9 , 160 ), # Arabic
	( 0x1eeab , 0x1eebb , 160 ), # Arabic
	( 0x1eef0 , 0x1eef1 , 160 ), # Arabic
	( 0x1f000 , 0x1f02b , 998 ), # Common
	( 0x1f030 , 0x1f093 , 998 ), # Common
	( 0x1f0a0 , 0x1f0ae , 998 ), # Common
	( 0x1f0b1 , 0x1f0bf , 998 ), # Common
	( 0x1f0c1 , 0x1f0cf , 998 ), # Common
	( 0x1f0d1 , 0x1f0f5 , 998 ), # Common
	( 0x1f100 , 0x1f10c , 998 ), # Common
	( 0x1f110 , 0x1f12e , 998 ), # Common
	( 0x1f130 , 0x1f16b , 998 ), # Common
	( 0x1f170 , 0x1f19a , 998 ), # Common
	( 0x1f1e6 , 0x1f1ff , 998 ), # Common
	( 0x1f200 , 0x1f200 , 410 ), # Hiragana
	( 0x1f201 , 0x1f202 , 998 ), # Common
	( 0x1f210 , 0x1f23a , 998 ), # Common
	( 0x1f240 , 0x1f248 , 998 ), # Common
	( 0x1f250 , 0x1f251 , 998 ), # Common
	( 0x1f300 , 0x1f579 , 998 ), # Common
	( 0x1f57b , 0x1f5a3 , 998 ), # Common
	( 0x1f5a5 , 0x1f6d0 , 998 ), # Common
	( 0x1f6e0 , 0x1f6ec , 998 ), # Common
	( 0x1f6f0 , 0x1f6f3 , 998 ), # Common
	( 0x1f700 , 0x1f773 , 998 ), # Common
	( 0x1f780 , 0x1f7d4 , 998 ), # Common
	( 0x1f800 , 0x1f80b , 998 ), # Common
	( 0x1f810 , 0x1f847 , 998 ), # Common
	( 0x1f850 , 0x1f859 , 998 ), # Common
	( 0x1f860 , 0x1f887 , 998 ), # Common
	( 0x1f890 , 0x1f8ad , 998 ), # Common
	( 0x1f910 , 0x1f918 , 998 ), # Common
	( 0x1f980 , 0x1f984 , 998 ), # Common
	( 0x1f9c0 , 0x1f9c0 , 998 ), # Common
	( 0x20000 , 0x2a6d6 , 500 ), # Han
	( 0x2a700 , 0x2b734 , 500 ), # Han
	( 0x2b740 , 0x2b81d , 500 ), # Han
	( 0x2b820 , 0x2cea1 , 500 ), # Han
	( 0x2f800 , 0x2fa1d , 500 ), # Han
	( 0xe0001 , 0xe0001 , 998 ), # Common
	( 0xe0020 , 0xe007f , 998 ), # Common
]
