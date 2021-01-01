def getDict1() :
	with open("/usr/share/dict/words", "r") as f :
		arr = f.readlines()
		return  set( filter ( lambda x : (len(x) ==1 and x in ("i", "a" )) or len(x) > 1, map(lambda x : x.strip(), arr)))

def getDict () :
	with open("./10kwords.txt", "r") as f :
		arr = f.readlines()
		return  set(  map(lambda x : x.strip(), arr))



memo = {}

def parseString (strn,dictionary) :

	if len(strn) == 0 :
		return  [""]

	res = []
	for j in range(1, len(strn)+1) :
		sub = strn [:j]
		#print (j, strn, sub)
		out = []
		if sub in dictionary :
			#print ("---", strn, sub)
			rest = strn[j:]
			if rest in memo :
				out = memo[rest]
			else :
				out = parseString(rest, dictionary )
				memo[rest] = out
			for i,o in enumerate(out) :
				res.append( sub + " " + o)
	return  res
				

dictionary = getDict() 
#print(dictionary)
#res = parseString("searchinputfilesforlinesthatmatchagivenpattern", dictionary)
res = parseString("daddycarnuttruckguy", dictionary)
#res = parseString("thisiscrazystupid", dictionary)
#print(memo)
print(res)
