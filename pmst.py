# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 
  
import sys # Library for INT_MAX 
from heapq import *
  
class Graph(): 
  
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)]  for row in range(vertices) ]
			

	def visit(self, heap, mst ) :
		print (heap, mst) 
		for i in range(self.V)  :
			if  mst[i] :
				for j in range(self.V)  :
					wt = self.graph[i][j]
					if j != i and wt != 0 and not mst[j]:
						print ("Adding wt, i",  wt, i)
						heappush(heap, (wt,i,j)) 
			
	
	def primMST(self) :
		mstSet = [False] * self.V
		parent = [0] * self.V
		heap = []
		mstSet[0] = True

		while (sum(mstSet) < self.V ) :
			self.visit(heap, mstSet) 
			print ("heap" , heap )
			(wt1,v1,v2) = heappop(heap)
			mstSet[v2] = True
			print ("w1, v1" , wt1, v1, v2 )
			parent[v2] = v1

		for i in range(len(parent)) :
			print ("%d <- %d  " % (parent[i], i) ) 
			
			
			
	 
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 
  
g.primMST(); 

  
