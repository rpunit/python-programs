#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
	#
	# Write your code here.
	#

	tank = 0
	curi = -1
	#A B C D
	queue = petrolpumps[:]
	queue2 = []
	# Add the last again 
	#A B C D A
	count = 0
	#queue.append(petrolpumps[0])
	i=0
	while curi !=  i and  count < 2*len(petrolpumps):
			
		#curPump = queue.pop(0)  
		curPump = petrolpumps[i] 
		print(curPump)
		tank += curPump[0]
		print (i, curi, curPump, tank )
		if (tank) >= curPump[1] :
			if curi == -1:
				curi = i
				#queue2.append(curPump)
			tank -= curPump[1]
		else :
			#queue.append(curPump)
			tank = 0
			curi = -1
		i = (i + 1) % len(petrolpumps)

	return curi

if __name__ == '__main__':
	n = int(input())

	petrolpumps = []

	for _ in range(n):
		petrolpumps.append(list(map(int, input().rstrip().split())))

	result = truckTour(petrolpumps)

	print(str(result) + '\n')


