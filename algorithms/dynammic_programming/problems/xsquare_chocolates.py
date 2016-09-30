'''
Xsquare loves to eat chocolates like we all do. Xsquare's father has given him a chocolate bar B of length N where each chocolate piece is either of strawberry flavour S or of caramel flavour C. Xsquare's mom does not want him to eat all the chocolates as she thinks that consumption of too many chocolates will make him chocoholic. Therefore, she decided to take some chocolates back from him. She has some empty boxes to keep chocolates. Each box can contain exactly three chocolates. No box can contain all the chocolates of same flavour. She has ordered Xsquare to return her back, the longest contiguous sub-bar of the original chocolate bar such that she can place every three consecutive chocolates from that contiguous chocolate bar in an empty box. Each empty box can accomodate exactly three chocolates, neither less, nor more. A sub-bar is defined as contiguous peices of chocolates in some particular range.
Xsquare agrees to whatever his mom has ordered. Now, he is wondering how many chocolates he is able to eat at the end after he returns the longest contiguous sub-bar.
Help him in accomplishing this task.

Input :
First line of input contains a single integer T denoting the number of test cases. Each of the next T line of input contains a string B denoting the chocolate bar, where ith character in the jth line denotes the flavour of ith chocolate piece in jth chocolate bar.

Output :
Output consists of T lines, each containing number of chocolates Xsquare manages to eat at the end.
Constraints :

1 ≤ T ≤ 105
1 ≤ |B| ≤ 106
String B consists of character 'S' and 'C' only.
sum of |B| over all test cases does not exceed 106
Subtasks :

sum of |B| over all test cases does not exceed 106 : ( 40 pts )
sum of |B| over all test cases does not exceed 106 : ( 60 pts )
Warning :
'''
n_test_cases = int(raw_input())
for _ in range(n_test_cases):
	choco_s = raw_input()
	l_choco_s = len(choco_s)
	count_max = 0
	for i in range(3):
		count = 0
		for j in range(i,l_choco_s,3):
			if j+3 > l_choco_s: continue
			if choco_s[j:j+3] == 'SSS' or choco_s[j:j+3] == 'CCC':
				count_max = max(count_max, count)
				count = 0
			else: 
				count += 1
		count_max = max(count_max, count)
	print l_choco_s - count_max*3