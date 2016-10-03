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

n = int(raw_input())
arr = map(int, raw_input().split())
if arr[0] > arr[len(arr)-1]:
	arr = sorted(arr)
for _ in range(int(raw_input())):
	q = int(raw_input())
	print binary_search(arr, 0,len(arr), q)+1