#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def listIsSorted (l) :
	if len(l) <= 1 :
		return True
	for i in range(1, len(l)) :
		if l[i] > l[i-1]:
			return False
	return True

def poisonousPlants(p):

	pqueue = p.copy()
	queue = p.copy()
	nDays = 0
	while not listIsSorted(pqueue) :
		nDays +=1
		print (pqueue)
		queue = []
		prev = None
		while len(pqueue) > 0:
			cur = pqueue.pop(0)
			if prev != None :
				#print ("Comparing ", cur, prev)
				if cur <= prev :
					queue.append(cur)
			else :
				queue.append(cur)

			prev = cur
		pqueue = queue
		#print ("---", pqueue)

	return nDays


if __name__ == '__main__':

	n = int(input())

	p = list(map(int, input().rstrip().split()))

	result = poisonousPlants(p)

	print(str(result) + '\n')


