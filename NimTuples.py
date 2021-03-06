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
        assert len(t1) == len(t2)

        t = tuple()
        for i in range(0, len(t1)):
            if t1[i] == None:
                t += None,
            else:
                t += (t1[i] + t2[i]),
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

        assert dim < len(t)

        new_t = tuple()
        for i in range(len(t)):
            if t[i] == None:
                new_t += None,
            elif i == dim:
                new_t += t[i] + 1,
            else:
                new_t += t[i],

        return new_t

    def incrementTupleWithCarry(self, tup, d = 1):
        t = tup
        dim = d
        carry_flag = True

        while (dim < len(t)) and carry_flag is True:
            self.inc_dim = dim
            t = self.incrementTuple(t, dim)
            if t[dim] > self.rectangle[dim]:
                t = self.setTuplePositionXtoY(t, dim, 0)
                dim += 1
            else:
                carry_flag = False

        self.overflow = (dim == len(t))
        return t

    def incrementTupleWithCarryExclusive(self, tup, d = 1):
        t = tup
        dim = d
        carry_flag = True

        while (dim < len(t)) and carry_flag is True:
            self.inc_dim = dim
            t = self.incrementTuple(t, dim)
            if t[dim] >= self.rectangle[dim]:
                t = self.setTuplePositionXtoY(t, dim, 0)
                dim += 1
            else:
                carry_flag = False

        self.overflow = (dim == len(t))
        return t


    def setTuplePositionXtoY(self, t, x, y):
        
        # Inputs: a tuple t, the desired position x, and the new value y
        # output: a tuple that is identical to the input tuple, with the exception
        #   that it's xth position has been changed to y
    
        new_t = tuple()
        for i in range(len(t)):
            if i == x:
                new_t += (y,)
            else:
                new_t += t[i],

        assert type(new_t) == type(tuple())
        return new_t

    def zeroTupleBelow(self, t, dim):

        # Inputs: t, a tuple
        #         dim, the dimension below which the tuple should be zeroed
        # Output: a new tuple identical to the old, 
        #   except that the first (d -1) dimensions have been 
        #   set to zero.

        new_t = t
        i= 1
        for entry in t[1:]:
            if i < dim:
                new_t = self.setTuplePositionXtoY(new_t,i,0)
            else:
                new_t = self.setTuplePositionXtoY(new_t,i,t[i])
            i += 1
        return new_t

    def zeroTupleAbove(self, t, dim):

        # Inputs: t, a tuple
        #         dim, the dimension above which the tuple should be zeroed
        # Output: a new tuple identical to the old, 
        #   except that the first (d -1) dimensions have been 
        #   set to zero.

        new_t = t
        i= 0
        for entry in t:
            if (not (t is None)) and i > dim:
                new_t = self.setTuplePositionXtoY(new_t,i,0)
            else:
                new_t = self.setTuplePositionXtoY(new_t,i,t[i])
            i += 1
        return new_t
