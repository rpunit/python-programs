import math

def divisors(n) :
	pairs = []
	i = 1
	sqrtn = math.sqrt(n)
	#print(sqrtn)
	while i < sqrtn : 
		if n% i == 0 :
			pairs.append((i,n//i))
		i += 1
	return pairs

#print(len(divisors(math.factorial(6))))
#exit(1)

def num_div(a, ndmap) :
	if a in ndmap :
		n1 = ndmap[a]
		print("cache_hit", a)
	else :
		ndmap[a] = []
		n1 = len(divisors(a))
		ndmap[a].append(n1)
	return n1


def num_div_with_same_div (l) :
	div_map = {} 
	count = 0
	for (a,b) in l :
		n1 = num_div(a, div_map) 
		n2 = num_div(b, div_map) 
		if n1 == n2 :
			print(n1,a,n2, b)
			count += 1
	return count

N = math.factorial(10)
list_div = divisors(N)
#print(list_div)

print(num_div_with_same_div(list_div))
	
	
