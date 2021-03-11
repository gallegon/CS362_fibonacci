def calc_fibonacci(num):
	if num - 1 == 0:
	 	return 1
	if num - 2 == 0:
		return 1
	
	n = calc_fibonacci(num - 1) + calc_fibonacci(num - 2)

	return n

def factorial(num):
	if num == 0:
		return 1
	n = num * factorial(num - 1)
	return n

def main():
	print("Enter the ith term of fibonnaci number you want: ")
	print(">> ", end="")

	desired_fib = calc_fibonacci(int(input()))

	print(desired_fib)


if __name__ == '__main__':
	main()
