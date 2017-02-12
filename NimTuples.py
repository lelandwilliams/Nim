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
        
        t = tuple()
        for i in range(0, len(t1)):
            if t1[i] == None:
                t += None,
            else:
                t += t1[i] + t2[i],
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

    def incrementTuple(self,t, pos = 1):

        # this function takes in a tuple and a dimension,
        # and returns the tuple but with the value in the given
        # position incremented by 1.

        new_t = tuple()
        for i in range(len(t)):
            if t[i] == None:
                new_t += None,
            elif i == pos:
                new_t += t[i] + 1,
            else:
                new_t += t[i],

        return new_t


    def incrementTupleWithCarry(self,t,pos = 1):
        
        # Input: a tuple, t & the position to increment (defaults to 1)
        # Output: the incremented tuple, with values of the boundary 'carried' to the next level
        #       unless the value of the position is None, or the Tuple is maxed out, in which cases
        #       the original tuple is returned.

        if (t[pos] != None) and (pos < len(t) - 1):
            if t[pos] == self.explored_region[pos]: # if position is at maximum value
                self.TuplePositionXtoY(t, pos, 0) # set selected position to 0
                t = self.incrementTupleWithCarry(t,pos + 1) # and increment the next position

        return t

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



