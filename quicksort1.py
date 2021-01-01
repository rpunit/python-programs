
def quicksort (arr, start, end ) :
	
	index = partition (arr, start, end )
	if start < index -1:	
		quicksort ( arr, start, index -1)
	if  index < end:	
		quicksort ( arr, index + 1, end)
	
	return arr


def partition (arr, start, end):

	# Just pick mid as pivot
	pivot = arr[ end]
	i = start
	j = end - 1 
	while i <= j :
		while arr[i] < pivot :
			i += 1

		while arr[j] > pivot :
			j -= 1

		print("Swappning i, j", i, j, arr[i], arr[j])
		if i <= j :
			arr[i],arr[j] = arr[j], arr[i]
			i+=1
			j-=1
			
	arr[i],arr[end] = arr[end], arr[i]
	print (start, end, i, pivot,  arr) 
	# swap partion
	return i


#arr = [8,4,8,5,2,6,8,1]
arr = list("ABRACADABRA!")
#arr = [4, 7, 3, 9, 1]
print (arr)
print (quicksort(arr, 0, len(arr) -1))
