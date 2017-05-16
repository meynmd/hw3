#!/bin/python

# from collections import defaultdict
import sys
import read_epron_jpron as r

'''
Tree class
to build our pronunciation-spelling trie
'''
class Tree:
    def __init__(self, value):
        self.Value = value
        self.Children = {}

    def addLeaf(self, transSymbol, value):
        self.Children[transSymbol] = Tree(value)

    def addNode(self, transSymbol, tree, value):
        if tree == None:
            self.Children[transSymbol] = Tree(value)
        self.Children[transSymbol] = tree

    def printTree(self, level = 0):
        for k in self.Children.keys():
            print '{0} '.format(k)
            self.Children[k].printTree(level + 1)

    '''
    This is where the tree building happens
    '''
    def expand(self, pre, post, leaf):
        if pre not in self.Children.keys():
            self.addNode(pre, Tree(None), None)
        if len(post) == 0:
            self.Value = leaf
            return
        else:
            self.Children[pre].expand(post[0], post[1:], leaf)

    '''
    This just loops over the lines pairs of word, pronunciation
    and sends each pair to Tree.expand()
    '''
    def build(self, word_pron):
        for (word, pron) in word_pron:
            pron = pron.split()
            self.expand(pron[0], pron[1:], word)




'''
pronuncation to word trie-building functions
'''

def buildTree(word_pron):
    tree = Tree('__root__')
    for (word, pron) in word_pron:
        pron = pron.split()
        tree.expand(pron[0], pron[1:], word)
    return tree


def readEnglishProns(filename):
    with open(filename, 'r') as fp:
        data = []
        for line in fp.readlines():
            if line[0].isalpha():
                contents = line.split()
                word = contents[0]
                chars = ' '.join(contents[1:])
                data.append((word, chars))

        return data



'''
main script
'''

MAX_E_PHON = 3

if __name__ == '__main__':
    # read our English pronunciation to word lexicon
    eWordFile = 'eword.wfsa'
    ePronFile = 'eword-epron.data'
    ejpronFile = 'epron-jpron.data'
    if sys.argv == 4:
        eWordFile = sys.argv[1]
        ePronFile = sys.argv[2]
        ejpronFile = sys.argv[3]

    wp = readEnglishProns(ePronFile)

    # build our trie
    t = buildTree(wp)

    # get English-Japanese pronunciation probs
    ejDict = r.read_construct_data(ejpronFile)
    print str(ejDict)

    # try to translate input
    # inputline = sys.stdin.read()
    candidates = []
    inputline = 'P I A N O'
    for start in range(len(inputline)):
        for size in range(MAX_E_PHON):
            end = start + size
            if end >= len(inputline):
                continue



