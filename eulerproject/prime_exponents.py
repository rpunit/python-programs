

def prime_exp (n,p) :
	s = 0
	n = n//p
	while n > 0 :
		s += n
		n = n//p
	return s


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
exp = {} 
for p in primes :
	exp[p] = 0 

for i in range(2, 101) :
		j = 0 
		if i == 147 :
			continue
		while  j < len(primes) and primes[j] <= i :	
			p = primes[j]
			#print(i,p,prime_exp(i,p))
			exp[p] += prime_exp(i,p)
			j += 1

print(exp)
	
