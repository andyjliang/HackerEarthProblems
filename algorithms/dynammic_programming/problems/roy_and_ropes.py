'''
Roy lit the rope on fire from the left end. This fire burns down the rope by 
1 meter/minute. 
Your task is to find how much time (in minutes) will the fire take to burn down the entire rope.

Input: 
First line contains T - number of test cases.
First line of each test case contains L - length of the rope.
Second line of each test case contains L-1
L−1 integers separated by space denoting lengths of all the upper ropes at each meter.
Third line of each test case contains L-1
L−1 integers separated by space denoting lengths all the lower ropes at each meter.
'''

t = int(raw_input())

for _ in range(t):

	rope_length = int(raw_input())
	upper_rope_lengths = [int(x) for x in raw_input().split()]
	lower_rope_lengths = [int(x) for x in raw_input().split()]
	minutes_taken = 1
	estimated_more_minutes = 0
	for i in range(0, rope_length-1):
		curr_rope_time = max(upper_rope_lengths[i], lower_rope_lengths[i])
		if curr_rope_time > estimated_more_minutes:
			estimated_more_minutes = curr_rope_time
		estimated_more_minutes =  estimated_more_minutes - 1 if estimated_more_minutes > 0 else 0
		minutes_taken += 1
	print estimated_more_minutes + minutes_taken

# 10
# 6
# 0 1 0 1 0
# 1 1 1 0 0
# 3
# 0 1
# 0 1
# 2
# 1
# 0
# 2
# 1
# 1
# 7
# 1 0 0 0 0 0
# 1 0 0 0 0 0
# 6
# 1 1 1 1 1
# 0 0 1 0 0
# 4
# 0 0 0
# 0 0 0
# 10
# 0 0 0 0 1 0 0 0 0
# 0 0 1 1 1 0 0 0 1
# 10
# 0 0 0 0 1 1 0 1 0
# 0 1 1 0 0 1 1 0 1
# 2
# 0
# 0