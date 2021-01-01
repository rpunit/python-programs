from collections import defaultdict


class Graph  :

	def __init__(self) :
		self.nodes = defaultdict (list)
		self.visited = defaultdict(bool) 


	def addEdge (self, v, edge) :
		self.nodes[v].append(edge)
		self.visited[v] = False
		self.visited[edge] = False
		

	def recurse(self, stack, k) :
		edges = self.nodes[k]
		self.visited[k] = True
		for e in edges :
			if  not self.visited[e] :
				self.recurse(stack, e) 

		stack.append(k)

	def topologicalSort (self ) :
		print(self.nodes)
		print(self.visited)
		stack = []	
		
		for k in list(self.nodes) :
			if not self.visited[k] :
				self.recurse(stack, k) 

		print (stack)


graph = Graph ()

graph.addEdge("a","c")
graph.addEdge("a","b")
graph.addEdge("a","d")
graph.addEdge("c","e")
graph.addEdge("b","d")


graph.topologicalSort()


