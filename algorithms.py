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
	tfDict = {}
	countDict = {}
	tfList = []
	for eachWord in wordList:
		if eachWord in countDict:
			countDict[eachWord] += 1
		else:
			countDict[eachWord] = 1
	numOfTerms = len(wordList)
	maximumCount = 0
	for eachWord in countDict:
		tfDict[eachWord] = countDict[eachWord]/numOfTerms
	#for each in tfDict:
	#	tfList.append((each, tfDict[each]))
	#tfList.sort(key = lambda x:x[1], reverse = True)
	return tfDict