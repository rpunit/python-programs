
"""
  TF: (T op Y)  - > 3

  TTF :		T op (T op Y) - 9
			(T op T) op Y - 9
			: 18

  FTTY : 


"""
def getBooleanVal (b) :
	if b == "T":
		return True
	return False

def isTrue( b1, b2, ops) :
	b1 = getBooleanVal(b1)
	b2 = getBooleanVal(b1)
	if ops == "|" :
		return b1 | b2
	elif ops == "&" :
		return b1 & b2
	elif  ops == "^" :
		return b1 ^ b2
	else :
		raise Exception("ERROR. Unknown op " + ops)
		
def countParen ( symbols, operators, index) :

	if index == len(symbols) - 1 :
		s1 = symbols[0]
		if getBooleanVal(s1) :
			return 1
		return 0

	count = 0 
	# Use just the first symbol as standalone 
	if index <= len(symbols) - 1 :
		for op in operators :
			s1 = symbols[index]
			cnt = countParen(symbols, operators, index + 1) 
			if isTrue(s1, "T",  op) :
				count += cnt

	if index <= len(symbols) - 2 :
		# Use  the first two symbol as standalone 
		for op in operators :
			s1 =symbols[index]
			cnt = countParen(symbols, operators, index + 2) 
			if isTrue(s1,"T", op) :
				count += cnt
	
	return count	


# Driver Code 
#symbols = "TTFT"
symbols = "TTFT"
operators = "|&^"
n = len(symbols) 
  
# There are 4 ways  
# ((T|T)&(F^T)), (T|(T&(F^T))),  
# (((T|T)&F)^T) and (T|((T&F)^T))  
print(countParen(symbols, operators, 0)) 
  
# This code is contributed by  
# sahil shelangia 
