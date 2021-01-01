#https://www.hackerrank.com/challenges/challenging-palindromes/problem


def isPalin (s) :
	mid = len(s)//2
	for i in range(mid) :
		if s[i] !=  s[len(s) -i-1] :
			return False
	return True

def buildPalindrome(a, b) :
	la = len(a) 
	lb = len(b)
	for i in range(len(a)) :
		for j in range(len(b)) :
			sub1 = a[:la -i]
			sub2 = b[:lb -j]
			temp = []
			temp.append(sub1 + sub2)
			temp.append(sub2 + sub1)
			print(a,b, temp)
	
			temp = list(filter(lambda x : isPalin(x), temp))
			if len(temp) != 0 :
				maxp = sorted(temp, key=lambda x : len(x), reverse=True)[0]
				print("---", maxp)
				return maxp
	return "-1"


def buildPalindrome2(a, b) :
	while  len(a) > 0 and len(b) > 0 :
		print(a,b)
		temp = []
		temp.append(b+a) 
		temp.append(a+b) 

		temp.append(a[1:]+ b)
		temp.append(b + a[1:])

		temp.append(a+ b[1:])
		temp.append(b[1:] + a)

		temp.append(a+ b[:-1])
		temp.append(b[:-1] + a)

		temp.append(a[:-1]+ b)
		temp.append(b + a[:-1])

		temp.append(a[1:]+ b[:-1])
		temp.append(b[:-1] + a[1:])

		temp.append(a[:-1]+ b[1:])
		temp.append(b[1:] + a[:-1])
		print(temp)
		temp = list(filter(lambda x : isPalin(x), temp))
		if len(temp) != 0 :
			maxp = sorted(temp, key=lambda x : len(x), reverse=True)[0]
			print("---", maxp)
			return maxp
		a = a[1:-1]
		b = b[1:-1]
	return "-1"


		
"""
a = abc      abcde
"""
def buildPalindrome1(a, b) :
	if len(a) == 0 or len(b) == 0 :
		return "-1" 
	# try different perms
	maxp = 0
	temp = []
	temp.append(a + b)
	temp.append(b + a)
	print(a,b, temp)
	
	temp = list(filter(lambda x : isPalin(x), temp))
	if len(temp) != 0 :
		maxp = sorted(temp, key=lambda x : len(x), reverse=True)[0]
		print("---", maxp)
		return maxp

	temp1 = []
	temp1.append(buildPalindrome(a[1:], b))
	temp1.append(buildPalindrome(a, b[1:]))
	temp1.append(buildPalindrome(a, b[:-1]))
	temp1.append(buildPalindrome(a[:-1], b))
	temp1 = list(filter(lambda x : len(x) > 0 , temp1))
	if len(temp1) != 0 :
		maxp = sorted(temp1, key=lambda x : len(x), reverse=True)[0]
		return maxp

	return "-1" 
	 
	
a = "bac"
b = "bac"
#a = "jdfh"
#b = "fds"
print (buildPalindrome(a,b) )
