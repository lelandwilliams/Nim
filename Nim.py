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

        self.dimensions = 0 # The maximum number of dimensions to consider
        self.max_depth = 100 # The max length of the rectangle in any dimension
        self.origen = ()    # The 0 vector
        self.period = ()    # The currently considered quotiant
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.rectangle = () # The shape of the rectangle needed to work out the period

        self.setDimensions(3) # sets above parameters to 3 dimensional objects
        self.moves = self.setStandardMoves() # A list of the moves, according to the rules
        self.setNormalPlay()    

        self.print_report_when_done = True

        if run:
            self.run()
    
    def run(self):
        # 
        # This function is the main loop of the program
        #
        done = False
        while not done:
            self.rectangle = self.addTuples(self.period, self.preperiod)
            self.fillRectangle()
            done = True
        if self.print_report_when_done:
            print(self)

    def fillRectangle(self):
        #
        # Input: none
        # Output: none
        #
        # This function makes sure that every lattice point inside (inclusively)
        # the dimensions of self.rectangle has had it's outcome determined
        # and recorded in self.outcomes
        #
        t = self.origen
        while t[-1] <= self.rectangle[-1]:
            self.evaluateTuple(t)
            t = self.incrementTupleWithCarry(t)

    def evaluateTuple(self,t):
        #
        # Input: a tuple
        # Outpus: 'P' or 'N'
        #
        # This function also stores the P/N value in the outcomes dictionary
        # when it is first discovered, except when a tuple has a negative scalar,
        # in which case it simply returns 'N'
        #

        if t in self.outcomes:
            return self.outcomes[t]
        else:
            if self.offthegrid(t):
                return 'N'
            else:
                for move in self.moves:
                    if self.evaluateTuple(self.addTuples(t,move)) == 'P':
                        self.outcomes[t] = 'P'
                        return 'P'
                self.outcomes[t] = 'N'
                return 'N'

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
    # The following are functions to create report strings
    #

    def __repr__(self):
            return self.report()

    def report(self):
        return self.report_parameters()

    def reportGrids(self, cur_t = None):
        #
        # Input: cur_t, a tuple
        # Output: a string containg the values of self.outcomes
        #   arranged in grids
        #
        if cur_t == None:
            cur_t = self.origen

        if self.dimensions == 1: 
            text = ""
            for i in range(self.rectangle[0]):
                text += self.outcomes[cur_t] + " "
            return text
        else:
            return self.printGrid(cur_t)

    def printGrid(self, t):
        text = ""
        while t[-1] <= self.rectangle[-1]:
            if (t[0] == 0) and t[1] == 0:
                text += "\n\n"
                for dim in range(2,self.dimensions):
                    text += "x_" + str(dim) + " = " + str(t[dim]) + ";  "
                text += "\n "
                for i in range(self.rectangle[1] +1):
                    text+= " " + str(i) 
            if t[0] == 0:
                text+= "\n" + str(t[1]) + " "

            text+= self.outcomes[t] + " "
            t = self.incrementTupleWithCarry(t)
        return text


    def report_parameters(self):
        #
        # This Function returns a string that lists the values of the parameters line by line
        #
        if self.outcomes[self.origen] == 'P':
            text = 'Play: \t\tStandard Play\n'
        else:
            text = "Play: \t\tMisere Play\n"
        text += 'Period: \t' + str(self.period) + '\n'
        text += 'Preperiod: \t' + str(self.preperiod) + '\n'
        text += 'Moves: \t\t' + str(self.moves) + '\n'
        return text



    #
    # below are setter functions
    #

    def setDimensions(self,dimensions):
        self.dimensions = dimensions
        self.origen = self.fillTuple(())
        self.period = self.fillTuple((),1)
        self.preperiod = self.origen
        self.moves = self.setStandardMoves()
        self.outcomes = {}

    def setNormalPlay(self):
        self.outcomes[self.origen] = 'P'

    def setMiserePlay(self):
        self.outcomes[self.origen] = 'N'

    def setStandardMoves(self):
        moves = []
        for i in range(self.dimensions ):
            base_tuple = self.decrementTuple( self.fillTuple(()) , i)
            moves.append(base_tuple)
            for j in range(i):
                moves.append(self.incrementTuple(base_tuple,j))
        return moves

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

    def incrementTupleWithCarry(self,t,pos = 0):
        #
        # Input: a tuple, t & the position to increment (defaults to 0)
        # Output: the incremented tuple, with values of the boundary 'carried' to the next level
        # Function does not carry the uppermost (rightmost) dimension
        t = self.incrementTuple(t,pos)
        for dim in range(pos, self.dimensions -1):
            if t[dim] > self.rectangle[dim]:
                t = t[:dim] + (0,) + t[(dim +1):]
                t = self.incrementTuple(t,dim + 1)
        return t

    def periodHolds(self,current_dimension):
        global outcomes, period, preperiod, outcomes, dimensions
        cur_position = preperiod
        indexer = fillTuples((),0, current_dimension) + period[current_dimension]
        indexer = fillTuples(indexer)
        while(addTuples(cur_position, indexer) in outcomes):
            if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
                return false
            cur_position = addTuples(cur_position, indexer)

