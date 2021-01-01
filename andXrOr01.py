#!/bin/python3

import os
import sys
import heapq
#
# Complete the andXorOr function below.
#
def andXorOr(a):
    #
    # Write your code here.
    #
    stack = []
    stack.append(0)
    maxval = 0
    for i in range(1,len(a)):
        x = a[i]
        while (len(stack) >= 1 and stack[-1] > x) :
            stack.pop(-1)
        a1 = a[stack[-1]]
        a2 = x
        v = (((a1&a2)^(a1|a2))&(a1^a2))
        if v > maxval :
            maxval = v
        stack.append(i)
    return maxval

        

if __name__ == '__main__':

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    print(str(result) + '\n')


