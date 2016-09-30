def count(n):
	n = int(n)
	c = 0
	while n: 
		n=n&(n-1)
		c+=1
	return c

for _ in range(int(raw_input())):
	n = int(raw_input())
	print ' '.join(sorted([x for x in raw_input().split()], key=count))
