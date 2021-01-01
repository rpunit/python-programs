

def span (arr) :
	out = [0]*len(arr)

	stack = []
	stack.append(0)
	out[0] = 1
	for i in range(1,len(arr)) :
		print (stack) 
		while len(stack) > 0 and arr[stack[-1]] <= arr[i] :
			stack.pop(-1)

		if len(stack) == 0 :
			out[i] = i + 1 
		else :
			out[i] = i - stack[-1] 
		print (i, stack, out)
		
		stack.append(i)
	return out

a = [3, 4, 1, 6, 2]
print (a)
print(span(a)) 

