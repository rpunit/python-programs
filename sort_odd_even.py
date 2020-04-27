

def sortOdd(x ) :
	if x%2 == 0 :
		return 0
	else :
		return 1

arr = [ 1,2,3,4,5,6,7,8]

arr.sort(key=sortOdd )

print(arr)
	
