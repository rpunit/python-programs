import math
import os
import random
import re
import sys
from   heapq import *

class Query :
	def __init__ (self, query) :
		self.start = query[0]
		self.stop = query[1]
		self.k = query[2]

	def __lt__(self, other):
		return self.stop < other.stop

	def __repr__ (self) :
		return "start:%d stop:%d k:%d" % (self.start, self.stop, self.k)

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
	max_s = 0
	heap = []

	queries = list(map( lambda x : Query(x), queries) )
	queries = sorted(queries, key = lambda x: x.start)
	maxv = 0
	val = 0 
	for i in range(0, len(queries)) :	
		q = queries[i] 	
		#print (i, q, heap)
		# remove all the non intersecting indexes
		while (len(heap) > 0 and heap[0].stop < q.start ) :
			qv = heappop(heap) 
			val -= qv.k 

		heappush(heap, q)
		val  += q.k 
		if val > maxv :
			#print("Found max", val) 
			maxv = val

	return maxv
				 
n = 4
#queries= [[1,5,3],[4,8,7],[6,9,1]]
#queries=[[2,6,8],[3,5,7] ,[1,8,1] ,[5,9,15]]
#queries = [[2,3,603], [1,1,286], [4,4,882]]
#queries = [[29,40,787], [9,26,219], [21,31,214], [8,22,719], [15,23,102], [11,24,83], [14,22,321], [5,22,300], [11,30,832], [5,25,29], [16,24,577], [3,10,905], [15,22,335], [29,35,254], [9,20,20], [33,34,351], [30,38,564], [11,31,969], [3,32,11], [29,35,267], [4,24,531], [1,38,892], [12,18,825], [25,32,99], [3,39,107], [12,37,131], [3,26,640], [8,39,483], [8,11,194], [12,37,502]]
#print(arrayManipulation(n,queries)) 
if __name__ == '__main__':
	fi = open("./array.txt", "r" ) 

	nm = fi.readline().split()

	n = int(nm[0])

	m = int(nm[1])

	queries = []

	for _ in range(m):
		queries.append(list(map(int, fi.readline().rstrip().split())))

	result = arrayManipulation(n, queries)

	print(str(result) + '\n')



