


def remove_duplicates (arr) :
	
	out = []
	index = 0
	for i in range(len(arr)): 
		if arr[i] not in out  :
			out.append(arr[i])
			index += 1


	print (out)


a = list("abcaaaadefbk") 
remove_duplicates( a)
