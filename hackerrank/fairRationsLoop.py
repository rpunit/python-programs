#!/bin/python3

import math
import os
import random
import re
import sys

# 1221
def isEven (B) :
	for i in B :
		if i %2 == 1 :
			return False
	return True

memo = {}
def frUtil(B,i, c) :
	#print(i,c,B)
	if  (i,c) in memo :
		return memo[(i,c)]
	if i >= len (B) :
		if isEven(B) :
			print(B)
			return c
		else :
			return sys.maxsize
	
	temp = B
	c1 = sys.maxsize
	c2 = sys.maxsize
	c3 = sys.maxsize
	if i > 0 :
		temp[i] +=1
		temp[i-1] +=1 
		c1 = frUtil(temp, i+1, c+2)
		temp[i] -=1 
		temp[i-1] -=1 
	if i < len(B)-1 :
		temp[i+1] +=1
		temp[i] +=1
		c2 = frUtil(temp, i+1,c+2)
		temp[i] -=1 
		temp[i+1] -=1 
	c3 = frUtil(temp, i+1, c)
	minc =  min(c1,c2,c3)
	memo[(i,c)] = minc
	return minc

	
# Complete the fairRations function below.
def fairRations(B):
	ret = frUtil(B, 0, 0) 
	print (ret)
	if ret == sys.maxsize :
		return "NO"
	else :
		return ret

if __name__ == '__main__':

	N = int(input())

	B = list(map(int, input().rstrip().split()))

	result = fairRations(B)

	print(str(result) + '\n')


