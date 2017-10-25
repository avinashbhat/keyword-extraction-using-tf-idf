import math

def getDocLinkStrength(linkList, tfDict):
	linkStrength = []
	for each in linkList:
		strength = 0
		temp = each.split(" ")
		j = 1
		i = len(tfDict)
		for word in temp:
			if word in tfDict:
				strength += tfDict[word]*i
			i -= 2**j
			if i <= 0:
				break
			j += 1
		strength = strength/len(temp)
		linkStrength.append((each, strength))
	linkStrength.sort(key = lambda x:x[1], reverse = True)
	return linkStrength

def tf(wordList):
	#tfDict = {}
	countDict = {}
	#tfList = []
	for eachWord in wordList:
		if eachWord in countDict:
			countDict[eachWord] += 1
		else:
			countDict[eachWord] = 1
	#numOfTerms = len(wordList)
	#maximumCount = 0
	#for eachWord in countDict:
	#	tfDict[eachWord] = countDict[eachWord]/numOfTerms
	#for each in tfDict:
	#	tfList.append((each, tfDict[each]))
	#tfList.sort(key = lambda x:x[1], reverse = True)
	return countDict

def sublinear_tf(wordList):
	countDict = {}
	sub_tfDict = {}
	for eachWord in wordList:
		if eachWord in countDict:
			countDict[eachWord] += 1
		else:
			countDict[eachWord] = 1
	for each in countDict:
		sub_tfDict[each] = 1 + math.log(countDict[each])
	return sub_tfDict

def augmented_tf(wordList):
	max_count = 0
	aug_tfDict = {}
	countDict = {}
	for eachWord in wordList:
		if eachWord in countDict:
			countDict[eachWord] += 1
		else:
			countDict[eachWord] = 1
	for eachWord in countDict:
		if countDict[eachWord] > max_count:
			max_count = countDict[eachWord]
	for eachWord in countDict:
		aug_tfDict[eachWord] = (0.5 + ((0.5 * countDict[eachWord]) / max_count))
	return aug_tfDict

def idf(tfDict, dump):
	idfDict = {}
	for each in tfDict:
		count = 0
		for i in range(0, 10):
			if each in dump[i]:
				count += 1
		idfDict[each] = math.log(10/(1+count))
	return idfDict

def tfidf(tfDict, idfDict):
	tfidfDict = {}
	for each in tfDict:
		tfidfDict[each] = tfDict[each]*idfDict[each]
	return tfidfDict