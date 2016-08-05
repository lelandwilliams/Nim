

class Nim:
    def __init__(self, run = False)
    # The __init__ function is automatically run when an instance of the 
    # class is created.
    # The parameter run indicates whether the class should run with the 
    # default parameters set below, or (by default) just create the structures
    #
    # The class tuples are predefined to () until the setup function is run,
    # which automatically creates them according to the given dimension
    #
    # The moves list is populated by various setMoves functions. By default it is set
    # to standardMoves().

        self.dimensions = 3 # The maximum number of dimensions to consider
        self.origen = () # The 0 vector
        self.period = () # The current quotiant
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.moves = [] # A list of the moves, according to the rules
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.current_dimension = 0
        self.rectangle = () # The shape of the rectangle needed to work out the period
        self.origen_value_is_P = True
        self.print_report_when_done = True

        if run:
            self.mainLoop()

        while(current_dimension < dimensions):
            current_tuple = incrementTuple(current_tuple, current_dimension)
            evaluateTuple(current_tuple)
            if periodHolds():
                current_dimension += 1
            else:
                updatePeriod()

    def mainLoop():
        self.setup()
        if self.print_report_when_done:
            print(report())

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
        if t not in self.outcomes:
            if self.offthegrid(t):
                if not self.origen_value_is_P:
                    self.outcomes[t] = 'P'
                else:
                    self.outcomes[t] = 'N'
            else:
                self.outcomes[t] = 'P'
                for move in moves:
                    if self.evaluateTuple(addTuples(t,move)) == 'P':
                        self.outcomes[t] = 'P'
                        break

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
