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

#  1 3 1 3 9
# Complete the countTriplets function below.
def countTriplets(arr, r):
	map2 = defaultdict(int)
	map3 = defaultdict(int)
	count = 0
	for i,a in enumerate(arr) :
				
		if a in map2 :
			map3[a*r] += map2[a] 

		if a in map3 :
			count += map3[a] 
			
		map2[a*r] +=1
		
	return count

if __name__ == '__main__':

	nr = input().rstrip().split()

	n = int(nr[0])

	r = int(nr[1])

	arr = list(map(int, input().rstrip().split()))

	ans = countTriplets(arr, r)

	print(str(ans) + '\n')


