from NimBase import NimBase

class NimReport(NimBase):

    # This class contains the following report functions for Nim:
    # __repr__(self)
    # report(self)
    # reportGrids(self, t)
    # reportParameters(self)

    def __init__(self):
        super().__init__()

    def __repr__(self):
            return self.report()

    def p_positions(self):
        position_list = list()
        for j,k in self.outcomes.items():
            if k == 'P':
                flag = True
                for i in range(1, len(self.rectangle)):
                    if j[i] == self.rectangle[i]:
                        flag = False
                if flag:
                    position_list.append(j)
        return position_list

    def report(self):

        return self.report_parameters() + self.reportGrids()

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

    def reportGrids(self, report_boundary = None):

        # Input: report_boundary, a tuple representing the boundary of you wish to print
        #
        # Output: a string containg the values of self.outcomes
        #   arranged in grids

        report_boundary = self.rectangle if report_boundary == None else report_boundary
        
        max_dimension = 0 # see how many dimensions the boundary tuple contains
        for i in range(len(report_boundary)):
            if report_boundary[i] != None and report_boundary[i] != 0:
                max_dimension += 1

        if max_dimension == 0:
            return "No dimensions to report\n"

        cur_t = self.origen
        if max_dimension == 1: 
            text = ""
            for i in range(self.report_boundary[1]):
                text += self.getOutcome[cur_t] + " "
                cur_t = self.incrementTuple(cur_t,1)
            return text
        else:
            return self.printGrid()

    def printGridHeader(self,c):
        line = str()
        for i in range(3, len(c)):
            if len(line) > 0:
                line+=", "
            line += "x_{} = {}".format(i, c[i])
        line += "\n"
        return line

    def printGrid(self, truncate = False):

        # Helper function for reportGrids() for when the tuple has more than 1 dimension
        # The truncate parameter tells the function to  
        # not display values at the outer limit of rectangle

        text = ""
        c = self.origen
        quitting_time = False

        while not quitting_time:
            if c[1] == 0 and len(text) > 0:
                text+= "\n"

            if (c[1] == 0) and (len(c) <= 2 or c[2] == 0):
                if len(text) > 0:
                    text += "\n"
                text += self.printGridHeader(c)

            text += self.getOutcome(c) + " "
            c = self.incrementTupleWithCarry(c)

            if truncate:
                for i in range(1, len(self.rectangle)):
                    if c[i] == self.rectangle[i]:
                        c = self.incrementTupleWithCarry(c, i)

            if c == self.origen:
                quitting_time = True
        return text

