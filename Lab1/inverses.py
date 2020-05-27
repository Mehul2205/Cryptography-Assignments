def additiveInverse():
	n = int(input())
	arr = [i for i in range(n)]
	inverseArr = list()
	for i in range(len(arr) // 2 + 1):
		if i == 0:
			continue
		inverseArr.append((arr[i], arr[n - i]))
	print(inverseArr)
	
def multiplicativeInverse():
	n = int(input())
	arr = [i for i in range(n)]
	inverseArr = list()	
	for i in arr:
		for j in arr:
			if (i * j) % n == 1:
				inverseArr.append((i, j))
	print(inverseArr)
