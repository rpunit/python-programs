from heapq import *
import math

def minSum(num, k):
	# Write your code here
	heap = []
	# heapq does not support maxheap. Insert -ve to simulate it
	for i in num:
		heappush(heap, -i)
	while k > 0 :
		cur = heappop(heap)
		print (cur/2)
		cur = math.floor(cur/2)
		print (cur)
		heappush(heap, cur)
		k-=1
	
	return -1 * sum(heap)


a = [ 2,3]
k = 1
print (minSum(a, k) )
