# Python program for brute force method to calculate stock span values 

# Fills list S[] with span values 
def calculateSpan(price, n, S): 
	
	# Span value of first day is always 1 
	S[0] = 1	
	for i in range(1, len(price)) :
		j = i - 1
		prev = price[i]
		while  j >= 0 and  price[j] <= price[i] :
			j -= 1	
			prev = price[j]  
	
		S[i] = i-j

						
# A utility function to print elements of array 
def printArray(arr, n): 

	for i in range(n): 
		print(arr[i], end = " ") 

# Driver program to test above function	 
price = [10, 4, 5, 90, 120, 80] 
n = len(price) 
S = [None] * n 

# Fill the span values in list S[] 
calculateSpan(price, n, S) 

# print the calculated span values 
printArray(S, n) 


# This code is contributed by Sunny Karira 

