


def delExtraSpace (s) :
	lstr = list(s) 
	index = 0
	count = 0
	for i in range(len(lstr)) :
		if lstr[i].isspace() :
			count +=1 
			if count == 1:
				lstr[index] = lstr[i] 
				index += 1
				
		else :
			count = 0
			lstr[index] = lstr[i] 
			index += 1

	print ("".join(lstr[:i+1]))


delExtraSpace("this    is a  random     string")
			
