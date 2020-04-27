import math, bisect 

def search_list(l, n) :
	'Locate the leftmost value exactly equal to x'
	i = bisect.bisect_left(l, n)
	if i != len(l) and l[i] == n:
		return True
	False


primes = [2,3,5,7,11] 
def get_next_prime (n) :
	if primes[-1] > n  :
		return 
	j = primes[-1]  + 1
	while (j < n + 1) :
		prime  = True
		for i in range(len(primes)):
			if j % primes[i] == 0 :
				prime = False
			if math.sqrt(j) <  primes[i] :
				break
		if prime == True :
			primes.append(j)
		j += 1
	return 

	
N = 1000000
get_next_prime(N)

def are_prime_pairs(p1, p2) :
	p12 = int(str(p1) + str(p2))
	#if  not is_prime(p12) :
		#return False
	
	if not search_list(primes,p12) :
		return False
	p21 = int(str(p2) + str(p1))
	#if  not is_prime(p21) :
		#return False
	if not search_list(primes,p21) :
		return False
	is_prime(p12)
	return True


def is_prime (p ) :
	i = 0
	if math.sqrt(p) > primes[-1] :
		print("resizing for " + str(p))
		get_next_prime( int(math.sqrt(p))  )

	while ( primes[i] < math.sqrt(p) ) :
		if p % primes[i] == 0:
			return False
		i += 1
	return True
	
mapp = {}

limit = 30000
for i in range(limit) :
	mapp[primes[i]] = set() 
	for j in range(limit) :
		if i == j :
			continue
		if are_prime_pairs(primes[i], primes[j]) :
			#print("paris", primes[i], primes[j])
			mapp[primes[i]].add(primes[j])

candidates = list(filter(lambda x : len(x[1]) >= 4, mapp.items()))

for i in range(len(candidates)) :
		p1 = candidates[i][0]
		set1 = set(candidates[i][1])
		count  = 0
		for p2 in set1 : 
			iset = mapp[p2].intersection(set1)
			if len(iset) >= 4 :
				print(p1,p2,set1)
				set1 = iset 
				count += 1

			if count >= 4 :
				print (p1, set1) 
				break
				



