class NimBase:

    # This class provides the following functions:
    # __init__(self, run)
    # run(self)
    # checkDimension(self,dim)
    # fillRectangle(self,dim)
    # evaluateTuple(self,t)
    # offthegrid(self,t)
    # recUpToDims(self, dim, t)
    # setDimensions(self, dimensions)
    # setNomalPlay(self)
    # setMiserePlay(self)
    # setStandardMoves(self)
    # addTuples(self, t1, t2)
    # decrementTuple(self,t, pos)
    # fillTuple(self,t fill,d)
    # incrementTuple(self,t,pos)
    # incrementTupleWithCarry(self,t,pos)
    # setTuplePositionXtoY(self,t,x,y)

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
         
        # This function is the main loop of the program
        
        done = False
        current_dimension = 1
        cur_t = self.fillTuple()
        while not done:
            self.rectangle = self.incrementTuple(self.rectangle, current_dimension -1)
            self.fillRectangle()
            if True:
#           if self.checkDimension(current_dimension):
                done = True
        if self.print_report_when_done:
            print(self)

    def checkDimension(self, dim,t):
        
        # Input: dimensions of the slice, a tuple that specifies which dimensions each slice lives in
        # Output: True if the last slice in the given dimension has a match in the prior slices
        #         False otherwise

        pass

    def fillRectangle(self, dim=-1):
        #
        # Input: number of dimensions to fill
        # Output: none
        #
        # This function makes sure that every lattice point inside (inclusively)
        # the given number of dimensions of self.rectangle has had it's outcome determined
        # and recorded in self.outcomes
        #
        t = self.origen
        while t[dim] <= self.rectangle[dim]:
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
        elif self.offthegrid(t):
                return 'N'
        else:
            for move in self.moves:
                if self.evaluateTuple(self.addTuples(t,move)) == 'P':
                    self.outcomes[t] = 'N'
                    return 'N'
            self.outcomes[t] = 'P'
            return 'P'

    def getOutcome(self, t):

        # returns the P/N value of t
        # if t is not set, it evaluates it first

        if t not in self.outcomes:
            self.evaluateTuple(t)
        return self.outcomes(t)

    def offthegrid(self,t):
        #
        # if a given tuple contains a negative scalar
        # return True, else return False
        #
            for idx in range(len(t)):
                if t[idx] == -1:
                    return True
            return False

    def recUpToDims(self, dim, t):
        #
        # Input, the max dimension to include, and a tuple t
        #       Note that the function begins with t, so the first few dimensions
        #       of the given tuple t should be set to zero, if that is desired
        #       This function does not check for that.
        # Output: a string of every outcome inside self.rectangle
        #       of the first dim dimensions within the higher dimensions 
        #       specified by the input tuple t
        s = ""
        cur_t = t
        while cur_t[dim] <= t[dim]:
            s += self.outcomes[cur_t]
            cur_t = self.incrementTupleWithCarry(cur_t)
        return s



    #
    # below are setter functions
    #

    def setDimensions(self,dimensions):
        self.dimensions = dimensions
        self.origen = self.fillTuple((None,))
        self.period = self.fillTuple((None,),1)
        self.rectangle = self.origen
        self.preperiod = self.origen
        self.moves = self.setStandardMoves()
        self.outcomes = {}

    def setNormalPlay(self):
        self.outcomes[self.origen] = 'P'

    def setMiserePlay(self):
        self.outcomes[self.origen] = 'N'

    def setStandardMoves(self):
        moves = []
        for i in range(1, self.dimensions + 1):
            base_tuple = self.decrementTuple( self.fillTuple((None,)) , i)
            moves.append(base_tuple)
            for j in range(1, i):
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
        t = (None,)
        for i in range(1, len(t1)):
            t += t1[i] + t2[i],
        return t

    def decrementTuple(self,t, pos = 1):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position decremented by 1.
        indexTuple = self.fillTuple( (None,), 0, pos ) + (-1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def fillTuple(self, t, fill=0, l = None):
        # This function fills up a give tuple t with fill f until the
        # lenght of the tuple is l
        # if l is not given, l defaults to dimensions +1

        if l == None:
            l = self.dimensions +1
        if l == 0:
            return (None,)
        while len(t) < l:
            t += fill,
        return t

    def incrementTuple(self,t, pos = 1):
        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position incremented by 1.
        if pos == 0:    #pos 0 is not incrementable
            return t

        indexTuple = self.fillTuple( (), 0, pos ) + (1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def incrementTupleWithCarry(self,t,pos = 1):
        #
        # Input: a tuple, t & the position to increment (defaults to 1)
        # Output: the incremented tuple, with values of the boundary 'carried' to the next level
        # Function does not carry the uppermost (rightmost) dimension
        if pos == 0: #pos 0 is not incrementable
            return t

        t = self.incrementTuple(t,pos)
        for dim in range(pos, self.dimensions + 1):
            if t[dim] > self.rectangle[dim]:
                t = t[:dim] + (0,) + t[(dim +1):]
                t = self.incrementTuple(t,dim + 1)
        return t

    def periodHolds(self,current_dimension):
        #
        # This function is leftover from the previous version of the program
        # It is now currently being used, and will probably be removed
        #
        global outcomes, period, preperiod, outcomes, dimensions
        cur_position = preperiod
        indexer = fillTuples((),0, current_dimension) + period[current_dimension]
        indexer = fillTuples(indexer)
        while(addTuples(cur_position, indexer) in outcomes):
            if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
                return false
            cur_position = addTuples(cur_position, indexer)

    def setTuplePositionXtoY(self, t, x, y):
        #
        # Inputs: a tuple t, the desired position x, and the new value y
        # output: a tuple that is identical to the input tuple, with the exception
        #   that it's xth position has been changed to y
        #
    
        new_t = ()
        for i in range(len(t)):
            if i == x:
                new_t += (y,)
            else:
                new_t += (t[i],)
        return new_t



