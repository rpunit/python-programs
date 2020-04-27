# Implementing a graph proper way

class Node:

	def __init__ (self, data) :
		self.data = data
		self.edges = []
		self.path = "" 

	def setPath(self, p) :
		self.path = path

	def add_edge(self, edge) :
		self.edges.append(edge)

	def __str__ (self) :
		temp = ""
		for e in self.edges :
			temp = temp + " " + str(e.data)
		return "this = %s,  edges = %s " % (str(self.data), temp ) 


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
			

	def traverse_bfs(self) :
		visited = {}
		queue = []
		self._tbfs (self, visited, queue)



	def _sps (self, end, visited, queue ) :

		if len(queue) <= 0:
			return

		node = queue.pop(0) 
		#print("node-->" + str(node))

		if node not in visited :

			if node.data == end.data :
				path = node.path + "-->" + ",".join((map(lambda x : str(x), node.data)))
				print (path)
			visited[node] = True
			for n in node.edges :
				n.path = node.path + "--" + ",".join((map(lambda x : str(x), node.data)))
				queue.append(n)		 
		self._sps( end, visited, queue)

	def _sp (self, node, end, visited, queue, path) :
		queue.append(node) 
			
		while (len(queue) > 0 ) :
			n = queue.pop(0)
			if n not in visited :
				visited[n] = True
				path = path + "--" + "".join((map(lambda x : str(x), n.data)))
				print(n)
				if n.data == end.data :
					print (path)
					return True;
				for v in n.edges :
					queue.append(v)

				

	def shortest_path(self, start, end ) :
		visited = {}
		queue = []
		queue.append(start) 
		self._sps (end, visited, queue)
		

# build the graph starting from position (0,0) 
root = Node([0,0])

def get_next_move ( i, j) :
	moves = []
	if i + 1 < 8 :
		if j + 2 < 8:
			moves.append([i + 1, j + 2])
		if j - 2 >=  0:
			moves.append([i + 1, j - 2])

	if i - 1 >= 0 :
		if j + 2 < 8:
			moves.append([i - 1, j + 2])
		if j - 2 >=  0:
			moves.append([i - 1, j - 2])

	if i + 2 < 8 :
		if j + 1 < 8:
			moves.append([i + 2, j + 1])
		if j - 1 >=  0:
			moves.append([i + 2, j - 1])

	if i - 2 >= 0 :
		if j + 1 < 8:
			moves.append([i - 2, j + 1])
		if j - 1 >=  0:
			moves.append([i - 2, j - 1])

	return moves



		

#visited = [ [ False for i in range(8) ] for j in range(8)]
nodes = [ [ False for i in range(8) ] for j in range(8)]
def build_graph (node, i, j) :
	for (ii,jj)  in get_next_move(i,j)  : 
		if not nodes[ii][jj] :
			nodes[ii][jj] =  Node([ii,jj])
		n = nodes[ii][jj]
		if n not in node.edges :
			node.add_edge(n)
			#print("Adding %s to  %s " % (n.data, node.data))
			#print (node)
			build_graph(n, ii, jj)

build_graph(root, 0,0)

n1 = nodes[0][0]
n2 = nodes[7][7]
print (n1)
print (n2)

root.shortest_path (n1, n2)
