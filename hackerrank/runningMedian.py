#!/bin/python3

import os
import sys
from  heapq import *
#
# Complete the runningMedian function below.
#
def runningMedian(a):
	#
	# Write your code here.
	#
	maxh = []
	minh = []
	medians = []
	for i in a :
		if len(maxh) == 0 :
			maxh.append(-i)
			medians.append(i)
			continue

		if len(minh) == 0 :
			if -i > maxh[0] :
				heappush(minh, -heappop(maxh))
				heappush(maxh, -i)
			else :
				minh.append(i)
			medians.append( (-maxh[0] + minh[0])/2)
			continue
			

		# i is less than max heap
		if -i >= maxh[0] :
			heappush(maxh, -i)
		elif i >= minh[0] :
			heappush (minh, i)
		else :
			heappush(maxh, -i)
		
		if len(maxh) - len(minh) > 1 :
			heappush(minh, -heappop(maxh))
		if len(minh) - len(maxh) > 1 :
			heappush(maxh, -heappop(minh))
		
		if len(maxh) > len(minh) :
			medians.append(-maxh[0])
		elif len(minh) > len(maxh) :
			medians.append(minh[0])
		else :
			medians.append ((minh[0] + -maxh[0])/2)

		print(i, maxh, minh)
	return medians

if __name__ == '__main__':

	a_count = int(input())

	a = []

	for _ in range(a_count):
		a_item = int(input())
		a.append(a_item)

	result = runningMedian(a)

	print('\n'.join(map(str, result)))
	print('\n')


