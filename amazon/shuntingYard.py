# https://brilliant.org/wiki/shunting-yard-algorithm/

def operatorPrec(op1, op2) :
	if op1 == op2 :
		return 0 
	if op1 in ("*", "/") :
		if op2 in ( "+", "-") :
			return 1
		else :
			return 0
	elif op1 in ( "+", "-") :
		if op2 in ( "*", "/") :
			return -1
		else :
			return 0
	
	return 0


def getReversePolish (expr) :
	stack = []
	queue = []
	i = 0
	while i < len(expr) :
		dig = ""
		while expr[i].isdigit () :
			dig += expr[i]
			i += 1
		if dig != "" :
			queue.append(dig)
			
		s = expr[i]
		if s in ( "+", "-", "/", "*", "(") :
			if len(stack) > 0 and operatorPrec(stack[-1], s) > 0 :
				temp = stack.pop(-1) 
				queue.append(temp)
			stack.append(s)
		elif s in ( ")") :
			e = stack.pop(-1) 
			while e != "(" :
				queue.append(e)
				e = stack.pop(-1) 
		i+=1

			

	while (len(stack)) :
		s = stack.pop(-1)
		queue.append(s)

	return queue




def doMath(v1,v2,v) :
	if v == "+" :
		return v1 + v2
	elif v == "*" :
		return v1 * v2
	elif v == "/" :
		return v1 / v2
	elif v == "-" :
		return  v1 - v2

def solve (expr) :
		
	polish = getReversePolish(expr)
	print("polish " , polish)

	stack = []
	for v in polish :
		if v.isdigit() :
			stack.append(int(v))

		if v in ( "+", "-", "/", "*" ) :
			v2 = stack.pop(-1) 	
			v1 = stack.pop(-1) 	
			stack.append(doMath(v1, v2, v) )
		print (v, stack)

	print(stack.pop(0))
			
expr = "4 + 18/(9-3)"
expr = "(4 +3)*4 + 18/(9-3)"

polish = getReversePolish(expr)


print (expr)
solve(expr)
