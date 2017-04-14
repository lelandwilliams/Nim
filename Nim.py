import NimReport

class Nim(NimReport):
    """ This is the 'top-level' or 'user-level' class of this project
    Make sure you run this class with python3. If you are getting weird
    messages about super(), then you probably tried to use this class
    with python3.
    """

    def __init__(self, dimensions=3, rulecode=None, normalPlay = True):
        # TODO make normal play an enum
        # TODO make dimensions have a default of None

        super.__init__(); # calls super class inits
        self.rulecode = rulecode

        # Test for non-full parameters, since we cant run without them
        # Todo: Enter an interactive mode
        if dimensions == None:
            return True
        self.setDimensions(dimensions)


    def setDimensions(dim):
        self.max_dimensions = dimensions
        self.origen = self.fillTuple((None,))
        self.rectangle = self.origen
        self.preperiod = self.origen

        # Test various values of rulecode to set it properly
        # If rulecode is not set, set it to 0.3333....
        if self.rulecode == None:
            self.rulecode = "0."
            while len(self.rulecode < dimensions + 2):
                self.rulecode += "3"

        # If rulecode entered as a float, convert to a string
        if type(rulecode) == type(float()):
            self.rulecode = rulecode.str()

        # At this point rulecode should be a string. If not, 
        # throw
        if type(rulecode) != type(str()):
            throw("rulecode {} is invalid. Please enter a string or a float\n".format(self.rulecode))

        # And test that the string is a valid code





