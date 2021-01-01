

# 1  11   21  1211
def lookAndSay (n) :
	cur = [1] 
	for i in range(0,n) :
		j = 0
		temp = []
		while j < len(cur) :
			#print(i,j,cur)
			v = cur[j] 
			count = 0
			while j  < len(cur) and cur[j] == v  :
				count +=1 
				j+=1
			temp.append(count)
			temp.append(v)
			#print("--", i,j,temp, cur)
		cur = temp

	print (temp) 
	print (len(temp) )

lookAndSay(5)
		
