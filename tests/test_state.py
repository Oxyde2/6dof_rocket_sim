import unittest
from sim.initial_conditions import State

class TestInitialConditions(unittest.TestCase):
	
	def test_neg_t0(self):
		self.assertEqual(State([1], -1), "t0 must be a natural scalar")