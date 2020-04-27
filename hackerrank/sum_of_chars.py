def recurse (s, index, r,  tmp, out ):
	if r == 0 :
		out.append("".join(tmp.copy()))
		return
	if index == len(s) :
		return 

	i = index 	
	while i < len(s) - r + 1: 
		tmp[len(tmp) -r] = s[i]	
		recurse(s, index + 1, r -1, tmp, out)
		i += 1


			
def genSubStrings (s) :
	substrs = set()
	for sublen in range(1, len(s)) :
		for	i in range(0, len(s) -sublen + 1) :
			substrs.add(s[i: i + sublen])
	return substrs
		
def getIntForStr(p, q) :
	# Add all the characters
	orda = ord("a")
	total = 0
	for i in range(len(p)) :
		index = ord(p[i]) - orda
		total += int(q[index])

	return total

def removeDuplicates (s) :
	s = "".join(set(list(s)))
	return s

def distinctSubstring(p, q, k, n) :

	total = 0 
	orda = ord("a")

	
	subs = genSubStrings(p) 	
	print( subs)
	for s in subs :
		v = getIntForStr(s, q)
		if v <= k :
			total += 1

	return total
			


# Driver code  
P = "abcde"
Q = "12345678912345678912345678"
K = 5
N = len(P) 
  
print(distinctSubstring(P, Q, K, N)) 
