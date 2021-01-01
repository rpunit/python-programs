#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/
# 2 4 5 9 12 15
def hackerlandRadioTransmitters(x, k):

	if len(x) < 2 :
		return 1
	x.sort()
	print(x)
	i = 0
	count =0
	while i < len(x):
		j = i+1	
		while j < len(x) and x[j] -x[i] <= k:
			j+=1
		#for j in range(i+1,len(x)) :
			#if x[j] - x[i] >= k :
				#break
		count +=1
		j -=1 
		i = j 
		while j < len(x) and x[j] -x[i] <= k:
			j+=1
		i = j
	return count

if __name__ == '__main__':

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	x = list(map(int, input().rstrip().split()))

	result = hackerlandRadioTransmitters(x, k)

	print(str(result) + '\n')

