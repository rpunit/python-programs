

def subSetSum(arr, index , total , res) :
	if index >= len(arr) :
		if total == 0 :
			return True
		else :
			return False

	if total == 0 :
		print (res) 
		return True


	# include the element
	res[index] = 1 
	ret1 =  subSetSum(arr, index + 1, total - arr[index], res)
	res[index] = 0 


	# do not include the element
	ret2 =  subSetSum(arr, index + 1, total, res)


	return ret1 or ret2





#arr = [1,5,11,5]
arr = [1,2,4,8,16,10, 41]
res = [0]*len(arr)
print (subSetSum(arr, 0, sum(arr)//2, res))
