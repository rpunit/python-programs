#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
	len_str1 = len(s1)
	len_str2 = len(s2)

	# memo contains the longest subseq from 0 .. i-1, j-1
	memo = [ [ 0 for i in range(len_str2 + 1) ] for j in range(len_str1 + 1) ]
	print (len_str1, len_str2)

	for i in range(len_str1 + 1) :
		for j in range(len_str2 + 1) :
			if i == 0 or j == 0 :
				memo[i][j] = 0
			elif	s1[i-1] == s2[j-1] :
				memo[i][j] =  memo[i-1][j-1] + 1
			else :
				memo[i][j] =  max( memo[i-1][j], memo[i][j-1] )

	return memo[len_str1][len_str2]

if __name__ == '__main__':

	s1 = input()

	s2 = input()

	result = commonChild(s1, s2)

	print(str(result) + '\n')


