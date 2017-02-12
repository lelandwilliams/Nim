from NimTuples import NimTuples

class NimBase(NimTuples):

# This class provides the following functions:
# __init__(self, run)
# run(self)
# fillRectangle(self,dim)
# getOutcome(self,t)
# offthegrid(self,t)
# setDimensions(self, dimensions)
# setNomalPlay(self)
# setMiserePlay(self)
# setStandardMoves(self)

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

        self.max_dimensions = 0 # The maximum number of dimensions to consider
        self.max_depth = 100 # The max length of the rectangle in any dimension
        self.origen = ()    # The 0 vector
        self.period = ()    # The currently considered quotiant
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.rectangle = () # The shape of the rectangle needed to work out the period, being deprecated in favor of explored_region
        self.normal_play = True    

        self.setDimensions(1) # sets above parameters to 3 dimensional objects
        self.moves = self.setStandardMoves() # A list of the moves, according to the rules

        self.print_report_when_done = False

        if run:
            self.run()
    
    def run(self):
         
        # This function is the main loop of the program
        
        cur_dimension = 1   # start by looking for a pattern in dimension 1
        self.rectangle = self.origen

        while cur_dimension <= self.max_dimensions:
            self.rectangle = self.incrementTuple(self.rectangle, cur_dimension)
            match_value = self.checkForMatch(self.rectangle, cur_dimension)
            if match_value != -1: # -1 signals no match found
                cur_dimension += 1
                self.updatePreperiod(cur_dimension, match_value)

        if self.print_report_when_done:
            print(self)

    def checkForMatch(self, t, dim):
        
        # Input: the current dimension to check,
        #   the tuple describing the rest of the dimensions
        # Output: The first dimension of the matching cell, or -1 if no match

        if dim == 1:
            check_tuple = self.setTuplePositionXtoY(t, dim, self.preperiod[dim])
            while check_tuple[dim] < t[dim]:
                if self.getOutcome(check_tuple) == self.getOutcome(t):
                    return check_tuple[dim] 
                check_tuple = self.incrementTuple(check_tuple, dim)
            return -1

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

    def getOutcome(self,t):
        
        # Input: a tuple
        # Output: 'P' or 'N'
        #
        # This function returns the P/N value in the outcomes dictionary, if it exists
        # if not, it calculates it, and stores it in the outcomes dictionary and returns it

        if t in self.outcomes:
            return self.outcomes[t]
        elif self.offthegrid(t):
                return 'N'
        else:
            for move in self.moves:
                if self.getOutcome(self.addTuples(t,move)) == 'P':
                    self.outcomes[t] = 'N'
                    return 'N'
            self.outcomes[t] = 'P'
            return 'P'

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
    # below are setter functions
    #

    def setDimensions(self, dimensions):
        self.max_dimensions = dimensions
        self.origen = self.fillTuple((None,))
        self.period = self.fillTuple((None,))
        self.preperiod = self.origen
        self.moves = self.setStandardMoves()
        self.outcomes = {}
        if self.normal_play:
            self.outcomes[self.origen] = 'P'
        else:
            self.outcomes[self.origen] = 'N'

    def setNormalPlay(self):
        self.normal_play = True
        self.outcomes[self.origen] = 'P'

    def setMiserePlay(self):
        self.normal_play = False
        self.outcomes[self.origen] = 'N'

    def updatePreperiod(self, cur_dimension, match_value):
        self.setTuplePositionXtoY(self.preperiod, cur_dimension, match_value)

    def setStandardMoves(self):
        moves = []
        for i in range(1, self.max_dimensions + 1):
            base_tuple = self.decrementTuple( self.fillTuple((None,)) , i)
            moves.append(base_tuple)
            for j in range(1, i):
                moves.append(self.incrementTuple(base_tuple,j))
        return moves
