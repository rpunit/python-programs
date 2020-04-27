# Implementing a graph proper way

class Node:

	# static variable 
	count = 0 

	def __init__ (self, data) :
		self.data = data
		self.edges = []
		Node.count += 1

	def add_edge(self, edge) :
		self.edges.append(edge)



	def _tdfs (self, node, visited) :
		visited[node] = True
		print (node.data)
		
		for n in node.edges :
			if n not in visited.keys() or visited[n] == False:
				self._tdfs(n, visited)

	def traverse_dfs  (self) :
		visited = {}
		self._tdfs (self, visited )

	def _tbfs (self, node, visited, queue) :

		queue.append(node)
		while (len(queue) != 0 ) :
			n = queue.pop(0)
			if n not in visited :
				print (n.data) 
				visited[n] = True
				for v in n.edges :
					queue.append(v)
			
	def _rec_bfs (self, index, visited, queue, target, path) :
			if len(queue) == 0:
				return 
			n = queue.pop(0) 
			if path != None :
				path[index] = n.data
			if target != None and n.data == target.data :
				print("reached target ", n.data)
				print("path to target ", path)
				return 

			if n not in visited :
				print(n.data)
				visited[n] = True
				for v in n.edges :
					if v not in visited :
						queue.append(v)
			self._rec_bfs(index + 1, visited, queue, target, path) 
			

	def traverse_bfs(self) :
		visited = {}
		queue = []
		self._tbfs (self, visited, queue)
		
	def traverse_bfs_rec(self) :
		visited = {}
		queue = []
		queue.append(self)
		print ( list(map(lambda x: x.data , self.edges )))
		self._rec_bfs(0, visited, queue, None, None)

	def find_path(self, target) :
		visited = {}
		queue = []
		queue.append(self)
		path = [0]*self.count
		print ( list(map(lambda x: x.data , self.edges )))
		self._rec_bfs(0, visited, queue, target, path)


####################
#          (7) -->  (5) <--->  (6) <---->   (3)  <----> (4)
#              					\--> (8) 
#            
	     

graphroot = Node(3)

# Lets add a new vertex

vert = Node(4)

# Lets connect the vertex.

vert.add_edge(graphroot)
graphroot.add_edge(vert)

# adding more vertices

vert2=Node(6)
vert2.add_edge(graphroot)

graphroot.add_edge(vert2)

vert3= Node(5)
vert2.add_edge(vert)
vert.add_edge(vert2)

vert3.add_edge(vert2)
vert2.add_edge(vert3)

vert4= Node(7)
vert3.add_edge(vert4)

vert5 = Node(8)
graphroot.add_edge(vert5)

print("dfs")
graphroot.traverse_dfs()
print("bfs")
graphroot.traverse_bfs()
		

print("bfs recursive")
graphroot.traverse_bfs_rec()

print("find  path")
graphroot.find_path(vert3)
