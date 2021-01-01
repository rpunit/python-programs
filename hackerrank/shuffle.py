import random


def shuffle (arr) :
	l = len(arr)
	for i in range(l) :
		j = random.randrange(l) 
		arr[i],arr[j]  = arr[j], arr[i]
	
	return arr


arr = list(range(1,1000))

shuffle(arr)
print(arr)
