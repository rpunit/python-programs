import math
primes = [2,3,5,7,11] 
def get_next_prime (n) :
	j = primes[-1]  + 1
	while (j < n) :
		prime  = True
		for i in range(len(primes)):
			if j % primes[i] == 0 :
				prime = False
			if math.sqrt(j) <  primes[i] :
				break
		if prime == True :
			primes.append(j)
		j += 1
	return primes[-1]


def get_factors(n) :
	get_next_prime(n + 1)
	factors = {} 
	if n in primes :
		return [n]
	np = n
	for i in range(len(primes)) :
		while  np % primes[i] == 0:
			#print("Adding", np, primes[i])
			factors[primes[i]] = 1
			np = np//primes[i]

	return list(factors.keys())



#get_next_prime(100000)
n = 2*3*5*7


while (n < 1000000) :
	if (len(get_factors(n)) == 4 and
		len(get_factors(n+1)) == 4 and
		len(get_factors(n+2))== 4 and
		len(get_factors(n+3)) == 4 ) :
			print(n, n+1, n+2)
			break
	n += 1 

		
			
