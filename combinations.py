


def combo  (arr, n, start, res) :
	if n == 0 : 
		print(res)
		return
	i = start	
	while  i < len(arr) - n + 1 : 
		i_res = len(res) - n
		res[i_res] = arr[i]
		combo(arr, n - 1, i + 1, res)
		i = i + 1 


arr = [1,2,3,4,5,6,7,8,9]
n = 3
res = [0]* n
combo (arr, n, 0 , res )
