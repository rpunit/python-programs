#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
	maps = defaultdict(int)
	mapf = defaultdict(int)
	out = []
	for  o,v in queries :
		if o == 1:
			maps[v] +=1
			mapf[maps[v]] = 1
		elif o == 2:
			if v in maps and maps[v] > 0:
				maps[v] -=1
				mapf[maps[v]] = 1
		elif o == 3 :
			#va = list(filter(lambda x : x == v, list(maps.values())))
			#if len(va) > 0 :
			if v in mapf :
				out.append(1)
			else :
				out.append(0)
	return out

if __name__ == '__main__':

	q = int(input().strip())

	queries = []

	for _ in range(q):
		queries.append(list(map(int, input().rstrip().split())))

	ans = freqQuery(queries)

	print('\n'.join(map(str, ans)))
	print('\n')


