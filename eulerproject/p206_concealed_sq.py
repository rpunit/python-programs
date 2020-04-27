import math


sq = "1020304050607080900"
min = int(math.sqrt(1020304050607080900))
max = int(math.sqrt(1929394959697989990))

def matches (n) :
	ns = str(n)
	i = 0
	while i < len(ns) :
		if sq[i] != ns[i]:
			return False
		i += 2
	return True 

print(min, max)
i = min 
while i < max :
	v =  i*i 
	if matches(v) : 
		print (i)
		break
	i += 10
