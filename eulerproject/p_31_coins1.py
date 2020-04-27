


def coin_combinations (money, index , out) : 
	count = 0
	print("money,index",money, index)
	if index <= 0 :
		out.append(coin_list[0])
		combos.append(out)
		return 1

	m = money 
	if memoiz_list[m][index] > 0 :
		return memoiz_list[m][index]
	while ( m >= 0 ) :
		coin = coin_list[index]
		count += coin_combinations (m, index - 1, out.copy() ) 
		out.append(coin)
		print("m,coin",m, coin)
		m -= coin_list[index] 

	memoiz_list[money][index]  = count
	return count


coin_list = [1,2,5,10,20,50,100,200]
memoiz_list = [[0,0,0,0,0,0,0,0] for i in range(201)]
combos = []

print (coin_combinations (5, len(coin_list) - 1, []))
print(combos)
