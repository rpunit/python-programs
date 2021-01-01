
def kLargest(arr, k ) :
	ma = []

	for i,a in enumerate(arr) :
		
		if  len(ma)  < k :
			ma.append(a) 	
			ma = sorted(ma, reverse=True)
		else :
			if a > ma[-1]  :
				ma[-1] = a
				ma = sorted(ma, reverse=True)

	return ma
		
			




# Driver program 
arr = [1, 23, 12, 9, 30, 2, 50] 
# n = len(arr) 
k = 3
print(kLargest(arr, k) )
