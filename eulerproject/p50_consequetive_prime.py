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

# get all primes up to 1m
n = 1000001
get_next_prime(n) 
print (primes[-1])

max_sum = 0
max_count = 0
prime_i = 2 
for i in range (len(primes)) :
	sum = primes[i] 
	count = 1
	arr = [sum]
	for  j in range (i+1, len(primes))  :
		#print("--", sum, primes[j])
		if sum > n :
			#print ("breaking", sum, n)
			break
		sum += primes[j] 
		arr.append(primes[j])
		count += 1
		if sum  in primes :
			#print(i,j,primes[i],primes[j],sum)
			if count > max_count :
				print("found prime, count", primes[i], primes[j], count, sum)
				print(arr)
				max_sum = sum
				prime_i = i
				max_count = count


print (primes[prime_i], max_count, max_sum)
		

	
			
