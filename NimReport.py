class NimReport:

    # This class contains the following report functions for Nim:
    # __repr__(self)
    # report(self)
    # reportGrids(self, t)
    # reportParameters(self)

    def __repr__(self):
            return self.report()

    def report(self):

#        return self.report_parameters() + self.reportGrids()
        return self.report_parameters() 

    def report_parameters(self):

        #
        # This Function returns a string that lists the values of the parameters line by line
        #

        if self.outcomes[self.origen] == 'P':
            text = 'Play: \t\tStandard Play\n'
        else:
            text = "Play: \t\tMisere Play\n"
        text += 'Period: \t' + str(self.period) + '\n'
        text += 'Preperiod: \t' + str(self.preperiod) + '\n'
        text += 'Moves: \t\t' + str(self.moves) + '\n'
        text += 'Rectangle: \t' + str(self.rectangle) + '\n'
        return text

    def reportGrids(self, cur_t = None):
        #
        # Input: cur_t, a tuple if for some reason you want the reports to begin 
        #       at some place other than the origen.
        #   If a tuple is not given, the report begins at the origen.
        # Output: a string containg the values of self.outcomes
        #   arranged in grids
        #
        # Note: currently the function only prints out the area within the 
        # rectangle. Any tuples that are evaluated and added to outcomes yet
        # not within the rectangle are not printed.
        #
        if cur_t == None:
            cur_t = self.origen

        if self.dimensions == 1: 
            text = ""
            for i in range(self.rectangle[1]):
                text += self.outcomes[cur_t] + " "
            return text
        else:
            return self.printGrid(cur_t)

    def printGrid(self, t):
        #
        # Helper function for reportGrids() for when the tuple has more than 1 dimension
        #
        text = ""
        while t[-1] <= self.rectangle[-1]:
            if (t[0] == 0) and t[1] == 0:
                text += "\n\n"
                for dim in range(2,self.dimensions):
                    text += "x_" + str(dim +1) + " = " + str(t[dim]) + ";  "
                text += "\n "
                for i in range(self.rectangle[0] +1):
                    text+= " " + str(i) 
            if t[0] == 0:
                text+= "\n" + str(t[1]) + " "

            text+= self.outcomes[t] + " "
            t = self.incrementTupleWithCarry(t)
        return text



