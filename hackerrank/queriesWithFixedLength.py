#!/bin/python3

import os
import sys
from collections import deque

# Complete the solve function below.
def solve(arr, queries):
	out = []
	for q in queries :
		deq = deque(arr[:q-1])
		minv = sys.maxsize
		if len(deq) > 0 :
			prev_max = max(deq)
		else :
			prev_max = -sys.maxsize

		for i in range(q-1, len(arr)) :
			deq.append (arr[i])
			maxv = max(prev_max, arr[i])
			#print (i, maxv, minv)
			if maxv < minv :
				minv = maxv
			v = deq.popleft()	
			if v >= maxv :
				if len(deq) > 0 :
					prev_max = max(deq)
				else :
					prev_max = -sys.maxsize
			else :
				prev_max = maxv
		#print(minv)
		out.append(minv)
	return out


if __name__ == '__main__':

	nq = input().split()

	n = int(nq[0])

	q = int(nq[1])

	arr = list(map(int, input().rstrip().split()))

	queries = []

	for _ in range(q):
		queries_item = int(input())
		queries.append(queries_item)

	result = solve(arr, queries)

	print('\n'.join(map(str, result)))

