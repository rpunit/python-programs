def recurse (k, A, B, index ) :

	#print(A,B,index)
	if index == len(A) -1:
		return A[index]  +  B[0] >= k

	a = A[index]
	ret = False
	for i,b in enumerate(B) :
		if a + b >= k:
			B1 = B.copy()
			B1.pop(i)
			ret = ret or  recurse(k, A, B1, index + 1)

	return ret

def sortCompare(k,A,B ) :
	A.sort()
	B.sort(reverse=True)
	for i in range(len(A)) :
		if A[i] + B[i] < k :
			print(A[i], B[i]) 
			return False

	return True

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    if recurse(k,A,B, 0) :
    #if sortCompare(k,A,B) :
        return "YES"
    else :
        return "NO"

A = [2,1,3]
B = [7,8,9]
k = 10

A = [1,2,2,1]
B = [3,3,3,4]
k = 5 

A=[4,4,3,2,1,4,4,3,2,4]
B=[2,3,0,1,1,3,1,0,0,2]
k = 4




print(twoArrays(k,A,B))
