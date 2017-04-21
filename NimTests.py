#from NimReport import NimReport as Nim
from Nim import Nim
import unittest

class TestNim(unittest.TestCase):

    def test_incrementTupleWithCarry(self):
        nim = Nim(4)
        nim.rectangle = (None,0,0,0,0)
        nim.incrementTupleWithCarry((None,1,1,1,1))
        self.assertTrue(nim.carry_dim)

    def test_setMoves(self):
        nim = Nim(2)
        nim.setNormalPlay()
        self.assertEqual(len(nim.moves), 3)
        self.assertTrue((None,-1,0) in nim.moves)
        self.assertTrue((None,1,-1) in nim.moves)
        self.assertTrue((None,0,-1) in nim.moves)


    def test_example1(self):
        nim = Nim(1)
        nim.run()
        self.assertEqual(len(nim.p_positions()), 1)
        self.assertEqual(nim.p_positions(), [(None,0)])
        self.assertEqual(nim.rectangle, (None,2))
        self.assertEqual(nim.preperiod, (None,0))

    def test_example2(self):
        nim = Nim(2)
        nim.setNormalPlay()
        nim.run()
        self.assertEqual(len(nim.p_positions()), 1)
        self.assertEqual(nim.p_positions(), [(None,0,0)])
        self.assertEqual(nim.rectangle, (None,2,2))
        self.assertEqual(nim.preperiod, (None,0,0))

    def test_example3(self):
        nim = Nim(2)
        nim.setMiserePlay()
        nim.run()
        self.assertEqual(len(nim.p_positions()), 2)
        self.assertTrue((None,1,0) in nim.p_positions())
        self.assertTrue((None,0,2) in nim.p_positions())
        self.assertEqual(nim.rectangle, (None,2,3))
        self.assertEqual(nim.preperiod, (None,0,1))

    def test_example3_5(self):
        nim = Nim(3)
        nim.setMiserePlay()
        nim.run()
        self.assertEqual(len(nim.p_positions()), 5)
        self.assertTrue((None,1,0,0) in nim.p_positions())
        self.assertTrue((None,0,2,0) in nim.p_positions())
        self.assertTrue((None,1,1,1) in nim.p_positions())
        self.assertTrue((None,0,0,2) in nim.p_positions())
        self.assertTrue((None,0,2,2) in nim.p_positions())
        self.assertEqual(nim.rectangle, (None,2,3,3))
        self.assertEqual(nim.preperiod, (None,0,1,1))
        self.assertEqual(nim.period(), (None,2,2,2))

    def test_example4(self):
        nim = Nim(4)
        nim.setMiserePlay()
        nim.moves = [(None,-1,0,0,0),(None,0,-1,0,0),(None,1,-1,0,0),(None,0,1,-1,0),(None,1,0,0,-1),(None,0,0,1,-1)]
        nim.run()
        self.assertEqual(len(nim.p_positions()), 8)
        self.assertTrue((None,1,0,0,0) in nim.p_positions())
        self.assertTrue((None,0,2,0,0) in nim.p_positions())
        self.assertTrue((None,0,0,1,0) in nim.p_positions())
        self.assertTrue((None,0,2,1,0) in nim.p_positions())
        self.assertTrue((None,1,0,0,1) in nim.p_positions())
        self.assertTrue((None,0,3,0,1) in nim.p_positions())
        self.assertTrue((None,0,1,1,1) in nim.p_positions())
        self.assertTrue((None,0,3,1,1) in nim.p_positions())
        self.assertEqual(nim.rectangle, (None,2,4,2,2))
        self.assertEqual(nim.preperiod, (None,0,2,1,0))
        self.assertEqual(nim.period(), (None,2,2,1,2))

if __name__=='__main__':
    unittest.main(exit=False)

