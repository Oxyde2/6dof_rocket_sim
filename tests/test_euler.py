import unittest
import numpy as np
from euler import eulerStep

class TestEulerStep(unittest.TestCase):
	
	def test_neg_tStep(self):
		self.assertEqual(eulerStep(-1, -9.81, 0),'tStep is < 0', 'tStep must be larger than 0')
		
	def test_rand_large_array(self):
		xn = 100000*np.random.rand(1,10)
		yn = 100000*np.random.rand(1,10)
		self.assertTrue(len(eulerStep(1,xn,yn)) == len(xn), 'output array should match input array length')
	
	def test_standard_array(self):
		xn = -1*np.ones(500)
		yn = np.zeros(500)
		ynp1 = eulerStep(1,xn,yn)
		for i in ynp1:
			if i != -1:
				incorrect = 1
			else:
				incorrect = 0
		self.assertFalse(incorrect, 'output array is predetermined to all be -1, and they are not')

if __name__ =='__main__':
	unittest.main()