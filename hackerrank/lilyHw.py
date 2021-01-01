#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/lilys-homework/problem
def getNSwap(arr, sarr) :
	numSwap = 0
	imap = {}
	for i in range(len(arr)) :
		imap[arr[i]] = i
	
	for i in range(len(arr)) :
		if arr[i] != sarr[i]: 
			# swap arr[i] with sarr[i]
			new_index = imap[sarr[i]]
			imap[arr[i]] = new_index
			arr[i], arr[new_index] = sarr[i], arr[i]
			numSwap +=1

	return numSwap

# Complete the lilysHomework function below.
def lilysHomework(arr):
	sarr = sorted(arr)
	nd1 = getNSwap (arr.copy(), sarr)
	sarr2 = sorted(arr, reverse=True)
	nd2 = getNSwap(arr.copy(), sarr2)
	print (nd1,nd2)

	return min(nd1, nd2) 


if __name__ == '__main__':

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	result = lilysHomework(arr)

	print(str(result) + '\n')


