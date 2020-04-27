from datetime import datetime
fibs = [0]

def gen_fib(n) :
	i1 = 0
	i2 = 1
	for i in range (n  ) :
		s = i1 + i2
		fibs.append (s)
		i2 = i1
		i1 = s


gen_fib(90)
print(fibs)

def dig_sum (n) :
	s = 0
	while n != 0 :	
		s += n % 10
		n = n//10
	return s

print(dig_sum (123) )

def s1 (n, m) :
	nines = n // 9		
	print(nines)
	ns = "9"*nines
	rem = n % 9 
	if rem > 0 :
		ns =  ( str(rem)  + ns)
	sum = 0
	for i in range(len(ns)) :
		sum = (sum*10 + int(ns[i])) % m
	return sum

def s (n, mod) :
	nines = n//9
	r = n % 9
	return  r*pow(10,nines, mod) + pow(10,nines,mod) -1 % mod

		
print (s(89,10000000000000000000000000 ))
#exit(1)

def S (n, mod) :
	sum = 0
	for i in range (1,n+1) :
		sum += s(i,mod)
	return sum

print (S(49, 1000000007))

def Sf () :
	sum = 0
	mod = 1000000007 
	for i in range (2,len(fibs)) :
		si = s(fibs[i], mod)
		sum += si 
		print("testing ", i, fibs[i], sum)
	return sum  % mod

print(Sf())
	
