from collections import defaultdict

def isValid(src, target) :
	for x in target :
		if x not in src or  src[x] !=  target[x] :
			return False	
	return True

"""
abbc 

abbd cabb efgh

"""
def find_perms (s, b ) :
	target = defaultdict(int) 
	for x in s :	
		target[x] += 1

	src = defaultdict(int) 
	out = []
	start = 0
	while start < len(b) - len(s) + 1 :

		
		cur = start 
		count = 0
		while count < len(s) and not isValid(src, target)  :
			c = b[cur]
			#print (b, cur, b[cur] )
			src[c] += 1
			cur += 1
			count += 1

		#print (start, cur, src, target, isValid(src, target))

		if isValid(src, target) and count == len(s):
			out.append(b[start : cur])
			src[b[start]] -= 1
		else :
			src = defaultdict(int)
		start += 1

		#print ("---", start, len(b), len(s))

		
	return out


s = "abbc"
b = "abbdcabbdefgabbc"

print (find_perms(s,b))
			
