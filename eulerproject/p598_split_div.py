import math
from functools import reduce

def combo(index, l, r , out, all_c) :
	if r == 0 :
		all_c.append(out.copy())	
		return
	i = index 
	while ( i < len(l) - r + 1) :		
		out[len(out) - r] = l[i]	
		combo(i + 1, l , r - 1, out, all_c)
		i += 1

def factors (n) :
	f = []
	i = 2
	n1 = n
	while i < math.sqrt(n)+1 :
		while n1 % i == 0 :
			f.append(i)	
			n1 = n1//i
		i += 1
	if n1 > 2 :
		return [n]
	return f


def factors_to_prime_factors(n) :
	f = [1]
	for i in range (1, n+1) :
		print(i,factors(i))
		f += factors(i)
	return f

#print( factors_to_prime_factors (8))
#exit(1)
		

def num_divisors_fact(n) :
	
	num = math.factorial(n)
	p_factors = factors_to_prime_factors (n)
	factors = list(range(1, n+1)) 
	factors.append(num)
	print(factors)
	r = 2
	while r < n :
		all_c = []
		print (r)
		combo(0, p_factors, r, [0]* r, all_c)
		#print(all_c)
		for facts in all_c :
			x =  reduce ( lambda a,b : a*b, facts, 1) 
			if x  not in factors :
					factors.append(x) 
			if num//x not in factors :
					factors.append(num//x) 
			
		r += 1
	return factors
		
n = 100
f = num_divisors_fact(n)
print(len(f))
print(f)


