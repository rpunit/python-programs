

def recurse ( s ,index ) :

	if index == len(s) -1 :
		return [s[index]]

	
	prev = recurse(s, index+1) 
	temp = []
	temp.append(s[index])
	for p in prev :
		temp.append(s[index] + p ) 

	temp.extend(prev)
	return temp


def powerset(a) :
	return recurse(str(a), 0)

def getDigMul(d) :
	out = 1
	for s in d:
		out = out* int(s)
	return out
		

def colorfulNos (d) :
	mapi = {}
	ps = powerset(d)
	for p in ps :
		mul=getDigMul(p)			
		if mul in mapi :
			return False
		else :
			mapi[mul] = 1

	return True

print(colorfulNos(3245))
print(colorfulNos(3246))
