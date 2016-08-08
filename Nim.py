

class Nim:
    def __init__(self, run = False):
    # The __init__ function is automatically run when an instance of the 
    # class is created.
    # The parameter run indicates whether the class should run with the 
    # default parameters set below, or (by default) just create the structures
    #
    # The class tuples are predefined to () until the setup function is run,
    # which automatically creates them according to the given dimension
    #
    # The moves list is populated by various setMoves functions. By default it is set
    # to setStandardMoves().

        self.dimensions = 1 # The maximum number of dimensions to consider
        self.origen = () # The 0 vector
        self.period = () # The current quotiant
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.rectangle = () # The shape of the rectangle needed to work out the period

        self.setDimensions(3) # sets above parameters to 3 dimensional objects
        self.moves = self.setStandardMoves() # A list of the moves, according to the rules
        self.origen_value_is_P = True
        self.setNormalPlay()    

        self.print_report_when_done = True

        if run:
            self.run()

    def run(self):
        if self.print_report_when_done:
            print(report())

    #
    # below are setter functions
    #

    def setDimensions(self,dimensions):
        self.dimensions = dimensions
        self.origen = self.fillTuple(())
        self.period = self.fillTuple((),1)
        self.preperiod = self.origen
        self.rectangle = self.period
        self.moves = self.setStandardMoves()
        self.outcomes = {}
        if self.origen_value_is_P:
            setNormalPlay()
        else:
            setMiserePlay()

    def setNormalPlay(self):
        self.origen_value_is_P = True
        self.outcomes[self.origen] = 'P'

    def setMiserePlay(self):
        self.origen_value_is_P = False
        self.outcomes[self.origen] = 'N'

    def setStandardMoves(self):
        moves = []
        for i in range(self.dimensions ):
            base_tuple = self.decrementTuple( self.fillTuple(()) , i)
            moves.append(base_tuple)
            for j in range(i):
                moves.append(self.incrementTuple(base_tuple,j))
        return moves

    def evaluateTuple(self,t):
        if t in self.outcomes:
            return outcomes[t]
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

    def offthegrid(self,t):
        #
        # if a given tuple contains a negative scalar
        # return True, else return False
        #
            for idx in range(len(t)):
                if t[idx] == -1:
                    return True
            return False

    #
    # Tuple manipulation functions
    #

    def addTuples(self,t1,t2):
        #
        # this function returns a new tuple constructed
        # by component-wise addition from the two input tuples
        #
        return tuple([i+j for i,j in zip(t1,t2)])

    def decrementTuple(self,t, pos = 0):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position decremented by 1.
        indexTuple = self.fillTuple( (), 0, pos ) + (-1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def fillTuple(self, t, fill=0, d = None):
        if d == None:
            d = self.dimensions
        if d == 0:
            return ()
        while len(t) < d:
            t += fill,
        return t

    def incrementTuple(self,t, pos = 0):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position incremented by 1.
        indexTuple = self.fillTuple( (), 0, pos ) + (1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def periodHolds(self,current_dimension):
        global outcomes, period, preperiod, outcomes, dimensions
        cur_position = preperiod
        indexer = fillTuples((),0, current_dimension) + period[current_dimension]
        indexer = fillTuples(indexer)
        while(addTuples(cur_position, indexer) in outcomes):
            if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
                return false
            cur_position = addTuples(cur_position, indexer)

