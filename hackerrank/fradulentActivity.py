#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import bisect

def countSort (arr, maxv ) :
	count = [0]*maxv

	# Step 1 get the counts :
	for a in arr :
		count[a] +=1

	# step 2, get the cummulative counts
	for i in range(1,len(count)) :
		count[i] += count[i-1]

	out = [0]*len(arr)
	# step 3
	for i in range(len(arr)) :
		out[ count[arr[i]] -1] = arr[i]
		count[arr[i]] -= 1

	return out

def getMedian(arr) :
	#arr=countSort(arr, 200)
	#arr=sorted(arr)
	if len(arr) % 2 == 1:
		return arr[len(arr)//2]
	else :
		return (arr[len(arr)//2-1] + arr[len(arr)//2])/2

def insert (arr, x) :
	i = 0
	while i <  len(arr)  and x > arr[i] :
		i+=1
	arr.insert(i, x)
	return arr
		
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
	if len(expenditure) < d+1 :
		return 0
	deq  = deque(expenditure[:d])
	s_arr = sorted(expenditure[:d])
	
	count = 0
	for i in range(d,len(expenditure)) :
		median = getMedian(s_arr) 
		#print (i, expenditure[i], median)
		if expenditure[i] >= median*2 :
			count+=1
		delx = deq.popleft()
		deq.append(expenditure[i])
		index = bisect.bisect_left(s_arr, delx)	
		#print(delx, index, len(s_arr), s_arr[len(s_arr)-5:])
		s_arr.pop(index)
		bisect.insort_left(s_arr, expenditure[i])
		
	return count


if __name__ == '__main__':
	nd = input().split()

	n = int(nd[0])

	d = int(nd[1])

	expenditure = list(map(int, input().rstrip().split()))

	result = activityNotifications(expenditure, d)

	print(str(result) + '\n')


