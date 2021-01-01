def nearestK(arr, k) :

	x,y = (0,0)
	xm = max(map(lambda x: x[0], arr))
	ym = max(map(lambda x: x[1], arr))
	out = []
	while x< xm and  y <  ym :
		for i in range (x) :
			if (i,y) in arr and len(out) <=k:
				out.append((i,y))	

		for i in range (x) :
			if (x,i) in arr and len(out) <=k:
				out.append((x,i))	
		x += 1
		y += 1
		
		if len(out) == k :
			break

	return out

		
arr = [(19,1), (2,24),  (1,2), (3,2), (2,3), (8,8), (7,6), (3,10) ]

print(nearestK(arr,5))
