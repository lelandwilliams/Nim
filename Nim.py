from NimReport import NimReport
from NimBase import PlayCondition

class Nim(NimReport):
    """ This is the 'top-level' or 'user-level' (sub)class of this project
    Make sure you run this class with python3. If you are getting weird
    messages about super(), then you probably tried to use this class
    with python2.
    """

    def __init__(self, dimensions=3, rulecode=None, play = PlayCondition.Normal):
        # TODO make dimensions have a default of None

        super().__init__(); # calls super class inits
        self.rulecode = rulecode
        self.playCondition = play

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
        if self.playCondition is PlayCondition.Normal:
            self.outcomes[self.origen] = 'P'
        if self.playCondition is PlayCondition.Misere:
            self.outcomes[self.origen] = 'N'

        self.setMoves(self.rulecode)
