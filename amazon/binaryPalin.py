


def isPalin (n) :
	s = bin(n)[2:]

	l = len(s)
	mid = len(s)//2

	for i in range(mid) :
		if s[i] != s [l -1 -i]  :
			return False
	return True


for i in range(1,100) :
		if isPalin(i) :
			print ("%d is palin %s" % (i, bin(i)))
