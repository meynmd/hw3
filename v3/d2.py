#!/bin/python

import numpy
import vit

def readfile(fname):
	data = []
	with open(fname, 'r') as fp:
		for line in fp.readlines():
			data.append(line)
	return data

def getprob(lexicon, trigram):
	lexSize = len(lexicon)
	triSize = len(trigram)
	states = []
	words = []

	# map symbols to indices
	triDict = {}
	count = 0
	for line in trigram:
		line = line.split()
		s = line[0].strip()
		if s not in triDict:
			triDict[s] = count
			states.append(s)
			count += 1

		s = line[3].strip()
		if s not in triDict:
			triDict[s] = count
			states.append(s)
			count += 1
	
	lexDict = {}
	count = 0
	for line in lexicon:
		line = line.split(':')
		line = line[1]
		line = line.split('#')
		sym = line[0].strip()
		if sym not in lexDict:
			lexDict[sym] = count
			words.append( sym )
			count += 1
	lexDict['<s>'] = count
	words.append('<s>')
	lexDict['</s>'] = count + 1
	words.append('</s>')
	

	#for k, v in lexDict.items():
	#	print '{0} : {1}'.format(k, v)
	
	# retrieve probability data
	triMat = numpy.zeros((len(states), len(states), len(states)))
	for line in trigram:
		line = line.split()
		idx1 = triDict[line[0]]
		idx2 = triDict[line[1]]
		idx3 = triDict[line[3]]
		triMat[idx1, idx2, idx3] = line[5]

	lexMat = numpy.zeros((len(words), len(states)))
	for line in lexicon:
		line = line.split(':')
		s = line[0].strip()
		if s == 'PAUSE':
			continue
		sIdx = triDict[s]
		ws = line[1].split('#')
		ws = ws[0].strip()
		wIdx = lexDict[ws]
		lexMat[wIdx, sIdx] = line[1].split('#')[1]
		
	return words, states, lexDict, triDict, lexMat, triMat



	

		


if __name__ == '__main__':
	emitSeq = '<s> <s> P I A N O </s>'.split()
	epronFile = 'epron.probs'
	ejpronFile = 'epron-jpron.probs'
	eprons = readfile(epronFile)
	ej = readfile(ejpronFile)
	symbols, states, symDict, stateDict, emitProb, transProb = getprob(ej, eprons)
	numSeq = [symDict[s] for s in emitSeq]
	vit.ViterbiPath(numSeq, states, symbols, transProb, emitProb)
