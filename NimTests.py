from Nim import Nim
from NimBase import PlayCondition
import unittest

class TestNim(unittest.TestCase):

    def test_incrementTupleWithCarry(self):
        nim = Nim(4)
        nim.rectangle = (None,0,0,0,0)
        nim.incrementTupleWithCarry((None,1,1,1,1))
        self.assertTrue(nim.carry_dim)
        nim.rectangle = (None,2,2,2,2)
        t = nim.incrementTupleWithCarry(nim.origen)
        self.assertEqual(t, (None,1,0,0,0))
        self.assertFalse(nim.carry_dim)
        t = nim.incrementTupleWithCarry((None,2,2,0,0))
        self.assertEqual(t, (None,0,0,1,0))
        self.assertEqual(nim.carry_dim, 3)

    def test_setMoves(self):
        nim = Nim(2)
        self.assertEqual(len(nim.moves), 3)
        self.assertTrue((None,-1,0) in nim.moves)
        self.assertTrue((None,1,-1) in nim.moves)
        self.assertTrue((None,0,-1) in nim.moves)

        nim = Nim(6, 0.3122, PlayCondition.Misere)
        self.assertEqual(nim.rulecode, "0.312200")
        self.assertEqual(len(nim.moves), 12)


    def test_example1(self):
        nim = Nim(1)
        nim.run()
        self.assertEqual(len(nim.p_positions()), 1)
        self.assertEqual(nim.p_positions(), [(None,0)])
        self.assertEqual(nim.rectangle, (None,2))
        self.assertEqual(nim.preperiod, (None,0))

    def test_example2(self):
        nim = Nim(2)
        nim.run()
        self.assertEqual(len(nim.p_positions()), 1)
        self.assertEqual(nim.p_positions(), [(None,0,0)])
        self.assertEqual(nim.rectangle, (None,2,2))
        self.assertEqual(nim.preperiod, (None,0,0))

    def test_example3(self):
        nim = Nim(2,None, PlayCondition.Misere)
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

