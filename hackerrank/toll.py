#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	road_nodes, road_edges = map(int, input().split())

	road_from = [0] * road_edges
	road_to = [0] * road_edges
	road_weight = [0] * road_edges

	re_map = {}
	for i in range(road_edges):
		road_from[i], road_to[i], road_weight[i] = map(int, input().split())
		re_map[(road_from[i], road_to[i])] = road_weight[i]
	
	memo = [ [ 0 for i in range(road_nodes+1)] for j in range(road_nodes+1)]
	
	for i in range(road_nodes+1) :
		for j in range(road_nodes + 1) :
			if i == j or i == 0 or j == 0:
				# dist from i to i is 0
				memo[i][j] == 0

			if i in road_from :
				if j in road_to :
					if (i,j) in re_map :
						wt = re_map[(i,j)]
						memo[i][j] = wt
						memo[j][i] = 1000 - wt
	
	for i in range(road_nodes+1) :
		for j in range(road_nodes + 1) :
			for k in range(j-i) :
				if memo[i][k] != 0 and memo[k][j] != 0 :
						new_toll = memo[i][j] = memo[i][k] + memo[k][j]
						if memo[i][j] == 0 :
							memo[i][j] = new_toll
						elif new_toll < memo[i][j] :
							memo[i][j] = new_toll

	print("memo", memo)

