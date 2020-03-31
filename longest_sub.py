import sys,os


def longest_ss(index, arr, prev_sum) :
	print(index, prev_sum)
	if index == len(arr) - 1 :
		return max (prev_sum, prev_sum + arr[index]) 

	if prev_sum  + arr[index] < 0 :
		return max ( prev_sum,  longest_ss(index + 1 , arr, prev_sum))

	return max ( prev_sum,  longest_ss(index + 1, arr, prev_sum + arr[index ]))
	


aff = [ 1, 2, 3 -6, 5, 3 -8, 11]
aff = [ 1, 2, 3 -6, 5, 3 -2, 11]


print (longest_ss(0, aff , 0) )
