
# abcd
# a
def get_permute (n, index ) :
	if index == len(n) - 1  :
		return [[n[index]]]
	
	partial = get_permute(n, index + 1)

	out = []
	for i in range (len(partial)) :
		temp = partial[i]
		for j in range(len(temp) + 1) :
			tcp = temp.copy()
			tcp.insert(j, n[index])
			out.append(tcp)

	#if index == 0 :
		#all.append(out)
	return out

def get_pair (l) :
	out = []
	for i in range(len(l) - 1) :
		for j in range (i + 1, len(l)) :
			out.append ((l[i], l [j]))
	return out

def is_pair_lycheral (p1, p2) :
	j = 0
	while j < 50 :
		p1 = p1 + p2	

	


print(get_pair([2, 4,5,6, 7]))


for i in range(12, 14) :
	all = get_permute(list(str(i)), 0 ) 
	list_int = list(map(lambda x : int("".join(x)), all))
	for j in list_int :
		print(j)
		j = 0
		#while j < 50 :
			
	
		
