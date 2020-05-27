def extendedMultiInverse():
	b = int(input('Enter the number whose multiplicative inverse has to be found '))
	n = int(input('Enter the residue set length '))
	r1 = n
	r2 = b
	t1 = 0
	t2 = 1
	while r2 > 0:
		q = r1 // r2
		r = r1 % r2
		t = t1 - q*t2
		r1 = r2
		r2 = r
		t1 = t2
		t2 = t
	print(t1, t2)

def extendedAdditiveInverse():
	b = int(input('Enter the number whose additive inverse has to be found out '))
	n = int(input('Enter the length of the residual set '))
	print(n - b)

extendedAdditiveInverse()
extendedMultiInverse()
