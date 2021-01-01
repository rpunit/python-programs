#!/bin/python3

import math
import os
import random
import re
import sys

def isPalin (s) :
	mid = len(s)//2
	i = 0
	for i in range(mid) :
		if s[i] != s[len(s) -i -1] :
			return False
	return True
	

# Complete the highestValuePalindrome function below.
# https://www.hackerrank.com/challenges/richie-rich/problem
def recurse (s, k) :
	# Base case
	#print(s,k) 
	if   k == 0 :
		if isPalin(s) :
			return s
		else :
			return "-1"	
	if len(s) ==1 and k ==1 :
		return "9"

	nk = 0
	mid = len(s)//2
	i = 0
	while i < mid and s[i] == s[len(s) -i -1] :
		i+=1
	# Case 1 : Change both to 9
	s1 = "-1"
	if k >= 2 :
		out = list(s)
		out[i] = "9"
		out[len(s) -i -1 ] = "9"
		s1 = recurse("".join(out), k-2) 
		#print("s1", s1)
	# Case 2 : Change 1 to the other 
	out = list(s)
	if out[i] > out[len(s) -i -1 ] :
		out[len(s) -i -1 ] = out[i]
	else :
		out[i] = out[len(s) -i -1]
	s2 = recurse("".join(out), k-1) 
	#print("s2", s2)
	if s1=="-1" : 
		if s2 == "-1" :
			return "-1"
		else :
			return s2
	else :
		if s2 == "-1" :
			return s1	
		elif  s1 > s2 :
			return s1
		else :
			return s2
			
		

	
def highestValuePalindrome(s, n, k):

	return  recurse(str(s),k) 
		
if __name__ == '__main__':

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	s = input()

	result = highestValuePalindrome(s, n, k)

	print(result + '\n')


