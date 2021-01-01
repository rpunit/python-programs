
"""
	 25,12,6,3,4

"""
def findSqRoot(N, start, end) :

	mid = (start + end) //2
	#print(N,mid)
	if mid <= 1 or start > end:
		return "No root"

	if mid*mid == N:
		return mid 

	elif mid*mid > N : 
		return findSqRoot (N, 0, mid-1)
	else :
		return findSqRoot (N, mid+1, end )
		

N = 152399025 
print (findSqRoot(N,0, (N+1)//2))

		
	
