import unittest
import fibonacci

class Test_fibonacci(unittest.TestCase):
	
	def test_one(self):
		self.assertEqual(fibonacci.calc_fibonacci(1), 1)
	def test_two(self):
		self.assertEqual(fibonacci.calc_fibonacci(2), 1)
	def test_three(self):
		self.assertEqual(fibonacci.calc_fibonacci(3), 2)

if __name__ == '__main__':
	unittest.main()
