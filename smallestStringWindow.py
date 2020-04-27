from collections import defaultdict 

def smallestWindow (inp, sub ) :

	def isValid ( src, dest ) :
		for item in dest :
			if item not in src or src[item] < dest[item] :
				return False
		return True 

	source = defaultdict(int) 
	target =  defaultdict(int)
	minlen = 10**10
	mins = ""
	# initialize the soruce 
	for s in sub :
		target[s] += 1 


	index = 0
	for start in range (len(inp)) :
		#print(start, source)
		while index < len(inp)  and  isValid(source,target) == False:
			source[inp[index]] += 1
			index += 1

		if isValid(source, target ) :
			substr = inp[start:index + 1]
			if len(substr) < minlen :
				minlen = len(substr) 
				#print(start, index, substr)
				mins = substr
		source[inp[start]] -= 1		

	return mins


a = "timetopractice"
b = "toc"
print(smallestWindow(a, b))
print(smallestWindow("zoomlazapzo", "oza"))
