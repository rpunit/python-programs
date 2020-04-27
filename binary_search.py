



def bsearch(arr, x, left, right) :


	if left >right :
		return False

	mid = (left + right)//2

	if x == arr[mid] :
		return True

	if x < arr[mid] :
		return bsearch(arr, x, left, mid -1)

	else :
		return bsearch(arr, x, mid + 1, right)




arr = [ 1,2,4,5,7,8,3]


print (bsearch(arr, 4, 0, len(arr)))
		
