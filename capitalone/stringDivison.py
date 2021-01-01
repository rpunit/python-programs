
def findRepeatingSubString(s, t) :
	i = len(t)//2 
	while i > 0 :
		if len(s) % i == 0 and len(t) %i == 0 :
			factor1 = len(s) //i
			factor2 = len(t) //i
			if  t[:i] * factor1  ==  s and t[:i] * factor2 == t :
				print (t[:i])
				return i 
		i-=1
	return -1 

def findSmallestDivisor(s, t):
	# Write your code here
	#if (len(s) % len(t) != 0) :
		#return -1
	
	return findRepeatingSubString(s, t)




s = "abcdabcdabcdabcd"
t = "abcdabcd"

s = "abcabcabc"
t = "abcabc"

s = "abcabc"
t = "de"

s="abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
t="abcdabcdabcdabcd"
print (findSmallestDivisor(s,t))
