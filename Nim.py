

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
            self.run()

    def run(self):
        self.setup()
        if self.print_report_when_done:
            print(report())

    def setup(self):
        self.origen = self.fillTuple()
        self.period = self.fillTuple((),1)
        self.preperiod = self.origen
        self.rectangle = self.period

        if self.origen_value_is_P:
            self.outcomes[self.origen] = 'P'
        else:
            self.outcomes[self.origen] = 'N'

    def evaluateTuple(self,t):
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
            neg = False
            for idx in range(len(t)):
                if t[idx] == -1:
                    neg = True
            return neg

    #
    # Tuple manipulation functions
    #

    def addTuples(self,t1,t2):
        #
        # this function returns a new tuple constructed
        # by component-wise addition from the two input tuples
        #
        return [i+j for i,j in zip(t1,t2)]

    def decrementTuple(self,t, pos = 0):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position decremented by 1.
        indexTuple = fillTuple( (), 0, pos ) + (1,)
        return addTuples(t, fillTuple(indexTuple))

    def fillTuple(self, t, fill=0, d = None):
        if d == None:
            d = self.dimensions
        while len(t) < d:
            t += fill,
        return t

    def incrementTuple(self,t, pos = 0):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position incremented by 1.
        indexTuple = fillTuple( (), 0, pos ) + (1,)
        return addTuples(t, fillTuple(indexTuple))

    def periodHolds(self,current_dimension):
        global outcomes, period, preperiod, outcomes, dimensions
        cur_position = preperiod
        indexer = fillTuples((),0, current_dimension) + period[current_dimension]
        indexer = fillTuples(indexer)
        while(addTuples(cur_position, indexer) in outcomes):
            if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
                return false
            cur_position = addTuples(cur_position, indexer)

    def setStandardMoves(self):
        self.moves = []
        for i in range(dimensions ):
            base_tuple = self.decrementTuple( (), i)
            self.moves.append(base_tuple)
            for j in range(i):
                self.moves.append(incrementTuple(base_tuple,j))

