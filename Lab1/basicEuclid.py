def gcd(a, b):
	if a == 0:
		return b
	return gcd(b % a, a)
a = int(input('Enter the larger of the two numbers'))
b = int(input('Enter the other number'))
print('The GCD of the numbers is : ', gcd(a, b))
