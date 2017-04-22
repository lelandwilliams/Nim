from NimReport import NimReport

class Nim(NimReport):
    """ This is the 'top-level' or 'user-level' class of this project
    Make sure you run this class with python3. If you are getting weird
    messages about super(), then you probably tried to use this class
    with python2.
    """

    def __init__(self, dimensions=3, rulecode=None, normalPlay = False):
        # TODO make normal play an enum
        # TODO make dimensions have a default of None

        super().__init__(); # calls super class inits
        self.rulecode = rulecode

        # Test for non-full parameters, since we cant run without them
        # Todo: Enter an interactive mode
        if dimensions == None:
            return True
        self.setDimensions(dimensions)


    def setDimensions(self, dim):
        self.max_dimensions = dim
        self.origen = self.fillTuple((None,))
        self.rectangle = self.origen
        self.preperiod = self.origen

       # And test that the string is a valid code

        self.setMoves(self.rulecode)
