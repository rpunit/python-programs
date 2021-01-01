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
			print("no match", i,"".join(s[i:len(s)-i-1]))
			return False
	return True
	

# Complete the highestValuePalindrome function below.
# https://www.hackerrank.com/challenges/richie-rich/problem
def highestValuePalindrome(s, n, k):

	mid = n//2
	ndiff = 0
	for i in range (mid)  :
		if s[i] != s[n-i-1] :
			ndiff +=2

	# min k is at least half of ndiff
	if k < (ndiff+1)//2 :
		return "-1" 

	out =  list(s)
	i = 0
	if (len(s) == 1) :
		if k >0  :
			return "9"
		else :
			return s 

	while i < mid :
		print("i,k,ndiff,out", i, k, ndiff)
		#if  ndiff > 0 and k == 0 :
			#return "-1"
		if k == 0 :
			break

		sub = s[i:-i]  
		end = len(s) -i -1
		if s[i] == "9" :
			if s[end] == "9" :
				# Both are 9, move on
				pass
			else :
				# First in 9, last is not
				out[end] = "9"
				k-=1
				ndiff -=2 
		else :
			if s[end] == "9" :
				# first is not 9, last is 
				out[i] = "9"
				k-=1
				ndiff -=2 
			else :
				
				print(k, (ndiff-2)//2, (k-2))
				# Case 1 :  neither at the ends are 9, change both if possible
				if k >= 2 and (ndiff-2)//2 <= (k-2) :
					out[i] = "9"
					out[end] = "9"
					k-=2
					ndiff -=2 
				# Case 2 :  neither at the ends are 9, change 1 to another
				elif s[i] > s[end] :
					out[end] = out[i]
					k-=1
					ndiff -=2 
				elif s[i] <  s[end] :
					out[i] = out[end]
					k-=1
					ndiff -=2 
				else :
					# both are same. 
					# first is not 9, last is not 9
					# No changes
					pass


		i+=1

	# if the string is odd and k>1 then you can change it to 9
	if len(s)%2==1  and k > 0:
		out[len(s)//2] = "9"

	if isPalin(out):
		return "".join(out)

	return "-1"
		
		
		
if __name__ == '__main__':

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	s = input()	

	result = highestValuePalindrome(s, n, k)

	print(result + '\n')


