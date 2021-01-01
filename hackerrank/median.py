

def partition (arr, start, end ) :
	
	part = arr[end]	
	i = 0
	j = end - 1 

	while i <= j :
		while i < len(arr) and arr[i] <  part :
			i+=1
		
		while j > 0 and arr[j] >  part :
			j-=1

		if i <= j:
			arr[i], arr[j] = arr[j], arr[i] 

	arr[end],arr[i] = arr[i], arr[end]	

	return i


arr = [1,3,6,7,8]
arr = [1,3,6,7,8,2]
arr = [10, 6,1,9,3,7,4,8]
print (arr)
print (partition (arr, 0, len(arr)-1))
print (arr)
		

def quickSelect (arr, start, end, index) :


	#print (start, end,  arr)
	if start>= end :
		return 0

	pi = partition (arr, start, end)

	if pi == index :
		print (pi, arr[pi], arr)
		return arr[pi]
	v1 = quickSelect(arr, start, pi-1, index)
	v2 = quickSelect(arr, pi+1, end, index)

	return v1 + v2




def getMedian (arr) :
	index = 0
	if len(arr) % 2 == 1 :
		index = len(arr)//2
		print(index)
		return quickSelect (arr, 0, len(arr)-1, index) 
	else :
		index1 = len(arr)//2 - 1
		index2 = len(arr)//2 
		print(index1,index2)
		return (quickSelect (arr, 0, len(arr)-1, index1)  + \
			 quickSelect (arr, 0, len(arr)-1,index2) )/2  


	quickSelect (arr, 0, len(arr)-1, index) 

	return medians
		
arr = [10, 6,1,9,3,7,4,8]
print(sorted(arr))
print (getMedian(arr))
