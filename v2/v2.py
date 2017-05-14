import math
import numpy



'''
Input :             list of observed symbols
TransProb :         numpy array [state t][state u][state v]
EmitProb :         numpy array [obs][state]

we will assume the first state is <s> and the last is </s>
'''
def ViterbiPath(Emitted, States, EmitSymbols, TransProb, EmitProb):
    order = 2
    numstates = EmitProb.shape[0]
    numobs = len(Emitted)# + order + 1
    graph = numpy.zeros((numobs, numstates, numstates))
    trace = numpy.zeros((numobs, numstates, numstates))

    # initialize <s> columns
    graph[0: order, 0, 0] = 1.
    graph[order, 0, :] = EmitProb[Emitted[order]]

    for i in range(order + 1, len(Emitted)):
        for w in range(numstates):
            for v in range(numstates):
                probs = numpy.zeros((numstates))
                for u in range(numstates):
                    probs[u] = graph[i - 1, u, v] * TransProb[u, v, w] * EmitProb[Emitted[i], w]
                graph[i, v, w] = probs.max()
                trace[i, v, w] = probs.argmax()

    print graph
    #print trace

    last = graph[-1, :, :].argmax()
    z, y = int(math.floor(last / numstates)), last % numstates
    path = [States[z], States[y]]
    print path
    return graph














if __name__ == '__main__':
    obs = '<s> <s> P I A N O </s>'.split()
    states = '<S> <S> p i a n o </S>'.split()
    numStates = len(states)
    emiss = numpy.identity(len(states))
    trans = numpy.zeros((numStates, numStates, numStates))
    trans[0, 0, :] = 1.
    for i in range(numStates - 2):
        trans[i, i + 1, i + 2] = 1.
    # print 'T({0}.{1},{2}) = {3}'.format(states[5], states[6], states[7], trans[5, 6, 7])
    ViterbiPath([0, 0, 1, 2, 3, 4, 5, 6], states, obs, trans, emiss)