


count_map = {}
def collatz (n) :
	count = 1
	while (n > 1) :
		if n % 2 == 0:
			n = n/2
		else :
			n = 3*n + 1
		if n in count_map : 
			return count + count_map[n]
		count += 1
		
	count_map[n] = count
	return count


max_n = 0
max_count = 0
for i in range(1000000) :
	c = collatz(i)
	print(i,c)
	if c > max_count :
		max_count = c
		max_n = i

print (max_count, max_n)
	

		
