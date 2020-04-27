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



def is_true () :
	j = 33
	while (j< 6000) :
		get_next_prime(j)
		# Must be composite
		if j in primes:
			j += 2
			continue	
		found = False
		for i in range (0, len(primes)) :
			if primes[i] >=j :
				break
			if (j - primes[i]) % 2 == 0 :
				v = math.sqrt((j - primes[i]) / 2 ) 
				if v - int(v) == 0 :
					#print("found", j)
					found = True
					break
		if not found :
			print ("not found", j)
			break
		
		j += 2

get_next_prime(10000)
print(primes)

is_true()
		
			
