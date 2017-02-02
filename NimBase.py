from NimTuples import NimTuples

class NimBase(NimTuples):

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
        self.rectangle = () # The shape of the rectangle needed to work out the period, being deprecated in favor of explored_region
        self.explored_region = self.rectangle # Some foo until name change rectangle -> explored_region is finished

        self.setDimensions(3) # sets above parameters to 3 dimensional objects
        self.moves = self.setStandardMoves() # A list of the moves, according to the rules
        self.setNormalPlay()    

        self.print_report_when_done = True

        if run:
            self.run()
    
    def run(self):
         
        # This function is the main loop of the program
        
        done = False
        cur_dimension = 1   # start by looking for a pattern in dimension 1
        region_mask = self.origen # the mask tells which values of higher dimensions we are working in

        while not done:
            self.explored_region = self.incrementTuple(self.explored_region, cur_dimensiion)
            if self.checkMatch(self.explored_region, cur_dimension):
                cur_dimension += 1
                if cur_dimension > self.dimensions:
                    done = True

        if self.print_report_when_done:
            print(self)

    def checkMatch(self, dim, t):
        
        # Input: dimensions of the slice, a tuple that specifies which dimensions each slice lives in
        # Output: True if the last slice in the given dimension has a match in the prior slices
        #         False otherwise

        if self.getOutcome(self.explored_region):
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

#        if t not in self.outcomes:
#            self.evaluateTuple(t)
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
