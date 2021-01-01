# Calculate the max product of 3 initigers in a array
"""
Approach 2: O(n) Time, O(n) Space

Construct four auxiliary arrays leftMax[], rightMax[], leftMin[] and rightMin[] of same size as input array.
Fill leftMax[], rightMax[], leftMin[] and rightMin[] in below manner.
leftMax[i] will contain maximum element on left of arr[i] excluding arr[i]. For index 0, left will contain -1.
leftMin[i] will contain minimum element on left of arr[i] excluding arr[i]. For index 0, left will contain -1.
rightMax[i] will contain maximum element on right of arr[i] excluding arr[i]. For index n-1, right will contain -1.
rightMin[i] will contain minimum element on right of arr[i] excluding arr[i]. For index n-1, right will contain -1.
For all array indexes i except first and last index, compute maximum of arr[i]*x*y where x can be leftMax[i] or leftMin[i] and y can be rightMax[i] or rightMin[i].
Return the maximum from step 3.

"""
def maxProduct(arr ) :

	n = len (arr)
	leftMinArr = [-1] *n
	leftMaxArr = [-1] *n
	rightMaxArr = [-1] *n
	rightMinArr = [-1] *n
	
	minVal = arr[0] 
	maxVal = arr[0] 

	for i in range(1, n) :
		if arr[i] < minVal :
			minVal = arr[i] 
		leftMinArr[i] = minVal 
		

		if arr[i] > maxVal :
			maxVal = arr[i] 
		leftMaxArr[i] = maxVal 

	minVal = arr[n-1] 
	maxVal = arr[n-1] 
		
	for i in range(1, n) :
		if arr[n-1-i] < minVal :
			minVal = arr[n-1-i] 
		rightMinArr[n-1-i] = minVal 

		if arr[n-1-i] > maxVal :
			maxVal = arr[n-1-i] 
		rightMaxArr[n-1-i] = maxVal 

	maxMult = -1

	for i in range(1,n-1) :
		maxv = max ( leftMaxArr[i-1]*arr[i]*rightMaxArr[i+1],
					leftMaxArr[i-1]*arr[i]*rightMinArr[i+1],
					leftMinArr[i-1]*arr[i]*rightMinArr[i+1],
					leftMinArr[i-1]*arr[i]*rightMaxArr[i+1])

		if maxv > maxMult :
			maxMult = maxv

	return maxMult


arr = [ 1, 4, 3, -6, -7, 0 ]


print (maxProduct(arr))
		


