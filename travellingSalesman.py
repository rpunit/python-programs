# Driver code 
  
answer = [] 

def tsp(graph, visited, curPos, n, count, cost ,tarr ) :

	if count == n and graph[curPos][0] != 0:
		cost = (cost + graph[curPos][0]) 
		print(cost, tarr)
		return answer.append(cost) 

	for i in range(len(graph[curPos])) :
		w = graph[curPos][i]
		if visited[i] == 0  and w != 0:
			visited[i] = 1
			tarr[count-1] = i
			tsp(graph, visited, i, n, count + 1, cost + w, tarr)
			visited[i] = 0

	return 0
	
			

# n is the number of nodes i.e. V 
if __name__ == '__main__': 
	n = 4
	graph= [[ 0, 10, 15, 20 ], 
			[ 10, 0, 35, 25 ], 
			[ 15, 35, 0, 30 ], 
			[ 20, 25, 30, 0 ]] 
  
	# Boolean array to check if a node 
	# has been visited or not 
	v = [False for i in range(n)] 

	tarr = [0]*n
	  
	# Mark 0th node as visited 
	v[0] = True
  
	# Find the minimum weight Hamiltonian Cycle 
	tsp(graph, v, 0, n, 1, 0, tarr)
  
	# ans is the minimum weight Hamiltonian Cycle 
	print(min(answer)) 
