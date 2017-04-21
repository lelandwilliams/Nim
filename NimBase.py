from NimTuples import NimTuples

class PlayType(Enum) :
    Normal = 0
    Misere = 1

class NimBase(NimTuples):

# This class provides the following functions:
# __init__(self, run)
# run(self)
# getOutcome(self,t)
# offthegrid(self,t)
# setDimensions(self, dimensions)
# setNomalPlay(self)
# setMiserePlay(self)

    def __init__(self, run = False):

        # The __init__ function is automatically run when an instance of the 
        # class is created.
        # The parameter run indicates whether the class should run with the 
        # default parameters set below, or (by default) just create the structures
        #
        # The class tuples are predefined to () until the setup function is run,
        # which automatically creates them according to the given dimension

        self.max_dimensions = 0 # The maximum number of dimensions to consider
        self.max_depth = 100 # The maximum allowed size of the rectangle in any dimension
                            # if max_depth is set to 0, then dimensions can be infinite
        self.origen = ()    # The 0 vector
        self.preperiod = () # The lowest position in each dimension for which
                            # the period holds
        self.outcomes = {}  # a dictionary (key-value pair) of positions and their outcomes
                            # outcomes are either 'N' or 'P'
        self.rectangle = () # The shape of the rectangle needed to work out the period
        self.normal_play = True
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
        failure_dimension = self.verify(dim) 
        if failure_dimension:
            return self.explore(failure_dimension)

        # see if new value of rectangle matches an earlier value
        for i in range(self.preperiod[dim], self.rectangle[dim]):
            t = self.setTuplePositionXtoY(self.rectangle, dim, i)
            if self.getSlice(dim, t) == self.getSlice(dim, self.rectangle):
                self.updatePreperiod(dim, i)
                return self.explore(dim + 1)
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

        assert cur_tuple == None or type(cur_tuple) == type(tuple())
        cur_tuple = self.rectangle if cur_tuple == None else cur_tuple
        assert type(cur_tuple) == type(tuple())

        # set lower dimensions of cur_tuple to 0
        for i in range(1, dimension):
            cur_tuple = self.setTuplePositionXtoY(cur_tuple, i, 0)

        # remember the value of the cur_tuple in dimension. 
        cur_dimension_value = cur_tuple[dimension]

        # prevent infinite loop that happens when testing lowest dimension
        if dimension == 1:
            return self.getOutcome(cur_tuple)

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

    def period(self):

        # calculates the period from rectangle and preperiod

        t = self.origen
        for i in range(len(self.rectangle)):
            if self.rectangle[i] == None or self.preperiod[i] == None:
                t = self.setTuplePositionXtoY(t, i, None)
            else:
                t = self.setTuplePositionXtoY(t, i, 
                        (self.rectangle[i] - self.preperiod[i]))
        return t

    def verify(self, dim, check_t = None):

        # Input: the dimensions to make sure works. 
        #   In the call from explore, this should be the explore dimension
        # Output: 0 if everything is hunky-dory, else the dimension that 
        #   don't fly

        if not check_t:
            check_t = self.rectangle
        if dim -1 == 0:
            return 0

        for i in range(check_t[dim -1]):
            test_tuple = self.setTuplePositionXtoY(check_t, dim-1, i)
            if self.verify(dim -1, test_tuple):
                return self.verify(dim -1, test_tuple)
        test_tuple = self.setTuplePositionXtoY(check_t, dim-1, self.preperiod[dim-1])
        if self.getSlice(dim -1, test_tuple) != self.getSlice(dim -1, check_t):
            return dim -1
        
        return 0


    def xverify(self, test_dim):

        # Input: test_dim, the dimension of self.rectangle in which we are currently checking
        # Output: -1 if no error found, or test_dim if an error found

        assert test_dim >= 0

        if test_dim == 0: # the recursion 'base case'
            return -1 # -1 indicates all values pass

        # test prior dimensions before this one
        # if an error is found, return
        return_value = self.verify(test_dim -1) 
        if return_value != -1:
            return return_value
       
        # rectangle_test_tuple is set to rectangle, with all the 
        # dimensions up to test_dim zeroed out
        test_tuple = self.rectangle
        for i in range(1, test_dim + 1):
           test_tuple = self.setTuplePositionXtoY(test_tuple, i, 0)

        # set test_tuple to have the same value in test_dim as self.preperiod
        test_tuple = self.setTuplePositionXtoY(test_tuple, test_dim, self.preperiod[test_dim])

        if self.getSlice(test_dim,test_tuple) != self.getSlice(test_dim,self.rectangle):
            return_value = test_dim
        return return_value

    #
    # below are setter functions
    #

    def setDimensions(self, dimensions):
        self.max_dimensions = dimensions
        self.origen = self.fillTuple((None,))
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

    def setMoves(self, code=None):
        
        #Input: a valid quartenary code string
        #Output: nothing
        # This function sets self.moves accoring to the code given
        # It requires that self.max_dimension is set


        self.rulecode = code
        # Test various values of rulecode to set it properly
        # If rulecode is not set, set it to 0.3333....
        if self.rulecode == None:
            self.rulecode = "0."
            while len(self.rulecode < dimensions + 2):
                self.rulecode += "3"

        # If rulecode entered as a float, convert to a string
        if type(self.rulecode) == type(float()):
            self.rulecode = code.str()

        # At this point rulecode should be a string. If not, 
        # throw
        if type(self.rulecode) != type(str()):
            raise ValueError("code {} is invalid." + 
                    "Please enter a string or a float\n".format(self.rulecode))

        # And add trailing 0's to shorthand codes
        while len(self.rulecode) < self.max_dimensions + 3:
            self.rulecode += "0"

        self.moves = list()
        cur_position = 1
        for digit in code[2:]:
            if digit == '1' or digit == '3':
                new_move = self.setTuplePositionXtoY(self.origen, cur_position, -1)
                self.moves.append(new_move)
            if digit == '2' or digit == '3':
                for j in range(cur_position + 1, self.max_dimensions +1):
                    new_move = self.setTuplePositionXtoY(self.origen, j, -1)
                    new_move = self.setTuplePositionXtoY(new_move, j-cur_position, 1)
                    self.moves.append(new_move)
            cur_position += 1

                
    def setMiserePlay(self):
        self.normal_play = False
        self.outcomes[self.origen] = 'N'

    def updatePreperiod(self, cur_dimension, match_value):
        self.preperiod = self.setTuplePositionXtoY(self.preperiod, cur_dimension, match_value)

    def setStandardMoves(self):
        moves = []
        for i in range(1, self.max_dimensions + 1):
            base_tuple = self.decrementTuple( self.fillTuple((None,)) , i)
            moves.append(base_tuple)
            for j in range(1, i):
                moves.append(self.incrementTuple(base_tuple,j))
        return moves
