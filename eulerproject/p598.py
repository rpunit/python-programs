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

n = 1000 
get_next_prime(n) 

			
def get_factors (n) : 
	mapp = {}
	i = 0
	if n in primes :
		mapp[n] = 1
		return mapp
	while i < math.sqrt(n) + 1  :
		p = primes[i] 
		if p not in mapp:
			mapp[p] = 0 
		while  n % p == 0 :
			mapp[p] += 1 
			n = n//p
		i += 1
	return mapp

#print(get_factors(13))
#print(get_factors(6))

#exit (1)


def get_factorial_factors(n) :
	mapp = {}
	for i in range (1,n + 1) :
		map1 = get_factors(i)
		#print("--", i, map1)
		for k in map1.keys() :
			if k not in mapp :
				mapp[k] = 0 
			mapp[k] += map1[k]

	return mapp



mapp = get_factorial_factors(10)

print (mapp)
items = list(mapp.items())


def get_num_div(factors, temp) :
	s1 = 1
	s2 = 1
	
	for i in range (len(temp)) :
		s1 = s1 * (temp[i][1] + 1) 
		s2 = s2 * (factors[i][1] - temp[i][1]  + 1) 

	return (s1,s2)

def calc_div (arr) :
	s = 1
	for item  in arr: 
		s = s* (item[0] ** item[1])
	return s

count=0
rec_count=0
def count_divisors (items, index, out ) :
	global count
	global rec_count
	rec_count += 1
	if rec_count % 1000000 == 0:
		print("Processing index,rec_count " ,index, rec_count, out)
	if index == len(items) :
		div1,div2 = get_num_div(items, out)
		#print("---", div1, div2, out)
		if div1 == div2 :
			print(div1, div2, out)
			print(calc_div(out))
			count += 1
		return
	for i in range (items[index][1] + 1) :	
		out[index] = [items[index][0], i] 
		count_divisors(items, index + 1, out)


temp = [[0,0]]*len(items)
total = sum(map(lambda x : x[1] + 1, items))
count_divisors(items, 0, temp )
print(count)


