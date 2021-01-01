

arr = []

def substrCount( n, s) :
	memo = [ [0 for i in range(n) ] for j in range(n)]
	for i in range (n) :
		memo[i][i] = 1
		arr.append(s[i])
		if i < n-1 and s[i] == s[i+1] : 
			memo[i][i+1] = 1
			arr.append(s[i:i+2])
	
	plen = 3
	while ( plen <= n) :
		start = 0
		while ( start < n-plen + 1 ) :
			end = start + plen - 1
			if memo[start+1][end-1] ==  1 and  s[start] == s[end] :
				if plen > 3   :
					if s[start] == s[start+1]: 
						memo[start][end] = 1	
						arr.append(s[start:end+1])
				else : 
					memo[start][end] = 1	
					arr.append(s[start:end+1])
			start += 1
		plen += 1
	#print(memo)
			
				

if __name__ == '__main__':

	n = int(input())

	s = input()

	result = substrCount(n, s)

	print(str(result) + '\n')

	
