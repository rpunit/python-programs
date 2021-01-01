#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem
if __name__ == '__main__':
	road_nodes, road_edges = map(int, input().split())

	road_from = [0] * road_edges
	road_to = [0] * road_edges
	road_weight = [0] * road_edges

	graph = defaultdict(defaultdict)
	for i in range(road_edges):
		road_from[i], road_to[i], road_weight[i] = map(int, input().split())
		if road_to[i] in graph[road_from[i]] :
			w =	graph[road_from[i]][road_to[i]]
			# just use the least wt between edges
			if  w > road_weight[i] :
				graph[road_from[i]][road_to[i]] = road_weight[i]

		else :
			graph[road_from[i]][road_to[i]] = road_weight[i]

	q = int(input())

	queries = defaultdict(list)
	querylist = []
	#print(graph)
	for q_itr in range(q):
		xy = input().split()

		x = int(xy[0])

		y = int(xy[1])
		queries[x].append(y)
		querylist.append((x,y))

	results = defaultdict(list)	
	for  x  in queries :	
		queue = []
		queue.append(x)
		visited = defaultdict(int)
		visited[x] = 0
		while len(queue) > 0 :
			cur = queue.pop(0)
			for t in graph[cur].keys() :
				w = graph[cur][t]
				if t not in visited :
					visited[t] = w + visited[cur]
					queue.append(t)
				elif visited[t] > w + visited[cur] :
					visited[t] = visited[cur] + w
		for v in visited :
			results[(x,v)] = visited[v]
			if x == 178 and v == 187 :
				print (visited) 
	#print(results)
	for x,y in querylist :
		tup = (x,y)
		if tup in results :
			print (tup, results[tup])
		else :
			print (-1)

