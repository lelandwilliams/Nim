from NimTuples import NimTuples

class NimBase(NimTuples):

# This class provides the following functions:
# __init__(self, run)
# run(self)
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
        self.max_depth = 100 # The maximum allowed size of the rectangle in any dimension
                            # if max_depth is set to 0, then dimensions can be infinite
        self.origen = ()    # The 0 vector
        self.period = ()    # The currently considered quotiant
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.rectangle = () # The shape of the rectangle needed to work out the period
        self.normal_play = True

        self.setDimensions(3) # sets above parameters to 3 dimensional objects
        self.moves = self.setStandardMoves() # A list of the moves, according to the rules

        self.print_report_when_done = False

        if run:
            self.run()
    
    def run(self):
        self.explore(1)
        
    def explore(self, dim):
        if dim == 0:
            return self.explore(1)
        if dim > self.max_dimensions:
            return True

        # Zero out later dimensions of preperiod, rectangle
        self.preperiod = self.zeroHigherDimensions(self.preperiod, dim)
        self.rectangle = self.zeroHigherDimensions(self.rectangle, dim)

        # increment rectangle in present dimension
        self.rectangle = self.incrementTuple(self.rectangle, dim)

        # make sure rectangle has not overrun preset maximum in the current dimension
        if self.max_depth > 0 and self.rectangle[dim] > self.max_depth:
            print("\nError: self.rectangle in dimension {} has exceeded maximum depth of {}".format( dim, self.max_depth))
            return False

        # verify preperiod and period still holds for new value of rectangle
        failure_dimension = self.verify(dim -1) 
        if failure_dimension > -1:
            return self.explore(failure_dimension)

        # see if new value of rectangle matches an earlier value
        for i in range(self.preperiod[dim], self.rectangle[dim]+1):
            if self.getSlice(dim, i) == self.getSlice(dim, self.rectangle[dim]):
                self.updatePreperiod(dim, i)
                return explore(dim + 1)
        return self.explore(dim)

    def getOutcome(self,t):
        
        # Input: a tuple
        # Output: 'P' or 'N'
        #
        # This function returns the P/N value in the outcomes dictionary, if it exists
        # if not, it calculates it, and stores it in the outcomes dictionary and returns it

        if t in self.outcomes:
            return self.outcomes[t]

        if self.offthegrid(t):
            return 'N'

        for move in self.moves:
            if self.getOutcome(self.addTuples(t,move)) == 'P':
                self.outcomes[t] = 'N'
                return 'N'
        self.outcomes[t] = 'P'
        return 'P'

    def getSlice(self, dimension, cur_tuple = None):

        # Input: dimension, the dimension of the slice we want
        #        cur_tuple, the tuple we are pulling a slice out of. Defaults to rectangle

        cur_tuple = self.rectangle if cur_tuple == None else cur_tuple

        # set lower dimensions of cur_tuple to 0
        for i in range(1, dimension):
            cur_tuple = self.setXtoY(cur_tuple, i, 0)

        # remember the value of the cur_tuple in dimension. 
        cur_dimension_value = cur_tuple[dimension]

        s = str()

        while(cur_tuple[dimension] == cur_dimension_value):
            s += (self.getOutcome(cur_tuple))
            cur_tuple = self.incrementTupleWithCarry(cur_tuple)

        return s

    def offthegrid(self,t):
 
        # Input: t, a tuple
        # Output: True if t contains a negative scalar
        #         False otherwise
        
            for idx in range(len(t)):
                if t[idx] == -1:
                    return True
            return False

    def verify(self, test_dim):

        # Input: test_dim, the dimension of self.rectangle in which we are currently checking
        # Output: -1 if no error found, or test_dim if an error found

        assert test_dim >= 0

        if test_dim == 0: # the recursion 'base case'
            return -1 # -1 indicates all values pass

        # test prior dimensions before this one
        # if an error is round, return
        return_value = self.verify(test_dim -1) 
        if return_value != -1:
            return return_value
       
        # setup test_tuples.
        # rectangle_test_tuple is set to rectangle, with all the 
        # dimensions up to set_dim zeroed out
        test_tuple = self.rectangle
        for i in range(1, set_dim):
           self.setTupleXtoY(test_tuple, i, 1)
        self.setTupleXtoY(rectangle_test, test_dim, self.rectangle[test_dim])

        while(rectangle_test_tuple[set_dim] == self.rectangle[set_dim]):
           preperiod_test_tuple = self.setTupleXtoY(test_tuple, self.preperiod[test_dim])

    #
    # below are setter functions
    #

    def setDimensions(self, dimensions):
        self.max_dimensions = dimensions
        self.origen = self.fillTuple((None,))
        self.period = self.fillTuple((None,))
        self.rectangle = self.origen
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
