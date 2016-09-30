'''
The Monk wants to buy some cities. To buy two cities, he needs to buy the road connecting those two cities. Now, you are given a list of roads, bought by the Monk. You need to tell how many cities did the Monk buy.

Input:
First line contains an integer T, denoting the number of test cases. The first line of each test case contains an integer E, denoting the number of roads. The next E lines contain two space separated integers X and Y, denoting that there is an road between city X and city Y.

Output:
For each test case, you need to print the number of cities the Monk bought.

Constraint:
1 <= T <= 100
1 <= E <= 1000
1 <= X, Y <= 10000
'''


# from collections import defaultdict

def Main():
	adj = set()

	t = int(raw_input())
	for _ in range(t):
		e = int(raw_input())
		for _x in range(e):
			(n1, n2) = raw_input().split()
			adj.add(n1)
			adj.add(n2)
		print len(adj)
		adj.clear()
		
if __name__ == "__main__":
	Main()