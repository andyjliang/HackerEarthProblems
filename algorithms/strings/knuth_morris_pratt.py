def prefix_func(s):
	n = len(s)
	f = [0] * n
	for i in range(1,n):
		j = f[i-1]
		while j > 0 and s[i] != s[j]:
			j = f[j-1]
		if s[i] == s[j]:
			j += 1 
		f[i] = j
	return f

p = raw_input()
t = raw_input()

lp = len(p)
lt = len(t)
prefix_arr = prefix_func(p)

j = 0 
count = 0
for i in range(lt):
	while j >= 0 and p[j] != t[i]:
		if j-1 >= 0:
			j = prefix_arr[j-1]
		else:
			j -= 1
	j += 1
	if j == lp:
		j = prefix_arr[j-1]
		count += 1

print count