pd_map = {}
def is_pandigital (peri) : 

	memo = {}
	for p in range (3, peri) :
			print("Processing ", p)
			for i in range (1,p) :
				for j in range (1,p) :
					if i + j < p :
							k = p - (i + j) 
							arr = [i,j,k]	
							arr = sorted(arr)
							#print(arr)
							val = str(arr) 
							if arr[2]**2 == (arr[1]**2 + arr[0]**2) :
								if val in memo : 
									if p not in pd_map :
										pd_map[p] = []
									if val not in pd_map[p] :
										#print(p, " adding val", val)
										pd_map[p].append(val)
										memo[val] = 1
								else :
									print("found in memo", val)
									if p not in pd_map :
										pd_map[p] = []
									if val not in pd_map[p] :
										#print("--adding val", val)
										pd_map[p].append(val)

	items = sorted(pd_map.items(), key = lambda x: len(x[1]), reverse=True)
	return items
		


print (is_pandigital(1000)[:3])
