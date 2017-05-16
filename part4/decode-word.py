from collections import defaultdict

# class Tree:
#     def __init__(self, value, children = []):
#         self.Value = value
#         self.Children = [Tree(v) for v in children]
#
#     def add(self, value, children):
#         self.Children[value] = Tree(value, children)
#
#     def preOrder(self, func):
#         func(self.Value)
#         for c in self.Children:
#             c.preOrder(func)
#
#     def printTree(self):
#         self.preOrder(printString)
#
#
# class Tree2:
#     def __init__(self, value):
#         self.Value = value
#         self.Children = {}
#
#     def add(self, key, value):
#         self.Children[key] = Tree(value)
#
#     def preOrder(self, func):
#         func(self.Value)
#         for k in self.Children.keys():
#             self.Children[k].preOrder(func)
#
#     def printTree(self):
#         self.preOrder(printString)


def printString(bar):
    print(bar)

####

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

    def expand(self, pre, post, leaf):
        if pre not in self.Children.keys():
            if len(post) == 0:
                self.Children[pre] = Tree(leaf)
                return
            else:
                self.addNode(pre, Tree(None), None)

        self.Children[pre].expand(post[0], post[1:], leaf)

    def build(self, word_pron):
        for (word, pron) in word_pron:
            pron = pron.split()
            self.expand(pron[0], pron[1:], word)

    def printTrie(self, level = 0):
        for i in range(level):
            print '\t',
        for k in self.Children.keys():
            print '{0} '.format(k)
            self.Children[k].printTree(level + 1)
            #self.Children[k].printTrie()


####
#
# def buildTree(word_pron):
#     tree = Tree('__ROOT__')
#     for (word, pron) in word_pron:
#         pron = pron.split()
#         tree = expandTree(tree, pron[0], pron[1:], word)
#     return tree
#
#
# def expandTree(tree, pre, post, leaf):
#     print 'pre:{0}\tpost:{1}\n\ttree:{2}'.format(pre, post, tree.Children)
#     if pre not in tree.Children.keys():
#         if len(post) == 0:
#             tree.addLeaf(pre, leaf)
#             return tree
#         else:
#             tree.addNode(pre, None, None)
#
#     tree.Children[pre] =
#
#     # tree[pre] = (addTree(tree[pre], post[0], post[1:], leaf), None)
#
#     # tree.add(expandTree(tree.Children[pre], post[0], post[1:], leaf))
#
#     return tree
#
# def printTree(tree):
#     for k in tree.keys():
#         for stuff in tree[k]:
#             print 'tree[{0}]'.format(k) + str(stuff)
#             printTree(tree[stuff])



# def buildTree(word_pron):
#     tree = ({}, None)
#     for (word, pron) in word_pron:
#         pron = pron.split()
#         tree = addTree(tree, pron[0], pron[1:], word)
#     return tree
#
#
# def addTree(tree, pre, post, leaf):
#     print 'pre:{0}\tpost:{1}\n\ttree:{2}'.format(pre, post, tree[0])
#     if pre not in tree[0].keys():
#         if len(post) == 0:
#             tree[pre] = (None, leaf)
#             return tree
#         else:
#             tree[0][pre] = ({}, None)
#
#     tree[pre] = (addTree(tree[pre], post[0], post[1:], leaf), None)
#     return tree
#
# def printTree(tree):
#     for k in tree.keys():
#         for stuff in tree[k]:
#             print 'tree[{0}]'.format(k) + str(stuff)
#             printTree(tree[stuff])



####
#
#
# class Trie:
#     def __init__(self, value):
#         self.Value = value
#         self.Children = defaultdict(lambda : list)
#
#
#     def add(self, key, value):
#         self.Children[key].append(value)
#
#
# '''
# word_pron is a list of (word, p r o n) pairs
# '''
# def buildTrie(word_pron):
#     trie = {}
#     for (word, pron) in word_pron:
#         pron = pron.split()
#         if len(pron) > 1:
#             trie = addSubtrie(trie, pron[0], pron[1:], word)
#         elif len(pron) == 1:
#             trie = addSubtrie(trie, pron[0], [], word)
#
#     return trie


# '''
# addSubtrie
#
# trie :  dict (string->[dict])
# pre :   new key to add
# post :  value of key
# leaf :  eventual leaf node
# '''
# def addSubtrie(trie, pre, post, leaf):
#     if pre not in trie.keys():
#         trie[pre] = []
#
#     if len(post) == 0:
#         print 'appending leaf ' + str(leaf)
#         trie[pre].append(leaf)
#     else:
#         #trie[pre].append(post)
#         if len(post) > 1:
#             trie = addSubtrie(trie, post[0], post[1:], leaf)
#         else:
#             trie = addSubtrie(trie, post[0], [], leaf)
#
#     return trie
#
#
# def printTrie(trie):
#     for k in trie.keys():
#         for stuff in trie[k]:
#             print 'trie[{0}]'.format(k) + str(stuff)
#             printTrie(trie[stuff])
#



if __name__ == '__main__':
    wp = [('PIANO', 'P IY AE N O'), ('PEACE', 'P IY S'), ('PIECES', 'P IY S EH Z'), ('STUFF', 'S T UH F'), ('A', 'AH')]
    # t = buildTrie(wp)
    # printTrie(t)

    t = Tree('__ROOT__')
    t.build(wp)
    t.printTrie()
    #printTree(t)
