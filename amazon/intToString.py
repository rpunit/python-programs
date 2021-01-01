
def thToStr(n) :
	teensarr = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	onesarr = ["one", "two", "three", "fourt", "five", "six", "seven", "eigh", "nine"]
	tensarr = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	s = ""
	hun = n//100
	if hun != 0 :
		s += onesarr[hun-1] +  " hundered " 
	tens = n % 100
	if tens > 10 and tens < 20 :
		s += teensarr[tens - 11]  
	elif n < 11 :
		s += onesarr[tens-1] + " " 
	else :
		ten,uni = tens//10, n%10
		if ten > 0 :
			s += tensarr[ten-2] + " " 
		if uni :
			s += onesarr[uni-1] 
	return s
	

def intToString(n) :
	numTh = 0	
	arr = []
	while (n ) : 
		s = thToStr(n%1000)  
		arr.append(s)
		n = n//1000

	out = ""
	for i in range(len(arr)) :
		j = len(arr) - i -1  
		if j == 2 :
			out += arr[j] + " million " 
		elif j == 1 :
			out += arr[j] + " thousand " 
		else :
			out += arr[j] 
	
	return out	
		

print (intToString (2050098))
	
