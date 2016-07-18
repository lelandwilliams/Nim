

dimensions = 3
outcomes ={}
origen_value_is_P = True
origen = ()
period = ()         # the period is usually labelled 'D' 
preperiod = ()      # the preperiod is usually labelled 'R'
#moves = [(-1,0,0),(1,-1,0),(0,1,-1)]
moves = []

def Nim():
    global dimensions
    setup()
    current_tuple = origen
    current_dimension = 0

    while(current_dimension < dimensions):
        current_tuple = incrementTuple(current_tuple, current_dimension)
        evaluateTuple(current_tuple)
        if periodHolds():
            current_dimension += 1
        else:
            updatePeriod()

def addTuples(x,y):
    #
    # this function returns a new tuple constructed
    # by component-wise addition from the two input tuples
    #
    newTuple = ()
    for idx in range(len(x)):
        newTuple += (x[idx] + y[idx]),
    return newTuple

def evaluateTuple(t):
    if t not in outcomes:
        if offthegrid(t):
            if not origen_value_is_P:
                outcomes[t] = 'P'
            else:
                outcomes[t] = 'N'
        else:
            outcome = 'N'
            for move in moves:
                if addTuples(t,move) not in outcomes:
                    evaluateTuple(addTuples(t,move))
                if outcomes[addTuples(t,move)] == 'P':
                    outcome = 'P'
            outcomes[t] = outcome

def fillTuple(t, fill=0, d = dimensions):
    while len(t) < d:
        t += fill,
    return t

def incrementTuple(t, dim = 0):
    indexTuple = fillTuple( (), 0, dim ) + (1,)
    return addTuples(t, fillTuple(indexTuple))

def offthegrid(t):
        neg = False
        for idx in range(len(t)):
            if t[idx] == -1:
                neg = True
        return neg

def periodHolds(current_dimension):
    global outcomes, period, preperiod, outcomes, dimensions
    cur_position = preperiod
    indexer = fillTuples((),0, current_dimension) + period[current_dimension]
    indexer = fillTuples(indexer)
    while(addTuples(cur_position, indexer) in outcomes):
        if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
            return false
        cur_position = addTuples(cur_position, indexer)

def setNimMovesold():
    moves = []
    moves.append(fillTuple((-1,)))
    for idx in range(dimensions -1):
        newtuple = fillTuple((),0, idx)
        newtuple += (1,-1)
        moves.append(fillTuple(newtuple))

def setNimMoves():
    moves = []
    moves.append(fillTuple((-1,),0,dimensions))
    for i in range(dimensions ):
        for j in range(i+1, dimensions ):
            t = fillTuple((),0,i)
            inner = (1,) + fillTuple((),0,j-i-1) + (-1,)
            t += inner
            moves.append(fillTuple(t,0,dimensions))
    return moves


def setup():
    global moves
    origen = fillTuple(())
    if origen_value_is_P:
        outcomes[origen] = 'P'
    else:
        outcomes[origen] = 'N'

    preperiod = fillTuple((),1)
    moves = setNimMoves()
    moves.append(1)
