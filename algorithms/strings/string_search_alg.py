'''
Knuth-Morris-Pratt: also pre-analyzes the pattern, but tries to re-use whatever was already matched 
in the initial part of the pattern to avoid having to rematch that. This can work quite well, if your 
alphabet is small (f.ex. DNA bases), as you get a higher chance that your search patterns contain 
reuseable subpatterns.
'''
def prefix_function(p) :
	lp = len(p)
	prefix = [0] * lp
	j = 0
	for i in range(1,lp) :
		while j>=0 and p[j] != p[i] :
			if j-1 >= 0 :
				j = prefix[j-1]
			else :
				j-=1
		j+=1
		prefix[i] = j
	return prefix
	
def kmp_algorithm(p,t) :
	lp = len(p)
	lt = len(t)
	prefix_array = prefix_function(p)
	j = 0
	count = 0
	for i in range(lt)  :
		while j>=0 and p[j] != t[i] :
			if j-1 >= 0 :
				j = prefix_array[j-1]
			else :
				j-=1
		j+=1
		if j==lp :
			j=prefix_array[j-1]
			count+=1
	return count

'''
Aho-Corasick: Needs a lot of preprocessing, but does so for a number of patterns. If you 
know you will be looking for the same search patterns over and over again, then this is 
much better than the other, because you need to analyse patterns only once, not once per 
search
''' 

'''
Boyer-Moore: works by pre-analyzing the pattern and comparing from right-to-left. If a mismatch occurs, the initial analysis is used to determine how far the pattern can be shifted w.r.t. the text being searched. This works particularly well for long search patterns. In particular, it can be sub-linear, as you do not need to read every single character of your text.
'''

'''
Rabin-Karp
'''