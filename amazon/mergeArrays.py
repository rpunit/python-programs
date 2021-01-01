def merge(a1, a2 ) :
	l1 = len(a1)
	l2 = len(a2)
	i = 0
	j = 0


	out = []
	while (i< l1 and j < l2 ) :
		if a1[i] < a2[j] : 
			out.append(a1[i]) 
			i += 1
		else :
			out.append(a2[j]) 
			j += 1
	if i != l1 :
		out.extend(a1[i:])
	
	if j != l2 :
		out.extend(a2[j:])

	print(out) 


a = [11,42,6,3,2,17]
b = [3,5]


merge(sorted(a), sorted(b) ) 
		
