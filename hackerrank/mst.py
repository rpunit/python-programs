#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from heapq import *

def getIndexWithMinWt(wts, visited) :
	minwt = sys.maxsize
	minindex = 0
	for i in wts :
		if i not in visited and wts[i] < minwt:
			minwt = wts[i]
			minindex = i
	return minindex

def getTargetWt(source, target, graph)  :
	for e in graph[source] :
		if e[0] == target :
			return e[1]
	return sys.maxsize

# Complete the prims function below.
def prims(n, edges, start):
	graph = defaultdict(list)
	for e in edges :
		graph[e[0]].append((e[1],e[2]))
		graph[e[1]].append((e[0], e[2]))

	wts = {} 
	for i in graph :
		wts[i] = sys.maxsize
	wts[start] = 0
	visited = defaultdict(int)
	print(graph)
	#while sum(map(lambda x : x[1], visited.items())) < len(graph) :
	for i in range(len(graph)) :

		cur = getIndexWithMinWt(wts, visited)
		visited[cur] = 1
		print( cur, visited, wts)
		
		for t,w in graph[cur]  :
			if cur != t and w < wts[t] and t not in visited:
				wts[t] = w 

	print (wts)
	return sum(map(lambda x : x[1], wts.items()))



if __name__ == '__main__':

	nm = input().split()

	n = int(nm[0])

	m = int(nm[1])

	edges = []

	for _ in range(m):
		edges.append(list(map(int, input().rstrip().split())))

	start = int(input())

	result = prims(n, edges, start)

	print(str(result) + '\n')

