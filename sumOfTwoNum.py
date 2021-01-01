

def printIfSum ( a, tot ):
	a.sort() 
	i,j = 0, len(a) -1

	
	while (i < j) :


		if a[i] +  a[j] >  tot :
			j -= 1

		if a[j] + a[i] == tot :
			return True
		
		if a[j] + a[i] <  tot :
			i += 1

	return False



a = [1,4,45,6,10,8]

print(printIfSum(a,49))
