

def merge_val(v, out ) :
	outarr = []
	for arr in out : 
		for i in range (len(arr) + 1) :
			temp=arr.copy()
			temp.insert(i, v) 
			outarr.append(temp)
	return outarr

def permutate (arr, index) :
	if index == len(arr) - 1:
		return [[arr[index]]]

	temp = permutate (arr, index + 1 ) 
	out = merge_val(arr[index], temp)
	if index == 0 : 
		for i in range(len(out)) :
			print ("".join(out[i]))
		print(len(out))
	return out


arr = list("abcdef")
permutate ( arr, 0) 
