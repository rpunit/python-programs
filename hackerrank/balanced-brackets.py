#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
# Complete the isBalanced function below.
def getMatching (s) :
	if s == ")" :
		return "("
	if s == "}" :
		return "{"
	if s == "]" :
		return "["

def isBalanced(s):
	stack = []
	for i in range(len(s)) :
		if s[i] in ("(","{","["):
			stack.append(s[i])
		if s[i] in (")","}", "]"):
			if len(stack) > 0 :
				if stack[-1] != getMatching(s[i] )  :
					return "NO"
				else :
					stack.pop(-1)
			else :
				return "NO"
	if len(stack) == 0 :
		return "YES"
	return "NO"

if __name__ == '__main__':

	t = int(input())

	for t_itr in range(t):
		s = input()

		result = isBalanced(s)

		print(result)


