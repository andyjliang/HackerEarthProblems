'''
You are given a N∗MN∗M matrix. You need to print the sum of all the numbers in the rectangle which has (1,1)(1,1) as the top left corner and (X,Y)(X,Y) as the bottom right corner.Input:First line contains two integers, NN and MM, number of rows and number of columns in the matrix.Next NN lines contains MM space separated integers, elements of the matrix.Next line contains an integer, QQ, number of queries.Each query contains two space separated integers, XX and YY.Output:For each query, print the sum of all the numbers in the rectangle which has (1,1)(1,1) as the top left corner and (X,Y)(X,Y) as the bottom right corner.Constraints: 1≤N,M≤1031≤N,M≤103 1≤1≤ elements of matrix ≤103≤103 1≤X≤N1≤X≤N 1≤Y≤M1≤Y≤M 1≤Q≤105
'''

(n,m) = (int(x) for x in raw_input().split())
matrix = []
for _ in range(n):
	matrix.append([int(x) for x in raw_input().split()])

mem_matrix = {}
for i in range(n):
	for j in range(m):
		if i == 0 and j ==0:
			mem_matrix[(i,j)] = matrix[i][j]
		elif i == 0:
			mem_matrix[(i,j)] = mem_matrix[(i,j-1)] + matrix[i][j]
		elif j == 0:
			mem_matrix[(i,j)] = mem_matrix[(i-1,j)] + matrix[i][j]
		else:
			mem_matrix[(i,j)] = mem_matrix[(i,j-1)] + mem_matrix[(i-1,j)] - mem_matrix[(i-1,j-1)] + matrix[i][j]

for _ in range(int(raw_input())):
	query = tuple([int(x)-1 for x in raw_input().split()]
	print mem_matrix[query]