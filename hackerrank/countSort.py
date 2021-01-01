import random


# see https://www.geeksforgeeks.org/counting-sort/
def countSort (arr, maxv ) :

	count = [0]*maxv
	
	# Step 1 get the counts :
	for a in arr :
		count[a] +=1 


	# step 2, get the cummulative counts
	for i in range(1,len(count)) :
		count[i] += count[i-1]


	out = [0]*len(arr)
	# step 3 
	for i in range(len(arr)) :
		out[ count[arr[i]] -1] = arr[i]
		count[arr[i]] -= 1

	return out


arr = []
maxv = 200 
for i in range(200000) :
	arr.append(random.randrange(maxv))
	
for i in range(100) :
	sorted(arr)
	#countSort(arr, maxv)
	
