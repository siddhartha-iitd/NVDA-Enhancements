
from unicodeScriptHandler import *

def _compile_scripts_txt():
    # build indexes from 'scripts.txt'

	unicodeRange= []



	import urllib2, re, textwrap

	url = 'http://www.unicode.org/Public/UNIDATA/Scripts.txt'
	f = urllib2.urlopen(url)
	for ln in f:
		p = re.findall(r'([0-9A-F]+)(?:\.\.([0-9A-F]+))?\W+(\w+)\s*#\s*(\w+)', ln)
		if p:
			a, b, name, cat = p[0]
			if name in unicodeScriptNamesToISO15924Dictionary.keys():
				tempScriptCode = unicodeScriptNamesToISO15924Dictionary[name]
				unicodeRange.append((int(a, 16), int(b or a, 16), tempScriptCode , name ))
	unicodeRange.sort()

	unicodeRange = normalize(unicodeRange )

	print 'scriptCode= [\n%s\n]' % (
		'\n'.join('\t( 0x%x , 0x%x , %d ), # %s' % c for c in unicodeRange) )        

def normalize(unicodeRanges):
	normalizedRange= []
	lastRecord = unicodeRanges[0] 
	for index in xrange(1, len( unicodeRanges) ) :
		if lastRecord: 
			tempRecord = unicodeRanges[index] 
			if lastRecord[2] == tempRecord[2] and (lastRecord[1] + 1) == tempRecord[0]: 
				lastRecord = lastRecord[0] , tempRecord[1] , tempRecord[2] , tempRecord[3]
			else:
				normalizedRange.append(lastRecord) 
				lastRecord = tempRecord

	return normalizedRange


_compile_scripts_txt()
#profile.run("for i in range(0,100000): getScriptIDFromLangID('en')")


#print "script {}".format( getScriptIDFromLangID('hi'))
#print "langID: {}".format(getLangID(215))