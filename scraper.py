''' 
		A code to retrieve links and sort it in TF IDF
		Author: AB
		Date: 18October2017
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import string
from urllib.parse import unquote

def cleanupLatinEncoding(word):
    try:
        return unquote(word, errors='strict')
    except UnicodeDecodeError:
        return unquote(word, encoding='latin-1')

def cleanupHex(word):
    try:
        return unquote(word, errors='strict')
    except UnicodeDecodeError:
        return unquote(word, encoding='hex')

def getWords(url):
	html = urlopen("https://en.wikipedia.org"+url)
	bsObj = BeautifulSoup(html, "lxml")
	text = bsObj.findAll("div", {"id":"mw-content-text"})
	cleanInput = []
	for each in text:
		each = each.get_text()
		each = cleanupLatinEncoding(each)
		each = re.sub('\n+', " ", each)
		each = re.sub('\[[0-9]*\]', "", each)
		each = re.sub(' +', " ", each)
		each = each.split(' ')
		for item in each:
			if '\xa0' in item:
				item = re.sub('\xa0', " ", item)
			item = item.strip(string.punctuation)
			if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
				cleanInput.append(item)
	return cleanInput

# A function to get urls within the page
def getLinks(url):
	# Append the url tag to wiki
	html = urlopen("https://en.wikipedia.org"+url)
	bsObj = BeautifulSoup(html, "lxml")
	newLinks = list()
	# The url tags are always i) found in bodycontent tag
	for each in bsObj.findAll("div", {"id": "bodyContent"}):
		#print(each)
		# ii) start with /wiki/
		# and iii) do not contain semicolons
		for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
			#print(link)
			if 'href' in link.attrs:
				#print(link)
				stripped = re.sub('/wiki/', "", link.attrs['href'])
				stripped = re.sub('_', " ", stripped)
				stripped = cleanupLatinEncoding(stripped)
				newLinks.append(stripped)
	# return a list containing all the links
	return newLinks


# A function to create the link in parsable format
def linkify(s):
	starting = '/wiki/'
	tokens = s.split(" ")
	for i in range(0, len(tokens)):
		# To append the underscore
		if i != 0:
			starting = starting + '_'
		# To append the words
		starting = starting+tokens[i]
	return starting