#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def getCount (a1,a2,a3) :
	count = 0
	a1.sort()
	a2.sort()
	a3.sort()
	for i in a1:
		for j in a2:
			for k in a3:
				if i<j and j < k :
					count +=1 
	return count

def getCount1 (a1, a2, a3) :
	count = 0
	a1.sort()
	a2.sort()
	a3.sort()
	for i,a in enumerate(a1):
		j = 0
		k =0
		while j< len(a2) :
			if   a2[j] > a1[i] :
				break
			j+=1
		if j >= len(a2) :
			break
		while k < len(a3) :
			if  a3[k] > a2[j]:
				break
			k+=1
		if k >= len(a2) :
			break
		print ("---", i,j,k) 
		print(a1[i], a2[j], a3[k])
		if a1[i] < a2[j] and a2[j] < a3[k]:
			count += (len(a2)-j)*(len(a3) - k)
	return count

# Complete the countTriplets function below.
def countTriplets(arr, r):
	maps = defaultdict(list)

	for i,a in enumerate(arr) :
		maps[a].append(i)

	count = 0
	print (maps)
	for i in maps :
		if i*r in maps and i*r*r in maps :
			print (i,maps[i],maps[i*r],maps[i*r*r])
			tc = getCount(maps[i], maps[i*r], maps[i*r*r])
			print (i, tc)
			count += tc
	return count

if __name__ == '__main__':

	nr = input().rstrip().split()

	n = int(nr[0])

	r = int(nr[1])

	arr = list(map(int, input().rstrip().split()))

	ans = countTriplets(arr, r)

	print(str(ans) + '\n')


