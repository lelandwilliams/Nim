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
        self.max_depth = 100 # The max length of the rectangle in any dimension
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
            self.explore(1)
        if dim > self.max_dimensions:
            return None

        # Zero out later dimensions of preperiod, rectangle
        self.preperiod = self.zeroHigherDimensions(self.preperiod, dim)
        self.rectangle = self.zeroHigherDimensions(self.rectangle, dim)

        # increment rectangle in present dimension
        self.incrementTuple(self.rectangle, dim)

        # verify new value of dimemsion holds for prior
        # dimension values

        failure_dimension = self.verify(dim -1) 
        if failure_dimension > -1:
            self.explore(failure_dimension)
        else:
            match_found = False
            for i in range(self.preperiod[dim], self.rectangle[dim]+1):
                if self.getSlice(dim, i) == self.getSlice(dim, self.rectangle[dim]):
                    self.preperiod[dim]=i
                    match_found = True
                    break
            if match_found:
                explore(dim +1)
            else:
                self.explore(dim)

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

    def getSlice(dimension, value, cur_tuple = self.rectangle):
        for i in range(1, dimension):
            self.setXtoY(cur_tuple, i, 0)
        self.setXtoY(cur_tuple, dim, value)
        s = str()

        while(cur_tuple[dim] = value):
            s.append(self.getOutcome(cur_tuple))
            cur_tuple = self.incrementTuple(cur_tuple)

        return s

    def offthegrid(self,t):
        #
        # if a given tuple contains a negative scalar
        # return True, else return False
        #
            for idx in range(len(t)):
                if t[idx] == -1:
                    return True
            return False

    def verify(self, test_dim, set_dim):
        return_value = -1 # -1 indicates all values pass
        if test_dim == 0: # the recursion 'base case'
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
