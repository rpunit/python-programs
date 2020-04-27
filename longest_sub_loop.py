import sys,os


def longest_ss(arr) :
	prev_max = -100000000
	start = 0
	end = 0
	cur_max = 0
	for i in range(0, len(arr)) :
		cur_max = cur_max + arr[i] 
		if prev_max < cur_max : 
			prev_max = cur_max
			end = i
		
		if cur_max < 0 :
			cur_max = 0
			start = i + 1

	return (prev_max, start, i, arr[start: end+1])
				


aff = [ 1, 2, 3 ,-6, 5, 3 ,-8, 11]
aff = [ 1, 2, 3 , -7, 5, 3, -2, 11]


print(aff)
print (longest_ss(aff) )
