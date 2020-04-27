
def longest_palindrome (str ) :
	# build a truth table 
	n = len(str)
	tt = [[ 0  for x in range(n)] for y in range(n)]

	l = list(str)

	# x is srart index, y in end index

	# initilize all with lenth 1
	for x in range(n):
		tt[x][x] = 1

	max_len = 1
	start = 0
	# initilize all with lenth 2
	for x in range(n - 1):
		if l[x] == l[x+1] :
			tt[x][x+1] = 1 
			start = x
			max_len = 2


	# start with palindrom of length 3
	plen = 3	
	while plen <= n :
		index = 0
		while index < n -  plen + 1 :
			end = index + plen  - 1
			if tt[index + 1][ end - 1] and l[index] == l[end] :
				tt[index][end] = 1 
				if plen > max_len:
					start = index
					max_len = plen
			index += 1	
		plen += 1
	
	print(start, max_len)	
	return "".join(l[start:start + max_len])



print(longest_palindrome("abcdedcbklaba"))
	

