

def calc_count(index, total, denoms, out) :
	#
	if total == 0 :
		combos.append(out.copy())
		return 1

	if index == len(denoms) :
		return 0

	coin = denoms[index]
	mul  = 0
	count = 0 
	while (mul * coin <= total) :
		#print("index=%d, total=%d, coin=%d, mul=%d " % (index, total, coin, mul) )
		out[index] = mul
		count += calc_count(index + 1,  total - mul*coin, denoms, out) 
		out[index] = 0
		mul += 1
	return count


denoms = [1,2,5,10,20,50,100,200]
denoms.reverse()
combos = []
total = 200
vals = [0]*len(denoms)
print(calc_count(0, total, denoms, vals) )

#print(denoms, combos)


