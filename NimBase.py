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
        self.rectangle = self.origen # and start at the beginning

        while cur_dimension <= self.max_dimensions:
            # increment rectangle in current dimension
            self.rectangle = self.incrementTuple(self.rectangle, cur_dimension)

            failure_dimension = 0 # remembers in which dimension a failure to find a match was found
            # 0 indicates no failure occured
            for dim in range(1, cur_dimension): # test all explored dimensions
                if self.checkForMatch(self.rectangle, dim) == -1:
                    failure_dimension = dim
                    break
            
            if failure_dimension > 0:
            # if a failure occured, start over by considering current dimension.
                cur_dimension = failure_dimension 
                continue

            match_value = self.checkForMatch(self.rectangle, cur_dimension)
            if match_value != -1: # -1 signals no match found
                cur_dimension += 1
                self.updatePreperiod(cur_dimension, match_value)

        self.period = self.subtractTuples(self.rectangle, self.preperiod)

        if self.print_report_when_done:
            print(self)

        return self.period

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

        elif dim == 2:
            check_tuple = self.setTuplePositionXtoY(t, 1, 0)
            check_tuple = self.setTuplePositionXtoY(t, 2, self.preperiod[2])
            match = True
            for x_2 in range(self.preperiod[2], t[2]+1):
                for x_1 in range(t[1] +1):
                    pass

    def explore(self, dim):
        if dim == 0:
            self.explore(1)
        elif dim > self.max_dimensions:
            return None
        else:
            for i in range(dim + 1, self.max_dimensions + 1):
                self.setXtoY(self.preperiod, i, 0)
                self.setXtoY(self.rectangle, i, 0)
            self.incrementTuple(self.preperiod, 1)
            for i in range(self.preperiod[dim], self.rectangle[dim]+1):
                if self.getSlice(dim, i) == self.getSlice(dim, self.rectangle[dim]:
                    self.preperiod[dim]=i
                    explore(dim +1)
                    break
            self.explore(dim)




                    
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

    def verify(self, dim):
        pass
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
