import heapq

def bubble_sort(items):
        """ Implementation of bubble sort """
        for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] > items[j+1]:
                                items[j], items[j+1] = items[j+1], items[j]     # Swap!

def insertion_sort(items):
        """ Implementation of insertion sort """
        for i in range(1, len(items)):
                j = i
                while j > 0 and items[j] < items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1

def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:

        mid = len(items) / 2        # Determine the midpoint and split
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)            # Sort left list in-place
        merge_sort(right)           # Sort right list in-place

        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if lval < rval or rval is None:
                items[i] = lval
                l += 1
            elif lval >= rval or lval is None:
                items[i] = rval
                r += 1


def quick_sort(items):
        """ Implementation of quick sort """
        if len(items) > 1:
                pivot_index = len(items) / 2
                smaller_items = []
                larger_items = []

                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val < items[pivot_index]:
                                        smaller_items.append(val)
                                else:
                                        larger_items.append(val)

                quick_sort(smaller_items)
                quick_sort(larger_items)
                items[:] = smaller_items + [items[pivot_index]] + larger_items

def heap_sort(items):
        """ Implementation of heap sort """
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]

            
def mergesort( aList ):
  _mergesort( aList, 0, len( aList ) - 1 )
 
 
def _mergesort( aList, first, last ):
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) / 2
  if first < last:
    _mergesort( aList, first, mid )
    _mergesort( aList, mid + 1, last )
 
  # merge solved pieces to get solution to original problem
  a, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )
 
  while f <= mid and l <= last:
    if aList[f] < aList[l] :
      tmp[a] = aList[f]
      f += 1
    else:
      tmp[a] = aList[l]
      l += 1
    a += 1
 
  if f <= mid :
    tmp[a:] = aList[f:mid + 1]
 
  if l <= last:
    tmp[a:] = aList[l:last + 1]
 
  a = 0
  while first <= last:
    aList[first] = tmp[a]
    first += 1
    a += 1

def merge(x, y):
    result = []
    while x and y:
        result.append(x.pop(0) if x[0] > y[0] else y.pop(0))
    result += x + y

    return result

def counting_sort(array):
    k = max(array)
    aux = [0]*k
    for v in array:
        aux[v] += 1
    result = []
    for i in range(k):
        result += aux[i] * i
    return result
