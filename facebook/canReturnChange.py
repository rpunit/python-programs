import math
# Add any extra import statements you may need here
from collections import defaultdict

# Add any helper functions you may need here
def recurse(targetMoney, index, denoms, memo) :
	if targetMoney == 0 :
		return True
	if index >= len(denoms) :
		return False
	count = 1
	res = False
	if (targetMoney, index + 1) in memo :
		return memo[targetMoney, index + 1]
	while denoms[index] * count <= targetMoney :
		# 1 . Use current denomination :
		res |= recurse(targetMoney - denoms[index]*count, index + 1, denoms, memo)
		count += 1
	#	2 do not use current denom	
	f2 = recurse(targetMoney, index + 1, denoms, memo)
	memo[(targetMoney, index+1)] = f2 or res
	return f2 or res

def canGetExactChange(targetMoney, denominations):
	# Write your code here
	memo = defaultdict(bool)
	
	ret =  recurse(targetMoney, 0, denominations, memo)
	print(memo)
	return ret
	
	











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
	print('[\"', string, '\"]', sep='', end='')

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
		printString(expected)
		print(' Your output: ', end='')
		printString(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	target_1 = 94
	arr_1 = [5, 10, 25, 100, 200]
	expected_1 = False
	output_1 = canGetExactChange(target_1, arr_1)
	check(expected_1, output_1)

	target_2 = 75
	arr_2 = [4, 17, 29]
	expected_2 = True
	output_2 = canGetExactChange(target_2, arr_2)
	check(expected_2, output_2)

	# Add your own test cases here
	
