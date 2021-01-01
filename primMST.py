# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 
  
import sys # Library for INT_MAX 
from  heapq import *

class Edge :
	def __init__ (self, v, w, wt) :
		self.v = v
		self.w = w
		self.wt = wt
	def __lt__ (self, that) :
		return self.wt < that.wt

	def __repr__(self) :
		return  "Edge ( %d --> % d :weight %d ) " % (self.v, self.w, self.wt)
  

class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[]] * self.V
  
	
	def printMST (self, mst) :
		for edge in mst: 
			print (edge)

	def addGraph(self, matrix):
		for i in range(self.V) :	
			for j in range(self.V) :	
				if i != j and matrix[i][j] != 0:
					edge  = Edge(i, j, matrix[i][j])
					self.graph[i].append( edge)
			
		

	def visit (self, visited, mh, v) :
		visited[v] = 1
		for edge in self.graph[v] : 
			if edge.w not in visited :		
				heappush(mh, edge)

	def primMST(self) :
		minHeap = []	
		mst = []				
		visited = {} 
		self.visit(visited, minHeap, 0)

		while len(minHeap) != 0 and len(mst) != self.V -1 :
			#print ("---", minHeap)
			curEdge = heappop(minHeap)

			if curEdge.v in visited and curEdge.w in visited :
				continue	

			mst.append(curEdge)
		
			self.visit ( visited, minHeap, curEdge.v)	
			self.visit ( visited, minHeap, curEdge.w)	
				
		
		self.printMST(mst)

			
			
	 
g = Graph(5) 
g.addGraph ([ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] )
  
g.primMST(); 

  
