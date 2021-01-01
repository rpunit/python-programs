
#  1 4 6 3  8 4 2 
def merge(a, aux, start, mid, end) :
	for k in range(start,end+1) : 
		aux[k] = a[k]

	i = start 
	j = mid+1
	for k in range (start, end+1) :
		if i > mid  :
			a[k] = aux[j]
			j +=1 
		elif j > end :
			a[k] = aux[i]
			i +=1 
		elif aux[j] < aux[i] :
			arr[k] = aux[j]
			j+=1
		else:
			arr[k] = aux[i]
			i+=1
		
	

def _mergeSort (arr, aux, start, end)  :

	if start >= end :
		return 

	mid = start + (end - start)//2 
	#print(start, mid,end,  arr)
	_mergeSort(arr, aux, start, mid)
	_mergeSort(arr, aux, mid+1, end)
	merge(arr, aux, start, mid , end)

	return arr

def mergeSort(arr) :
	aux = [0]*len(arr) 
	return _mergeSort(arr, aux, 0, len(arr)-1)

arr = [ 1,5,2,9,4,2,6,7]
arr = list(range (10**9, 0, -1))

print(mergeSort(arr))
	
