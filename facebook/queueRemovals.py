import math

"""
Queue Removals
You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:
1. Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
2. For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then push it back onto the queue
Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.

"""
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findPositions(arr, x):
	# Write your code here
	out = []
	newarr = []
	for i,a in enumerate(arr) :
		newarr.append((i+1,a))
	#print (newarr)	
	for i in range(x) :
		#print ("i,newarr", i, newarr)
		maxv = (0,-1)
		tq = []
		j=0
		n = len(newarr)
		while j < n and j< x :
			tup = newarr.pop(0)
			if tup[1] > maxv[1]:
				maxv = tup
			tq.append(tup)
			j+=1 
		#print(j, maxv)
		out.append(maxv[0])
		for tup in tq :
			if tup != maxv :
				newarr.append(tup if tup[1] <=0 else (tup[0],tup[1]-1))
	return out		
		
			

	









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
	print('[', n, ']', sep='', end='')

def printIntegerList(array):
	size = len(array)
	print('[', end='')
	for i in range(size):
		if i != 0:
			print(', ', end='')
		print(array[i], end='')
	print(']', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	expected_size = len(expected)
	output_size = len(output)
	result = True
	if expected_size != output_size:
		result = False
	for i in range(min(expected_size, output_size)):
		result &= (output[i] == expected[i])
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printIntegerList(expected)
		print(' Your output: ', end='')
		printIntegerList(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	n_1 = 6
	x_1 = 5
	arr_1 = [1, 2, 2, 3, 4, 5]
	expected_1 = [5, 6, 4, 1, 2]
	output_1 = findPositions(arr_1, x_1)
	check(expected_1, output_1)

	n_2 = 13
	x_2 = 4
	arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
	expected_2 = [2, 5, 10, 13]
	output_2 = findPositions(arr_2, x_2)
	check(expected_2, output_2)

	# Add your own test cases here
	
