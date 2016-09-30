# Given an array of N elements, check if it is possible to obtain a sum of S, by choosing some (or none) elements of the array and adding them.

# Input:
# First line of the input contains number of test cases T. Each test case has three lines.
# First line has N, the number of elements in array.
# Second line contains N space separated integers denoting the elements of the array. 
# Third line contains a single integer denoting S.

# Output:
# For each test case, print "YES" if S can be obtained by choosing some(or none) elements of the array and adding them. Otherwise Print "NO".

# Note that 0 can always be obtained by choosing none.

from itertools import combinations
def check(A, _sum, n):
	if _sum == 0:
		return True
	for i_iter in range(1,n+1):
		for combination in combinations(A, i_iter):
			if sum(combination) == _sum:
				return True
	return False

for _ in range(int(raw_input())):
	n = int(raw_input())
	A = [int(x) for x in raw_input().split()]
	_sum = int(raw_input())
	print 'YES' if check(A, _sum, n) else 'NO'
