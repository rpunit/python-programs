#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
	graph = defaultdict(list)
	lmap = {}
	smap = {}
	for (s,e) in ladders :
		lmap[s] = e
	for (s,e) in snakes :
		smap[s] = e
	maxn = 100
	for i in range(1,maxn) :
		for j in range(1,7):
			if j+i in lmap :
				graph[i].append(lmap[i+j])
			elif j+i in smap :
				graph[i].append(smap[i+j])
			elif j+i <= maxn :
				graph[i].append(i+j)

	visited = {}
	queue = []
	queue.append(1)
	visited[1] = 0
	route = defaultdict(list)
	#print(graph)

	while len(queue) > 0 :
		cur = queue.pop(0)
	
		if cur == maxn :
			print("route = ", route[cur])
			#print("visited = ", visited)
			return visited[cur] 
			
		for n in graph[cur]:
			if n not in visited :
				queue.append(n)
				visited[n] = visited[cur] + 1
				route[n] = route[cur][:]
				route[n].append(n)
				#print (cur, n, visited[n], route[n]) 
			elif visited[n] > visited[cur] + 1:
				#print("---", cur, route[n], route[cur] )
				visited[n] = visited[cur] + 1
				route[n] = route[cur][:]
				route[n].append(n)
	return -1


if __name__ == '__main__':

	t = int(input())

	for t_itr in range(t):
		n = int(input())

		ladders = []

		for _ in range(n):
			ladders.append(list(map(int, input().rstrip().split())))

		m = int(input())

		snakes = []

		for _ in range(m):
			snakes.append(list(map(int, input().rstrip().split())))

		result = quickestWayUp(ladders, snakes)

		print(str(result) + '\n')


