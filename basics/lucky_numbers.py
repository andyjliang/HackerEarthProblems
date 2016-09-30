def binarySearch(arr, num):
	l = len(arr)
	if l == 1:
		return arr[0]
	m = l//2
	if arr[m-1] < num <= arr[m]:
		return arr[m]
	elif num >= arr[m-1]:
		return binarySearch(arr[m:], num)
	else:
		return binarySearch(arr[:m], num)

mem = []
n = 100
for i in range(n):
	for j in range(1+i,n):
		if j > i:
			mem.append((1<<i)+(1<<j))
mem= sorted(mem)
	
for _ in range(int(raw_input())):
	k = int(raw_input())
	i = mem.index(binarySearch(mem,k))
	s = sum(mem[:i])
	print s % 1000000007
