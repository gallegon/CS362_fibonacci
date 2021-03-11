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

