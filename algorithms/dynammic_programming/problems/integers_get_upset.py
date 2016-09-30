'''
Puchi was crossing a river by jumping over stepping stones, carrying a bag containing N integers. Our Monk saw him from the banks and shouted out to him. Shaken by the sudden shout, Puchi dropped the bag in the river and all the integers got wet! This upset the integers.
There are N stepping stones available ahead. Puchi wants to dry these integers on these stones, such that each stone contains a single integer. The upset value of the i'th integer Ai (after rearrangement of the integers) is (Ai ^ Ai-1 ^ Ai-2) times Pi for i ≥ 2, and 0 otherwise. (where '^' is the bit wise XOR operator). Here, i represents the position of the said integer.

Puchi asks our Monk to find an order of arranging the numbers on the stones, such that sum of upset values is minimized. Help our Monk find the order, given the arrays A and P .
Input:
First line contains T. T test cases follow.
First line of each test case contains an integer N.
Second line of each test case contains N integers, forming the array A.
Third line of each test case contains N integers, forming the array P.

Output:
Print the answer to each test case in a new line.
'''
n_test_case = int(raw_input())
for _ in range(n_test_case):
	n_int = int(raw_input())
	A = raw_input().split()
	P = raw_input().split()

	assignment = [float('inf')]*2**n_int
	assignment[0] = 0

	for mask in range(2**n_int):
		for j in range(n_int):
			if (mask&(1<<j))>0:
				print mask|(1<<j), assignment[mask|(1<<j)]
				assignment[mask|(1<<j)] = min(assignment[mask|(1<<j)], assignment[mask])
	assignment[2**n_int-1]

def solve(mem, ns, ps, pos=0, old2=-1, old1=-1, used=0):
    if pos == len(ps): return 0
    key = (old2, old1, used)
    if key in mem: return mem[key]
 
    mini = float('inf')
    for i, n in enumerate(ns):
        if used & (1 << i): continue
        val = solve(mem, ns, ps, pos + 1, old1, n, used | (1 << i))
        if old2 >= 0: val += (old2 ^ old1 ^ n) * ps[pos]
        if val < mini: mini = val
    mem[key] = mini
    return mini
 
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        ns = map(int, raw_input().split())
        ps = map(int, raw_input().split())
        print solve({}, ns, ps)