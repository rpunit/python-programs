


def quicksort (arr, start, end ) :
	
	if (start >= end) :
		return
	index = partition (arr, start, end )
	
	quicksort ( arr, start, index -1)
	quicksort ( arr, index + 1, end)
	
	return arr


def partition (arr, start, end):

	# Just pick last as pivot
	pivot = arr[end]
	starti = start
	endi = end - 1	
	while starti <= endi :
		while arr[starti] < pivot :
			starti += 1

		while arr[endi] > pivot :
			endi -= 1

		if starti <= endi :
			arr[starti],arr[endi] = arr[endi], arr[starti]
			starti += 1
			endi -= 1
			

	# swap partion
	arr[starti], arr[end] = arr[end], arr[starti]
	return starti


arr = [1,8,4,8,5,2,6,8]
print (quicksort(arr, 0, len(arr) -1))
