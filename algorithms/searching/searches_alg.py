def binary_search(array, low, high, key):
	while low < high:
		mid = (low+high)//2
		if arr[mid] < key:
			low=mid+1
		elif arr[mid]>key:
			high=mid-1
		else:
			return mid
	return low

def ternary_search(arr, l, r, x): # l is left part, r is right part, and x is search target
	if r>=1:
		mid1 = l+(r-1)//3
		mid2 = r-(r-1)//3
		if arr[mid1]==x:
			return mid1
		if arr[mid2]==x:
			return mid2
		if x<arr[mid1]:
			return ternary_search(1, mid1-1, x)
		elif x>arr[mid2]:
			return ternary_search(mid2+1, r, x)
		else:
			return ternary_search(mid1+1, mid2-1, x)
	return -1