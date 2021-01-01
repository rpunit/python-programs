# 1 2 3 4 5 
# i = 0 numRot 1 : 2 3 4 5 1 ,  i = 3 (4)  :  (len + i - d) % len
# i = 1     
def rotLeft(a,d) :
	arr = [0]*len(a)
	for i in range(len(a)) :
		nl = (i + len(a) - d ) % len(a)
		print(i,nl)
		arr[nl] = a[i]
	return arr



a = [1,2,3,4,5]
print(rotLeft(a,4))
