class NimTuples:

# Tuple manipulation functions used by NimBase
#
# addTuples(self, t1, t2)
# decrementTuple(self,t, pos)
# fillTuple(self,t fill,d)
# incrementTuple(self,t,pos)
# incrementTupleWithCarry(self,t,pos)
# setTuplePositionXtoY(self,t,x,y)

    def addTuples(self,t1,t2):
        
        # returns a new tuple constructed
        # by component-wise addition from the two input tuples
        #
        t = (None,)
        for i in range(1, len(t1)):
            t += t1[i] + t2[i],
        return t

    def decrementTuple(self,t, pos = 1):

        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position decremented by 1.
        indexTuple = self.fillTuple( (None,), 0, pos ) + (-1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def fillTuple(self, t, fill=0, l = None):

        # This function fills up a give tuple t with fill f until the
        # lenght of the tuple is l
        # if l is not given, l defaults to dimensions +1

        if l == None:
            l = self.dimensions +1
        if l == 0:
            return (None,)
        while len(t) < l:
            t += fill,
        return t

    def incrementTuple(self,t, pos = 1):

        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position incremented by 1.
        if pos == 0:    #pos 0 is not incrementable
            return t

        indexTuple = self.fillTuple( (), 0, pos ) + (1,)
        return self.addTuples(t, self.fillTuple(indexTuple))

    def incrementTupleWithCarry(self,t,pos = 1):
        
        # Input: a tuple, t & the position to increment (defaults to 1)
        # Output: the incremented tuple, with values of the boundary 'carried' to the next level
        # Function does not carry the uppermost (rightmost) dimension
        if pos == 0: #pos 0 is not incrementable
            return t

        t = self.incrementTuple(t,pos)
        for dim in range(pos, self.dimensions + 1):
            if t[dim] > self.rectangle[dim]:
                t = t[:dim] + (0,) + t[(dim +1):]
                t = self.incrementTuple(t,dim + 1)
        return t

    def periodHolds(self,current_dimension):
        #
        # This function is leftover from the previous version of the program
        # It is now currently being used, and will probably be removed
        #
        global outcomes, period, preperiod, outcomes, dimensions
        cur_position = preperiod
        indexer = fillTuples((),0, current_dimension) + period[current_dimension]
        indexer = fillTuples(indexer)
        while(addTuples(cur_position, indexer) in outcomes):
            if outcomes[cur_position] != outcomes[addTuples(cur_position, indexer)]:
                return false
            cur_position = addTuples(cur_position, indexer)

    def setTuplePositionXtoY(self, t, x, y):
        #
        # Inputs: a tuple t, the desired position x, and the new value y
        # output: a tuple that is identical to the input tuple, with the exception
        #   that it's xth position has been changed to y
        #
    
        new_t = ()
        for i in range(len(t)):
            if i == x:
                new_t += (y,)
            else:
                new_t += (t[i],)
        return new_t



