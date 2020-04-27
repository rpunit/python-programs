from  collections import defaultdict 


class Graph  :
	
	def __init__(self):
		self.graph = defaultdict(list) 

	def addEdge (self, u, v) :
		self.graph[u].append(v)

	def DFSUtil (self, v , visited) :

		visited[v] = True
		print(v)
		for u in self.graph[v] :
			if visited[u] == False : 
				self.DFSUtil(u, visited)
		
		

	# The function to do DFS traversal. It uses 
	# recursive DFSUtil() 
	def DFS(self, v): 
		visited = [False]* (len(self.graph))
		self.DFSUtil (v, visited)


# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)


	
	

