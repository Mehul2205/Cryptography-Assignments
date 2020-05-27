r1 = int(input('Enter the larger of the two numbers '))
r2 = int(input('Enter the other number '))
s1 = 1
s2 = 0
t1 = 0
t2 = 1
while r2 > 0:
	q = r1 // r2
	r = r1 % r2
	s = s1 - s2*q
	t = t1 - t2*q
	r1 = r2
	r2 = r
	s1 = s2
	s2 = s
	t1 = t2
	t2 = t
print('The GCD of the numbers is ', r1)
