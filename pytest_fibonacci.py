import pytest
import fibonacci

def test_fib():
	assert fibonacci.calc_fibonacci(1) == 1
	assert fibonacci.calc_fibonacci(2) == 1
	assert fibonacci.calc_fibonacci(3) == 2
	assert fibonacci.calc_fibonacci(4) == 3
	assert fibonacci.calc_fibonacci(5) == 5
	assert fibonacci.calc_fibonacci(6) == 8
	assert fibonacci.calc_fibonacci(7) == 13

def test_fact():
	assert fibonacci.factorial(1) == 1
	assert fibonacci.factorial(2) == 2
	assert fibonacci.factorial(3) == 6
	assert fibonacci.factorial(4) == 24
	assert fibonacci.factorial(5) == 120
	assert fibonacci.factorial(6) == 720
	
