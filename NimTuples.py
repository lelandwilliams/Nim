class NimTuples:

# Tuple manipulation functions used by NimBase
#
# addTuples(self, t1, t2)
# decrementTuple(self,t, pos)
# fillTuple(self,t fill,d)
# incrementTuple(self,t,pos)
# incrementTupleWithCarry(self,t,pos)
# setTuplePositionXtoY(self,t,x,y)
# zeroHigherDimensions(self,t,dim)

    def addTuples(self,t1,t2):
        
        # returns a new tuple constructed
        # by component-wise addition from the two input tuples
        
        t = tuple()
        for i in range(0, len(t1)):
            if t1[i] == None:
                t += None,
            else:
                t += t1[i] + t2[i],
        return t

    def subtractTuples(self,t1,t2):
        
        # returns a new tuple constructed
        # by component-wise subtraction from the two input tuples
        
        t = tuple()
        for i in range(0, len(t1)):
            if t1[i] == None:
                t += None,
            else:
                t += t1[i] - t2[i],
        return t

    def decrementTuple(self,t, pos = 1):

        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position decremented by 1.

        new_t = tuple()
        for i in range(len(t)):
            if t[i] == None:
                new_t += None,
            elif i == pos:
                new_t += t[i] - 1,
            else:
                new_t += t[i],

        return new_t

    def fillTuple(self, t, fill=0, l = None):

        # This function fills up a give tuple t with fill f until the
        # lenght of the tuple is l
        # if l is not given, l defaults to dimensions +1

        if l == None:
            l = self.max_dimensions +1
        if l == 0:
            return (None,)
        while len(t) < l:
            t += fill,
        return t

    def incrementTuple(self,t, dim = 1):

        # Inputs: t, a tuple
        #         dim, the dimension to increment
        # output: a new tuple identical to the old, except that it has been incremented.

        new_t = tuple()
        for i in range(len(t)):
            if t[i] == None:
                new_t += None,
            elif i == dim:
                new_t += t[i] + 1,
            else:
                new_t += t[i],

        return new_t


    def incrementTupleWithCarry(self, t, dim = 1, boundary = None):
        
        # Input: t, a tuple
        #        dim, the dimension to increment (defaults to 1)
        #        boundary, the tuple of maximum dimensions. If not specified, is set to self.rectangle

        # Output: the incremented tuple, with values of the boundary 'carried' to the next level
        #       unless the value of the position is None, or the Tuple is maxed out, in which cases
        #       the origen tuple is returned.

        boundary = self.rectangle if boundary == None else boundary

        if (t[dim] != None) and (dim < len(t) - 1):
            t = self.incrementTuple(t, dim)
            if t[dim] == boundary[dim]: # if position is at maximum value
                self.setTuplePositionXtoY(t, dim, 0) # set selected position to 0
                t = self.incrementTupleWithCarry(t, dim + 1) # and increment the next position
            return t
        else:
            return self.origen

    def setTuplePositionXtoY(self, t, x, y):
        
        # Inputs: a tuple t, the desired position x, and the new value y
        # output: a tuple that is identical to the input tuple, with the exception
        #   that it's xth position has been changed to y
    
        new_t = ()
        for i in range(len(t)):
            if i == x:
                new_t += (y,)
            else:
                new_t += (t[i],)
        return new_t

    def zeroHigherDimensions(self,t,dim):

        # Inputs: t, a tuple
        #         dim, the dimension above which the tuple should be zeroed
        # output: a new tuple identical to the old, except that it has been zeroed.

        new_t = tuple()
        for i in range(len(t)):
            if i <= dim:
                new_t += t[i],
            else:
                new_t += 0,
        return new_t



