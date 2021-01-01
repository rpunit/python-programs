#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

	

class GraphNode :
	def __init__ (self, targ, wt) :
		self.entry = defaultdict(list)
		self.entry[targ].append(wt)
		self.entry[targ] = sorted(self.entry[targ])
	
	def getNbrs(self) :
		return self.entry.keys()
		
	def addWt(self, target, wt) :
		self.entry[target].append(wt)
		self.entry[target] = sorted(self.entry[target])
		if len(self.entry[target]) > 1 :
			print ("--",target, self.entry[target])

	def getWt(self, target) :
		if target in self.entry :
			return self.entry[target][0]
		else :
			return -1
		
	
# Complete the shortestReach function below.
def shortestReach(n, edges, s):
	graph = defaultdict(list)
	for e in edges :
		if e[0] in graph :
			graph[e[0]].addWt(e[1],e[2])
		else :
			graph[e[0]]  = GraphNode(e[1], e[2])	
			
		if e[1] in graph :
			graph[e[1]].addWt(e[0], e[2])
		else :
			graph[e[1]]  = GraphNode(e[0], e[2])	
			
			
	for i in range(1, n+1):
		if i not in graph:
			graph[s] = GraphNode (i,-1)
	visited = defaultdict(int)
	print(graph)
	queue = [s]
	visited[s] = 0 
	while len(queue) > 0 :
		cur = queue.pop(0)
		node = graph[cur]
		for n in node.getNbrs() :
			if n not in visited :
				visited[n] = visited[cur] + node.getWt(n)
				queue.append(n)
			elif visited[n] > visited[cur] + node.getWt(n) :
				#print("Found lower", n, cur, visited[n], visited[cur] +  node.getWt(n))
				visited[n] = visited[cur] + node.getWt(n) 

	return map(lambda x : x[1], sorted(filter(lambda x : x[0] !=s, visited.items()), key = lambda x : x[0]))

if __name__ == '__main__':

	t = int(input())

	for t_itr in range(t):
		nm = input().split()

		n = int(nm[0])

		m = int(nm[1])

		edges = []

		for _ in range(m):
			edges.append(list(map(int, input().rstrip().split())))

		s = int(input())

		result = shortestReach(n, edges, s)

		print(' '.join(map(str, result)))
		print('\n')


