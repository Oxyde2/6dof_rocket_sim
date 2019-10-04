import sys
import unittest
import numpy as np
sys.path.append('D:\6dof_rocket_sim\sim\iters.py')
import iters

class TestEulerStep(unittest.TestCase):
	
	def test_neg_tStep(self):
		self.assertEqual(iters.euler_step(-1, -9.81, 0),'tStep is < 0', 'tStep must be larger than 0')
		
	def test_rand_large_array(self):
		xn = 100000*np.random.rand(1,10)
		yn = 100000*np.random.rand(1,10)
		self.assertTrue(len(iters.euler_step(1,xn,yn)) == len(xn), 'output array should match input array length')
	
	def test_standard_array(self):
		xn = -1*np.ones(500)
		yn = np.zeros(500)
		ynp1 = iters.euler_step(1,xn,yn)
		for i in ynp1:
			if i != -1:
				incorrect = 1
			else:
				incorrect = 0
		self.assertFalse(incorrect, 'output array is predetermined to all be -1, and they are not')
		
	def test_mult_steps(self):
		xn = -9.81
		yn = 0
		tn = 0
		tf = 10
		tStep = .005
		while tn < 10:
			ynp1 = iters.euler_step(tStep,xn,yn)
			tn +=tStep
			yn = ynp1
		self.assertTrue((abs(yn-(-98.1)) < 10**-3), 'error should be relatively low for many iterations with a small tStep')
		
	def test_xn_empty(self):
		self.assertEqual(iters.euler_step(.001,[],0),'xn cannot be empty')
		
	def test_yn_empty(self):
		self.assertEqual(iters.euler_step(.001,0,[]),'yn cannot be empty')
		
	def test_xn_none(self):
		self.assertEqual(iters.euler_step(.001,[None],0),'xn cannot have any None')
	
	def test_yn_none(self):
		self.assertEqual(iters.euler_step(.001,0,[None]),'yn cannot have any None')
	
	def test_xn_imaginary(self):
		self.assertEqual(iters.euler_step(.001,[5j],0),'xn cannot have any imaginary numbers')
	
	def test_yn_imaginary(self):
		self.assertEqual(iters.euler_step(.001,0,[5j]),'yn cannot have any imaginary numbers')
	
	def test_tStep_imaginary(self):
		self.assertEqual(iters.euler_step(5j,0,0),'tStep is not real')
	
	def test_tStep_list(self):
		self.assertEqual(iters.euler_step([1,2,5],1,1),'tStep is not a scalar')
	
	def test_heck(self):
		self.assertEqual(iters.euler_step([1,2,5j],[51j+12,124324.12,12j+12j],[None]),'tStep is not a scalar')

if __name__ =='__main__':
	unittest.main()