from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength


# Input the Personality Name
#name = input("Enter the Name of Personality\n")
name = "Nolan Bushnell"
# Get link
pageLink = linkify(name)

wordList = getWords(pageLink)
#print(wordsList)
linkList = getLinks(pageLink)
#print(newList)

tfDict = tf(wordList)
docLinks = getDocLinkStrength(linkList, tfDict)

links_for_tf_idf = []
for each in docLinks:
	temp = each[0]
	if temp not in links_for_tf_idf:
		links_for_tf_idf.append(temp)

print(links_for_tf_idf[:10])

dump = {}
for each in links_for_tf_idf[:10]:
	tempLink = linkify(each)
	dump[each] = getWords(tempLink)

for each in dump:
	print(each)