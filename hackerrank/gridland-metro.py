#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# https://www.hackerrank.com/challenges/gridland-metro/problem
def get_count (m, track_list ) :
	
	tl =  merge(track_list) 
	#print(tl)
	index = 0
	i = 1
	count = 0
	for track in tl :
		count += (track[1] - track[0] +1)
	return m - count


def merge(tracks) :
	if len(tracks)  < 1 :
		return tracks
		
	prev = None
	out = []
	tracks =  sorted(tracks, key=lambda x : x[0] )
	out.append(tracks[0])
	for i,t  in enumerate(tracks) :
		prev = out.pop(-1)	
		if t[0] >= prev[0] and t[0] <= prev[1] : 
			out.append([prev[0],  max(prev[1] , t[1])] )
		else :
			out.append(prev)
			out.append(t)
	return out

#tracks = [ [1,5], [2,4], [3,8], [9,11]]
#print (merge(tracks))
#exit(1)

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
	tm = defaultdict(list) 
	for t in track :
		tm[t[0]].append(t[1:])

	#print (tm)
	count = 0
	
	uniq_count = len(tm)
	count += (n - uniq_count) * m
	for t in tm :
		count += get_count(m,tm[t])

	#for i in range(1,n+1) :
		#if i not in tm:
			#count += m
		#else :
			#count += get_count(m,tm[i])
	
	return count

if __name__ == '__main__':

	nmk = input().split()

	n = int(nmk[0])

	m = int(nmk[1])

	k = int(nmk[2])

	track = []

	for _ in range(k):
		track.append(list(map(int, input().rstrip().split())))

	result = gridlandMetro(n, m, k, track)

	print(str(result) + '\n')


