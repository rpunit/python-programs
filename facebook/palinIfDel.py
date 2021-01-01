



"""
A B C

"""
def isPalin (arr, i, j, cnt) :
	if i == j :
		return True
	mid = (j +1 -i)//2 
	print (i, j, arr[i], arr[j], cnt)
	if  j == i + 1 and cnt > 0   : 
		if arr[i] == arr[j] :
			return True
		else :
			return False
			
	
	# case 1. i,j match
	if arr[i] == arr[j] :
		return isPalin(arr, i+1, j-1, cnt)
	
	if cnt > 0 :
		return False

	# case 2. delete i
	if  isPalin(arr, i+1, j, cnt + 1) :
		return True
	else :
		# case 3. delete j
		return  isPalin(arr, i, j-1, cnt + 1)



s = "NABCBAK"

print (isPalin(s,0 , len(s) -1, 0))
