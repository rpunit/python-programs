#!/bin/python3

import math
import os
import random
import re
import sys

def moveToDir (move) :
	if move == (1,0) :
		return "R"
	if move == (0,1) :
		return "D"
	if move == (0,-1) :
		return "U"
	if move == (-1, 0) :
		return "L"

def minimumMoves(grid, startX, startY, goalX, goalY):
	#  right dn left up 
	moves = [ (1,0),  (0,1), (-1,0), (0,-1)]
	# Queue has the list list of moves
	queue = []
	# elements are x,y, nummoves, dir
	queue.append((startX, startY, 0, "X"))
	visited = {} 
	visited[(startX,startY)] = 0

	while len(queue) > 0 :	
		i,j,n,dirp = queue.pop(0)

		for move in moves :
			ni =i + move[0]  
			nj =j + move[1]  
			while  ni >= 0 and ni <len(grid) and \
				nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == "."  :
					newDir =   moveToDir(move)
					newTurn = n
					if newDir != dirp : # and dirp != "X":
						newTurn +=1

					if ni == goalX and nj == goalY :
						return  newTurn 

					if  (ni,nj) not in visited:
						queue.append( (ni, nj, newTurn, newDir))
						visited[(ni,nj)] = newTurn
					elif visited[(ni,nj)] > newTurn :
							if ni==goalX and nj==goalY :
								print("Found lower" , ni,nj,visited[(ni,nj)] , newTurn )
							visited[(ni,nj)] = newTurn
					ni =ni + move[0]  
					nj =nj + move[1]  
						
	return visited[(goalX, goalY)] 
		
	
if __name__ == '__main__':
	n = int(input())

	grid = []

	for _ in range(n):
		grid_item = input()
		grid.append(grid_item)

	startXStartY = input().split()

	startX = int(startXStartY[0])

	startY = int(startXStartY[1])

	goalX = int(startXStartY[2])

	goalY = int(startXStartY[3])

	result = minimumMoves(grid, startX, startY, goalX, goalY)

	print(str(result) + '\n')


