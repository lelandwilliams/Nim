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
                    if j[i] >= self.rectangle[i]:
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
        text += 'Period: \t' + str(self.period()) + '\n'
        text += 'Preperiod: \t' + str(self.preperiod) + '\n'
        text += 'Moves: \t\t' 
        for i in range(0, len(self.moves)):
                if i>0:
                    text += ", "
                if i>0 and i%2 == 0:
                    text += "\n\t\t"
                text += str(self.moves[i])
        text += '\nRectangle: \t' + str(self.rectangle) + '\n\n'
        return text

    def reportGrids(self, report_boundary = None):

        # Input: report_boundary, a tuple representing the boundary of you wish to print
        #
        # Output: a string containg the values of self.outcomes
        #   arranged in grids

        report_boundary = self.rectangle if report_boundary == None else report_boundary
        
        if len(report_boundary) < 2: # since a len of one would only be the (None) tuple
            return "No dimensions to report\n"

        lines = list()
        cur_t = self.origen
        self.carry_dim = 0
        line = str()
        if len(report_boundary) > 3:
            for i in range(report_boundary[3]):
                line += ("x3 = {:<3}x1 = ".format(i))
                for k in range(report_boundary[1]):
                    line += ("{:<2d}".format(k))
                line += "  "
            if len(report_boundary) > 4:
                lines.append(self.gridHeader(cur_t).center(len(line)))
            lines.append(line)

            for j in range(report_boundary[2]):
                line = str()
                line += "x2 = {:<3}".format(j)
                for i in range(report_boundary[3]):
                    line += "{:5}".format(" ")
                    for k in range(report_boundary[1]):
                        line += "{:<2}".format(self.getOutcome(cur_t))
                        cur_t = self.incrementTupleWithCarry(cur_t, 1, True)
                    line += "{:10}".format(" ")
                lines.append(line)



        else: 
            line += ("{:>9}".format(" "))
            line += "x1 = "
            for i in range(report_boundary[1]):
                line += ("{:2d}".format(i))
            line += "\n"
            lines.append(line)

#       for l in lines:
#           print(l)

        retval = str()
        for l in lines:
            retval += l + "\n"
        return retval



    def gridHeader(self,c):
        line = str()
        for i in range(4, len(c)):
            if len(line) > 0:
                line+=", "
            line += "x_{} = {}".format(i, c[i])
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

