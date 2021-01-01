


def selectionSort(arr) :

	for i in range(1,len(arr)) :
		for j in range(0,i) :
			if arr[i] < arr[j] : 
				arr[i], arr[j] = arr[j],arr[i]


	return arr



arr = list(range(1,1000000)) 
selectionSort(arr)

print (arr)
