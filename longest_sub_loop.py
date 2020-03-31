import sys,os


def longest_ss(arr) :
	prev_max = -100000000
	cur_max = 0
	for i in range(0, len(arr)) :
		cur_max = cur_max + arr[i] 
		if prev_max < cur_max : 
			prev_max = cur_max
		
		if cur_max < 0 :
			cur_max = 0

	return prev_max
				


aff = [ 1, 2, 3 -6, 5, 3 -8, 11]
aff = [ 1, 2, 3 -6, 5, 3 -2, 11]


print (longest_ss(aff) )
