def calc_fibonacci(num):
	if num - 1 == 0:
	 	return 1
	if num - 2 == 0:
		return 1
	
	n = calc_fibonacci(num - 1) + calc_fibonacci(num - 2)
	
	return n

def test_fib():
	assert calc_fibonacci(3) == 2
	assert calc_fibonacci(2) == 1
	assert calc_fibonacci(1) == 1
