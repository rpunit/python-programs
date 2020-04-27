def commonChild(s1, s2):
	len_str1 = len(s1)
	len_str2 = len(s2)

	# memo contains the longest substring from 0 .. i-1, j-1
	memo = [ [ 0 for i in range(len_str2 + 1) ] for j in range(len_str1 + 1) ]

	for i in range(len_str1 + 1) :		
		for j in range(len_str2 + 1) :		
			if i == 0 or j == 0 :
				memo[i][j] = 0
			elif 	s1[i-1] == s2[j-1] :
				memo[i][j] =  memo[i-1][j-1] + 1	
			else :
				memo[i][j] =  max( memo[i-1][j], memo[i][j-1] )
	
	return memo[len_str1][len_str2] 


print(commonChild("shinchan", "noharaa"))
