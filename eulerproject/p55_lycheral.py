
N = 500	


def reverse (n ) :
	k = 0 
	while n > 0  :
		k = k*10 + n % 10
		n = n//10
	return k

		

count = 0
for i in range (1, 10000) :
	j = 0
	s = i
	while j < 50 :
		s =  s + reverse(s) 
		if  s == reverse(s) :  
			#print("not lychera", i, s) 
			break
		j += 1
	if j == 50 : 
		print(" lychera", i) 
		count += 1

print (count)
			
			
			
			
