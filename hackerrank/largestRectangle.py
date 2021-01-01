#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):

	# 1 2 3 4 5 
	maxrect = 0 
	stack = []
	# this makes sure stack is flushed in the end
	h.append(0)
	for i in range(len(h)):
		curh = h[i] 
		lasti = i
		while len(stack) > 0  and curh <= stack[-1][0] :
			top = stack.pop(-1)	
			lasth = top[0]
			lasti = top[1]
			maxrect = max (maxrect, curh*( i+1 -lasti))
			maxrect = max (maxrect, lasth*(i - lasti))
			print (i, lasti, top, maxrect) 
		stack.append((h[i],lasti))

	return maxrect
				

if __name__ == '__main__':

	n = int(input())

	h = list(map(int, input().rstrip().split()))

	result = largestRectangle(h)

	print(str(result) + '\n')


