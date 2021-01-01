def quicksort (arr, start, end ) :
	
	if (start >= end) :
		return arr
	index  = partition (arr, start, end )
	print(arr[start:end+1])
	quicksort ( arr, start, index -1)
	quicksort ( arr, index + 1, end)
	
	return arr 


def partition (arr, start, end):

	# Just pick first as pivot
	pivot = arr[start]
	starti = start + 1
	endi = end 
	left = []
	right = []
	while starti <= endi :
		if  arr[starti] < pivot :
			left.append(arr[starti])
		else :
			right.append(arr[starti])
		starti += 1
	res = left + [pivot] + right
	for i in range(len(res)) :
		arr[start + i] =  res[i]
	
	return start + len(left)


arr = [1,8,4,8,5,2,6,8]
arr = [4, 7, 3, 9, 1]
arr = [5,8,1,3,7,9,2]
print (quicksort(arr, 0, len(arr) -1))
