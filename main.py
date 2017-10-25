from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, sublinear_tf, augmented_tf, idf, tfidf


# Input the Personality Name
name = input("Enter the Name of Personality\n")

# Get link
pageLink = linkify(name)

wordList = getWords(pageLink)
#print(wordsList)
linkList = getLinks(pageLink)
#print(newList)

tfDict = tf(wordList)
#sub_tfDict = sublinear_tf(wordList)
#aug_tfDict = augmented_tf(wordList)

docLinks = getDocLinkStrength(linkList, tfDict)

links_for_tf_idf = []
for each in docLinks:
	temp = each[0]
	if temp not in links_for_tf_idf:
		links_for_tf_idf.append(temp)

#print(links_for_tf_idf[:10])

dump = []
for each in links_for_tf_idf[:10]:
	tempLink = linkify(each)
	dump.append(getWords(tempLink))


idfDict = {}
idfDict = idf(tfDict, dump)

tfidfDict = {}
tfidfDict = tfidf(tfDict, idfDict)

tfidfList = []
for each in tfidfDict:
	tfidfList.append((each, tfidfDict[each]))
tfidfList.sort(key = lambda x:x[1], reverse = True)

keywords = getDocLinkStrength(linkList, tfidfDict)
finalKeywordList = []
#count = 0
for each in keywords:
	temp = each[0]
	if temp not in finalKeywordList:
		#count += 1
		finalKeywordList.append(temp)
	#if count == 6:
		#break

for each in finalKeywordList:
	print(each)