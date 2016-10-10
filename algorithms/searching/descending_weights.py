'''
You have been given an array AA of size NN and an integer KK. This array consists of NN integers ranging from 11 to 107107. Each element in this array is said to have a Special Weight. The special weight of an element a[i]a[i] is a[i]%Ka[i]%K.You now need to sort this array in Non-Increasing order of the weight of each element, i.e the element with the highest weight should appear first, then the element with the second highest weight and so on. In case two elements have the same weight, the one with the lower value should appear in the output first.Input Format:The first line consists of two space separated integers NN and KK. The next line consists of NN space separated integers denoting the elements of array AA.Output Format:Print NN space separated integers denoting the elements of the array in the order in which they are required.
'''



(n,k) = map(int, raw_input().split())
A = map(int, raw_input().split())
A_mod = map(lambda x: x%k, A)
results = []

buckets = max(A_mod)+1
A_buckets = [[] for x in xrange(buckets)]
for i,v in enumerate(A_mod):
	A_buckets[v].append(A[i])
for i in xrange(buckets-1, -1, -1):
	results += A_buckets[i]
print ' '.join(map(str, results))