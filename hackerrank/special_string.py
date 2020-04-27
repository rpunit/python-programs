


arr  = []
def is_palin (s) :
	n = len(s) //2
	for i in range(n) :
		if s[i] != s[len(s) - i -1] or s[i] != s[0]:
			return False
	return True

def ss( s, n) :
	for i in range (0, n ) :
		for j in range (i, n) :
			if is_palin(s[i : j + 1] ):
				arr.append(s[i : j + 1])
					
s = "abcdddeffaffg"
s = "abcbaba"
ss(s, len(s))
print(s)
print(arr)
print(len(arr))
