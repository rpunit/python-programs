#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#https://www.hackerrank.com/challenges/flatland-space-stations/problem
# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
	c = sorted(c)
	print(n,c)
	maxnd = -1
	for i in range(n) :
		l = bisect.bisect_left(c,i)   
		if l >= len(c) :
			nd = i - c[-1]
		else :
			print(i,l,c[l])
			if l >0 : 
				nd =  min(abs(c[l]-i), abs(c[l-1]-i))
			else :
				nd = c[l]
		if nd > maxnd:
			maxnd = nd
	return maxnd
		



if __name__ == '__main__':

	nm = input().split()

	n = int(nm[0])

	m = int(nm[1])

	c = list(map(int, input().rstrip().split()))

	result = flatlandSpaceStations(n, c)

	print(str(result) + '\n')


