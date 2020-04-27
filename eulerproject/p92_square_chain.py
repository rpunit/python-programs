



def get_square_sum(n) :
	s = 0
	while (n  != 0  ) :
		s += (n%10) ** 2
		n = n//10
	return s

#print(get_square_sum (12))
#exit(1)

n = 10000000

mapp =  [ (0,0)  for i in range(n*2+1) ]

count = 0
for i in range(1,n) :
	x = get_square_sum (i)
	tcount = 0
	while x != 89  and  x != 1:
		if mapp[x][1] != 0 :
			if mapp[x][0] == 89 :
				tcount += mapp[x][1]
				break
		x = get_square_sum (x)
		tcount += 1
	

	if x == 89 or x==1 :
		#print(i, x)
		mapp[n] = (x,tcount)

	if x == 89 : 
		count += 1 


print (count)
		
	
