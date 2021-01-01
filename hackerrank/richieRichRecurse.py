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
	print(s,k) 
	if len(s) == 0 :
		return  ""

	if   k == 0 :
		if isPalin(s) :
			return s
		else :
			return "-1"	

	if len(s) ==1 and k ==1 :
		return "9"

	outarr = []
	sa = list(s) 
	sub1 = None  
	sub2 = None  
	sub3 = None 
	if s[0] == "9" :
		if s[-1] == "9" :
			if sub1 == None  :
				sub1 = recurse(s[1:-1], k)
			if sub1 != "-1" :
				s1 =  s[0] + sub1  + s[-1]
				outarr.append(s1) 
		else :
			if sub2 == None  :
				sub2 = recurse(s[1:-1], k-1)
			if sub2 != "-1":
				s1 =  s[0] + sub2 + "9"
				outarr.append(s1) 
	else :
		if s[-1] == "9" :
			if sub2 == None  :
				sub2 = recurse(s[1:-1], k-1)
			if sub2 != "-1":
				s1 =  "9" + sub2  + s[-1]
				outarr.append(s1) 
		else :
			if k >= 2 :
				# Case 1 :  neither at the ends are 9, change both
				if sub3 == None  :
					sub3 = recurse(s[1:-1], k-2)
				if sub3 != "-1" :
					s1 =  "9" + sub3 + "9"
					outarr.append(s1) 
			# Case 2 :  neither at the ends are 9, change 1 to another
			if s[0] > s[-1] :
				if sub2 == None  :
					sub2 = recurse(s[1:-1], k-1)
				if sub2 != "-1" :
					s1 = s[0] + sub2 + s[0] 
					outarr.append(s1) 
			elif s[0] <  s[-1] :
				if sub2 == None  :
					sub2 = recurse(s[1:-1], k-1)
				if sub2 != "-1" :
					s1 = s[-1] + sub2 + s[-1] 
					outarr.append(s1) 
			else :
				if sub1 == None  :
					sub1 = recurse(s[1:-1], k)
				if sub1 != "-1" :
					s1 = s[0] + sub1 + s[-1] 
					outarr.append(s1) 

	print(outarr)
	if (len(outarr) > 0 ) :
		outarr =  sorted(outarr)
		return outarr[-1]
	else :
		return "-1"
	
			
			
	
			
		

	
def highestValuePalindrome(s, n, k):

	return  recurse(str(s),k) 
		
if __name__ == '__main__':

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	s = input()	

	result = highestValuePalindrome(s, n, k)

	print(result + '\n')


