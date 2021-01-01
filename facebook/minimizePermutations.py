import math
"""
Minimizing Permutations
In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

"""
# Add any extra import statements you may need here


# Add any helper functions you may need here
def elementsNotInPlace(arr) :
	out = []
	for i,a in enumerate(arr) :
		if arr[i] != i + 1 :
			out.append(i)
	return out

def findBestMatch(arr) :
	for i in range(len(arr)) :
		for j in range(i+1,len(arr)) :
			if i+1 == arr[j] and j+1 == arr[i] :
				return (i,j)
	return(arr[0], arr[1])

def minOperations(arr):
	# Write your code here
	
	iarr = elementsNotInPlace(arr)
	count = 0
	while (len(iarr) > 0) :
		print(arr)
		
		count +=1 
		iarr = elementsNotInPlace(arr)
		print("iarr", iarr)
		(i,j) = findBestMatch(iarr)
		print(i,j)
		arr[i], arr[j] = arr[j],arr[i]
		iarr = elementsNotInPlace(arr)
	return count
	


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
	print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printInteger(expected)
		print(' Your output: ', end='')
		printInteger(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	n_1 = 5
	arr_1 = [1, 2, 5, 4, 3]
	expected_1 = 1
	output_1 = minOperations(arr_1)
	check(expected_1, output_1)

	n_2 = 3
	arr_2 = [3, 1, 2]
	expected_2 = 2
	output_2 = minOperations(arr_2)
	check(expected_2, output_2)
	
	# Add your own test cases here
	
