def whatFlavors(cost, money):
	scost = sorted(cost)
	prev=0
	i = 0
	j = len(cost) - 1
	while i < j  :
		total = scost[j] + scost[i]
		if total == money :
			break
		elif total > money :
			j -= 1
		elif total <  money :
			i += 1

	i1 = scost[i]
	i2 = scost[j]	
	items = sorted([i1,i2])
	print("i1,i2,money,i,j,total",i1, i2, money,i,j, total)

	k1=-1
	k2=-1
	for k in range(len(cost) ) :
		if cost[k] == items[0] :
			if k1 == -1:
				k1 = k
		if cost[k] == items[1] :
			if k1 != -1 : 
				if  k != k1:
					k2 = k
			else :
				k2 = k

		if k1 != -1 and k2 != -1 :
			break

	print(cost,money)
	print("%d %d" % (k1+1, k2+1))



whatFlavors([1,4,5,3,2], 5)
whatFlavors([7,2,5,4,11], 12)
whatFlavors([2,2,4,3 ], 4)

