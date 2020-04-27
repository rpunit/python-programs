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

get_next_prime(200000) 

i = 0 
while primes[i] <  1000 :
	i += 1 

print(i, primes[i])
while primes[i]  < 10000:
	for j in range (i+1,10000) :
			if sorted(str(primes[i])) == sorted(str(primes[j])) :
				#print("i,j,pi,pj",i,j, primes[i], primes[j])
				delta = primes[j] - primes[i]
				p_1 = primes[i] + 2*delta
				if p_1 in primes and sorted(str(primes[i])) == sorted(str(p_1)) :
					# found 
					print (str(primes[i] ) + str(primes[j]) + str(p_1))
					break
	i +=  1
		
			
