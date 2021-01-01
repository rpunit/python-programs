import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def getNewState(curState, y,x, yMin, xMin, yMax, xMax) :

	#print("getNewState", curState, y,x, yMin, xMin, yMax, xMax)
	if curState == "up" :
		if y >= yMax-1:
			return "right" 
		
	if curState == "right" :
		if x >=xMax -1:
			return "dn" 

	if curState == "dn" :
		if y <= yMin :
			return "left" 

	if curState == "left" :
		if x <= xMin :
			return "up" 
	return curState

def rotaeEachLayer(matrix, layer, r) :
	m,n = len(matrix[0]) - 2*layer, len(matrix) -2*layer 
	maxRot = 2*(m + n -2)
	r1 = r % maxRot
	if r1 != r :
		print ("%d truncated to %d" %(r, r1))
	for i in range(r1) :
		rotate(matrix, layer) 

def rotate(matrix, layer) :
	m,n = len(matrix[0]) - 2*layer, len(matrix) -2*layer 
	xMin,xMax = layer, len(matrix[0]) - layer 
	yMin,yMax = layer, len(matrix) - layer
	maxRot = 2*(m + n -2)
	count = 0
	x,y  = xMin,yMin
	first = matrix[y][x]
	prev = first
	state = "up"
	#print("xMin, yMin, xMax, yMax, maxRot", xMin, yMin, xMax, yMax, maxRot, layer)
	while count < maxRot :
		#print(y,x, state, prev, count)
		if state == "up" :
			y += 1
		elif state == "right":
			x+=1
		elif state == "dn":
			y-=1	
		elif state == "left":
			x-=1
		state = getNewState(state,y,x,yMin, xMin, yMax, xMax)
			
		count += 1	
		#print("--", y,x, state, matrix[y][x])
		cur = matrix[y][x]
		#if x == xMin +1  and y == yMin  :
		#	matrix[y][x] = first
		#else :
		matrix[y][x] = prev
		prev = cur
	

def rotateR (matrix, r):
	xm = len(matrix[0])
	ym = len(matrix)
	maxLevel = min ((xm-1)//2, (ym-1)//2)
	for l in range(maxLevel+1):
		rotaeEachLayer(matrix, l, r)


# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
	rotateR(matrix, r)

m,n = 5,4

matrix= [[] for j in range(m)]

#1 2 3 4
#7 8 9 10
#13 14 15 16
#19 20 21 22
#25 26 27 28
#matrix[0] = [1,2,3,4]
#matrix[1] = [7,8,9,10]
#matrix[2] = [13,14,15,16]
#matrix[3] = [19,20,21,22]
#matrix[4] = [25,26,27,28]

#print(matrix[4][0])
#matrixRotation(matrix, 7)
#print(matrix)



if __name__ == '__main__':
	fd = open("matrixinput2.txt", "r") 
	mnr = fd.readline().rstrip().split()

	m = int(mnr[0])

	n = int(mnr[1])

	r = int(mnr[2])

	matrix = []

	for _ in range(m):
		matrix.append(list(map(int, fd.readline().rstrip().split())))

	print(matrix)
	matrixRotation(matrix, r)
	print(matrix)
