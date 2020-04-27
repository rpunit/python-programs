import sys,os


def longest_ss(index, arr, prev_sum) :
	print(index, prev_sum)
	if index == len(arr) - 1 :
		return max (prev_sum, prev_sum + arr[index]) 

	if prev_sum  + arr[index] < 0 :
		return max ( prev_sum,  longest_ss(index + 1 , arr, prev_sum))

	return max ( prev_sum,  longest_ss(index + 1, arr, prev_sum + arr[index ]))


def longest_ss1(arr ) :
	i = 0
	prevs = 0
	while i < len(arr)  :
		sum1 = arr[i]
		for j in range(i+1, len(arr)) :
			sum1 += arr[j]  
			if sum1 < 0:
				print("--",i,j, arr[j])
				i = j + 1
				break

		if sum1 > prevs :
			prevs = sum1
		if j == len(arr) - 1:
			break
		i += 1

	return prevs
			
	


aff = [ 1, 2, 3 -7, 5, 3 -8, 11]
#aff = [ 1, 2, 3 -6, 5, 3 -2, 11]


print (longest_ss(0, aff , 0) )
print (longest_ss1(aff) )
print (longest_ss1(aff) )
