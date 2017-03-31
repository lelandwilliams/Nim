from NimReport import NimReport as Nim
import unittest

class TestNim(unittest.TestCase):
    def setUp(self):
        self.nim = Nim()

    def test_example1():
        nim.setDimensions(1)
        nim.run()
        self.assertEqual(len(nim.p_positions), 1)
        self.assertEqual(nim.p_positions, [(None,0)])
        self.assertEqual(nim.rectangle, (None,2))
        self.assertEqual(nim.preperiod, (None,0))

    def test_example2():
        nim.setDimensions(2)
        nim.run()
        self.assertEqual(len(nim.p_positions), 1)
        self.assertEqual(nim.p_positions, [(None,0,0)])
        self.assertEqual(nim.rectangle, (None,2,2))
        self.assertEqual(nim.preperiod, (None,0,0))

    def test_example3():
        nim.setDimensions(2)
        nim.setMiserePlay
        nim.run()
        self.assertEqual(len(nim.p_positions), 1)
        self.assertEqual(nim.p_positions, [(None,0,0)])
        self.assertEqual(nim.rectangle, (None,2,2))
        self.assertEqual(nim.preperiod, (None,0,0))

def example3_5():
    a = Nim
    a.setMiserePlay()
    a.setDimensions(3)
    a.run()
    return a

def example4():
    a = Nim
    a.setMiserePlay()
    a.setDimensions(3)
    a.moves = [(None,-1,0,0,0),(None,0,-1,0,0),(None,1,-1,0,0),(None,0,1,-1,0),(None,1,0,0,0),(None,0,0,1,-1)]
    a.run()
    return a

def runExamples():

