#!/bin/python3

import math
import os
import random
import re
import sys

# 1221


	
# Complete the fairRations function below.
def fairRations(B):
	count = 0
	tsum = 0
	for i,a in enumerate(B) :
		tsum += a
		if a % 2 == 1:
			B[i] +=1
			B[i+1] +=1
			count +=2
	
	print (tsum, count)
	if tsum %2 ==1:
		return "NO"
	else :
		return count

if __name__ == '__main__':

	N = int(input())

	B = list(map(int, input().rstrip().split()))

	result = fairRations(B)

	print(str(result) + '\n')


