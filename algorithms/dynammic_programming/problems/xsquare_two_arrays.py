'''
Xsquare loves to play with arrays a lot. Today, he has two arrays named as A and B. Each array consists of N positive integers.

Xsquare has decided to fulfill following types of queries over his array A and array B.

1 L R : Print the value of AL + BL+1 + AL+2 + BL+3 + ... upto Rth term.
2 L R : Print the value of BL + AL+1 + BL+2 + AL+3 + ... upto Rth term.
Input
First line of input contains two space separated integers N and Q denoting the size of arrays ( A , B ) and number of queries respectively. Next N lines of input contains N space separated integers denoting array A. Next line of input contains N space separated integers denoting array B. Next Q lines of input contains Q queries (one per line). Each query has one of the above mentioned types.

Output
Output consists of Q lines, each containing answer to the corresponding query.
'''
from numpy import zeros
(n, q) = (int(x) for x in raw_input().split())

A = raw_input().split()
B = raw_input().split()
ziz_zag_arrays = zeros((2,n), dtype=int)
for i in range(n):
	ziz_zag_arrays[0][i] = int(A[i]) if i%2==0 else int(B[i])
	ziz_zag_arrays[1][i] = int(B[i]) if i%2==0 else int(A[i])
	ziz_zag_arrays[0][i] += ziz_zag_arrays[0][i-1]
	ziz_zag_arrays[1][i] += ziz_zag_arrays[1][i-1]

for _ in range(q):
	(which_array, l, r) = (int(x) for x in raw_input().split())
	
	i = abs(which_array-1-1) if l%2==0 else which_array-1
	print ziz_zag_arrays[i][r-1] - ziz_zag_arrays[i][l-2] if l>1 else ziz_zag_arrays[i][r-1]
	