import math
import numpy
import decode2 as d



'''
Emitted :       list of observed symbols
TransProb :     numpy array [state t][state u][state v]
EmitProb :      numpy array [obs][state]

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
    # obs = '<s> <s> P I A N O </s>'.split()
    # states = '<S> <S> p i a n o </S>'.split()
    # numStates = len(states)
    # emiss = numpy.identity(len(states))
    # trans = numpy.zeros((numStates, numStates, numStates))
    # trans[0, 0, :] = 1.
    # for i in range(numStates - 2):
    #     trans[i, i + 1, i + 2] = 1.
    # # print 'T({0}.{1},{2}) = {3}'.format(states[5], states[6], states[7], trans[5, 6, 7])
    # ViterbiPath([0, 0, 1, 2, 3, 4, 5, 6], states, obs, trans, emiss)

    observations = 'P I A N O'.split()
    file_name = 'epron.probs'
    file_name1 = 'epron-jpron.probs'

    epron_data = d.read_file(file_name)
    TransitionProb,unique_words = d.get_prob(epron_data,Matt=True)

    if unique_words[1]==[None]:
        u_prior = unique_words[0]

    data = d.read_file(file_name1)
    EmissionProb, unique_words = d.get_prob(data,Noise=True)

    EmissionProb['<s>']['<s>'] = 1.
    EmissionProb['</s>']['</s>'] = 1.

    u_i_noise,u_o_noise=unique_words[0], unique_words[1]

    # Emitted, States, EmitSymbols, TransProb, EmitProb
    symbols = observations
    observedSeq = []
    for o in observations:
        for i in range(len(symbols)):
            if symbols[i] == o:
                observedSeq.append(i)

    states = [s for s in EmissionProb]

    transMat = numpy.zeros((len(states), len(states), len(states)))

    for ((k1, k2), v) in TransitionProb.items():
        for i in range(len(states)):
            if k1 == states[i]:
                num_k1 = i
            if k2 == states[i]:
                num_k2 = i
            if v == states[i]:
                num_v = i
        print v
        transMat[num_k1, num_k2] = v

    print transMat

