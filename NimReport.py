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

        # This Function returns a string that lists the values of the parameters line by line

        if self.outcomes[self.origen] == 'P':
            text = 'Play: \t\tStandard Play\n'
        else:
            text = "Play: \t\tMisere Play\n"
        text += 'Period: \t' + str(self.period) + '\n'
        text += 'Preperiod: \t' + str(self.preperiod) + '\n'
        text += 'Moves: \t\t' + str(self.moves) + '\n'
        text += 'Rectangle: \t' + str(self.rectangle) + '\n'
        return text

    def reportGrids(self, report_boundary = self.boundary):

        # Input: report_boundary, a tuple representing the boundary of you wish to print
        #
        # Output: a string containg the values of self.outcomes
        #   arranged in grids
        
        max_dimension = 0 # see how many dimensions the boundary tuple contains
        for i in range(len(report_boundary)):
            if report_boundary[i] != None and report_boundary[i] != 0:
                max_dimension += 1

        if max_dimension == 0:
            return "No dimensions to report\n"

        cur_t = self.origen
        if max_dimensions == 1: 
            text = ""
            for i in range(self.report_boundary[1]):
                text += self.getOutcome[cur_t] + " "
                cur_t = self.incrementTuple(cur_t,1)
            return text
        else:
            return self.printGrid(cur_t)

    def printGrid(self, t):

        # Helper function for reportGrids() for when the tuple has more than 1 dimension

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

