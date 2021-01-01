import sys
import random


def selectionSort(arr) :

	for i in range(0,len(arr)) :
		minv = sys.maxsize	
		minj = 0
		for j in range(i,len(arr)) :
			if arr[j] < minv :
				minj = j
				minv = arr[j] 	
			arr[i], arr[minj] = arr[minj],arr[i]


	return arr



arr = random.sample((range(0,100000)), 100000)
selectionSort(arr)

print (arr)
