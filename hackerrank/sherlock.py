#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the isValid function below.
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def isValid(s):
	maps = defaultdict(int)
	for a in s :
		maps[a]+=1
	map2 = defaultdict(int)
	for item in maps.items() :
		map2[item[1]]+=1
	print (maps, map2)
	if len(map2) < 2 :
		return "YES"
	elif len(map2) == 2 :
		items = list(map2.items())
		if (items[0][1] == 1 or items[1][1] == 1) :
			if (items[0][0] ==1 and items[0][1] ==1) or  (items[1][0] == 1 and items[1][1] == 1): 
				return "YES"
			elif  abs(items[0][0]- items[1][0]) == 1 : 
				return "YES"
			
	return "NO"
   

	
		

if __name__ == '__main__':

	s = input()

	result = isValid(s)

	print(result + '\n')


