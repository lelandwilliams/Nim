from NimReport import NimReport as Nim
import unittest

class TestNim(unittest.TestCase):
    def setUp(self):
        self.nim = Nim()

    def test_example1(self):
        self.nim.setDimensions(1)
        self.nim.run()
        self.assertEqual(len(self.nim.p_positions()), 1)
        self.assertEqual(self.nim.p_positions(), [(None,0)])
        self.assertEqual(self.nim.rectangle, (None,2))
        self.assertEqual(self.nim.preperiod, (None,0))

    def test_example2(self):
        self.nim.setDimensions(2)
        self.nim.run()
        self.assertEqual(len(self.nim.p_positions()), 1)
        self.assertEqual(self.nim.p_positions(), [(None,0,0)])
        self.assertEqual(self.nim.rectangle, (None,2,2))
        self.assertEqual(self.nim.preperiod, (None,0,0))

    def test_example3(self):
        self.nim.setMiserePlay()
        self.nim.setDimensions(2)
        self.nim.run()
        self.assertEqual(len(self.nim.p_positions()), 1)
        self.assertEqual(self.nim.p_positions(), [(None,0,0)])
        self.assertEqual(self.nim.rectangle, (None,2,2))
        self.assertEqual(self.nim.preperiod, (None,0,1))

    def test_example3_5(self):
        self.nim.setMiserePlay()
        self.nim.setDimensions(3)
        self.nim.run()
        self.assertEqual(len(self.nim.p_positions()), 4)
#       self.assertEqual(nim.p_positions, [(None,0,0)])
        self.assertEqual(self.nim.rectangle, (None,2,3,2))
        self.assertEqual(self.nim.preperiod, (None,0,1,1))
        self.assertEqual(self.nim.period(), (None,2,2,1))

def example4():
    a = Nim
    a.setMiserePlay()
    a.setDimensions(3)
    a.moves = [(None,-1,0,0,0),(None,0,-1,0,0),(None,1,-1,0,0),(None,0,1,-1,0),(None,1,0,0,0),(None,0,0,1,-1)]
    a.run()
    return a

if __name__=='__main__':
    unittest.main()

