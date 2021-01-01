def rw(s, i, j) :
	while i < j :
		s[i],s[j] = s[j], s[i]
		i += 1
		j -= 1
	
def reverseWords(inp ) :

	i=0
	j = 0
	s = list(inp)
	l = len(s)

	while i< l and j < l :
		while i < l and s[i] == " "  :
			i+=1	
		j = i	
		while j < l and s[j] != " "  :
			j+=1	

		# word is between i and j
		rw (s, i, j-1)
		i = j
	

	return  "".join(s)	

print (reverseWords("this is reversed"))



