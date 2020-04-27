def search(s, sub ) :
	i = 0
	while i < len(s) - len(sub) + 1 :
		j = 0
		while (j < len(sub) ) :
			if sub[j] != s[i + j] :
				break
			j += 1
		if j == len(sub)  :
			return i
		i += 1
	
	return -1

print(search("this is some thing", "ing"))	
	
