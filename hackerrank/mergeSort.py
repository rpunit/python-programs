import random

def merge(a1, a2) :
	i = 0
	j = 0
	out = []
	while i < len(a1) and j < len(a2) :
		if a1[i] <= a2[j] :
			out.append(a1[i])
			i+=1
		elif a1[i] > a2[j] :
			out.append(a2[j])
			j+=1
	out.extend(a1[i:])
	out.extend(a2[j:])

	return out
		
		
	

def mergeSort (arr)  :

	if len(arr) == 1:
		return arr

	mid = len(arr)//2 
	print(mid, arr)
	a1 = mergeSort(arr[0: mid])
	a2 = mergeSort(arr[mid:len(arr)])
	print(a1, a2)

	res = merge(a1,a2)

	return res


arr = random.sample(range(0,10**6),10**6)
#arr = list(range(0,10**6))
#arr.reverse()

print(mergeSort(arr[:100]))
	
