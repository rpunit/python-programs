# Python program for brute force method to calculate stock span values 
# https://www.geeksforgeeks.org/the-stock-span-problem/

# Fills list S[] with span values 
def calculateSpan1(price, n, S): 
	
	# Span value of first day is always 1 
	S[0] = 1	
	for i in range(1, len(price)) :
		j = i - 1
		prev = price[i]
		while  j >= 0 and  price[j] <= price[i] :
			j -= 1	
			prev = price[j]  
	
		S[i] = i-j


# This is the linear time solution
def calculateSpan(price, n, S): 
	
	stack = []
	stack.append(0)
	# Span value of first day is always 1 
	S[0] = 1	
	
	print ("stock", price)
	for i in range(1,len(price)) :	
		
		# empty out the sack for all values less than cur val
		cur_price = price[i]
		while  len(stack) > 0 and price[stack[-1]] < cur_price  :
			stack.pop(-1)

		print (i,cur_price,  stack) 
		if len(stack) > 0 :
			S[i] = i - stack[-1]
		else :
			S[i] = i +1
		
		stack.append(i)	




						
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

