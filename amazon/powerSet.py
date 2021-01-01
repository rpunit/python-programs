


def powerSet(arr) :
	out = []
	for i in range(1,2**len(arr)) :
		
		s = bin(i)[2:]
		print (s)
		subarr = []
		for i in range(len(s)) :
			if s[len(s) - i - 1] == "1" :
				subarr.append(arr[i])
		out.append(subarr)
	return out


arr = [1,2,3,4,5,6,7,8]
arr = [1,2,3]


print(powerSet(arr))
