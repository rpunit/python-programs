
def maxAmount (n, m, seats ) :
	total = 0
	i = n 
	while i > 0 :
		print(i, seats, total)
		total += seats[-1] 		 
		seats[-1] -= 1
		seats = sorted(seats, reverse=False)
		i -= 1
	return total



# Driver code 
if __name__ == '__main__': 
    seats = [1, 2, 4] 
    M = len(seats) 
    N = 3
  
    print(maxAmount(N, M, seats)) 
  
