

arr = []

def substrCount( n, s) :
	tups = []
	prev = None 
		
	count = 1
	for i in range(len(s)) :
		cur = s[i]
		if prev != None :
			if cur != prev : 
				tups.append((prev, count))
				count = 1
			else :
				count += 1
		prev = cur
	tups.append((cur,count))
	print (tups)
	sscount = 0	
	# second pass
	for a,c in  tups :
		# for aaa the values are :   a a a   +  aa,aa + aaaa ( 3 + 2 + 1)
		sscount += c*(c+1)//2

	# third pass for special case
	for i in range (1, len(tups)-1) :
		if tups[i-1][0] == tups[i+1][0] and tups[i][1] == 1:
			sscount += min (	tups[i-1][1], tups[i+1][1] )

	return sscount


		
		
			

if __name__ == '__main__':

	n = int(input())

	s = input()

	result = substrCount(n, s)

	print(str(result) + '\n')

	
