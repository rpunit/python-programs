

d = [
	["a", "b", 300],
	["b", "c", 200],
	["c", "a", 100],
]

def settle (items) :
	items = sorted (items, key = lambda x : x[1],  reverse=True )
	while (len(items) != 0 ) :	
		a1 = items[0][1] 
		a2 = items[-1][1] 

		if a1 > abs(a2) :
			print("person %s pays %d to person %s "% (items[0][0], abs(a2), items[-1][0] ))
			a1 = a1 + a2
			a2 = 0
			items[0][1] = a1
			items.pop(len(items) -1)
		elif a1 < abs(a2) :
			print("person %s pays %d to person %s "% (items[0][0], abs(a1), items[-1][0] ))
			a2 = a1 + a2 
			a1 = 0
			items[-1][1] = a2
			items.pop(0)
		else :
			print("person %s pays %d to person %s "% (items[0][0], abs(a2), items[-1][0] ))
			a2 = a1 + a2 
			items.pop(0)
			items.pop(len(items) -1)
		
		items = sorted (items, key = lambda x : x[1],reverse=True)
		
		
		

trans_map = {}
for trans in d :
	p1 = trans[0]
	p2 = trans[1]
	if p1 not in trans_map :
		trans_map[p1] = 0
	if p2 not in trans_map :
		trans_map[p2] = 0
	trans_map[p1] += trans[2]
	trans_map[p2] -= trans[2]


items = []
for t in trans_map.keys() :
	items.append([t, trans_map[t]])
		
settle(items)

