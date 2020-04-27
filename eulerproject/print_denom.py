


def print_all (index, denoms, total, vals ) :

	if total == 0 :
		print (vals)
		return

	if index == len(denoms) :
		return

	coin = denoms[index]
	for i in range (total//coin) :
		vals[index] = i
		print_all(index + 1, denoms, total - i*coin, vals)


total = 5
print_all (0, [5,2,1], total, [0]*total )
