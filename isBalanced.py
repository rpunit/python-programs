def getMatching (s) :
	if s == ")" :
		return "(" 
	if s == "}" :
		return "{" 
	if s == "]" :
		return "[" 

def isBalanced(s):
	stack = []
	for i in range(len(s)) :
		if s[i] in ("(","{","["):
			stack.append(s[i])
		if s[i] in (")","}", "]"):
			if len(stack) > 0 :
				if stack[-1] != getMatching(s[i] ) 	:
					print(s[i], stack[-1], getMatching(s[i]))
					return "NO"
				else :
					stack.pop(-1)
	print(stack)
	if len(stack) == 0 :
		return "YES"
	return "NO"


print( isBalanced("{{([)}"))
print( isBalanced("{{(]}"))

