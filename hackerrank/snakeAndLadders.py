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
	for i in range(1,100) :
		for j in range(1,7):
			
			if i+j in lmap :
				graph[i].append(lmap[i+j])
			elif i+j in smap :
				graph[i].append(smap[i+j])
			elif j+i <= 100 :
				graph[i].append(i+j)

	visited = {}
	queue = []
	queue.append(1)
	visited[1] = 0
	route = defaultdict(list)

	while len(queue) > 0 :
		cur = queue.pop(0)
	
		if cur == 100 :
			#print("route = ", route[cur])
			return visited[cur] 
			
		for n in graph[cur]:
			if n not in visited :
				queue.append(n)
				visited[n] = visited[cur] + 1
				route[n] = route[cur]
				route[n].append(n)
			elif visited[n] > visited[cur] + 1:
				visited[n] = visited[cur] + 1
				route[n] = route[cur]
				route[n].append(n)
	return -1


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

		fptr.write(str(result) + '\n')

	fptr.close()
