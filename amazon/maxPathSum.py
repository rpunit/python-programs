import sys
# Python program to find maximum path sum in Binary Tree 

# A Binary Tree Node 
class Node: 
	
	# Contructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


def recurse(node) :
	if node == None :
		return 0

	v = node.data
	vr = recurse(node.right)
	vl = recurse(node.left)

	max_l_r = max(v, v+vr, v+vl)

	max_top = max(max_l_r, v + vr +vl)
	if recurse.maxsum < max_top :
		recurse.maxsum = max_top
	
	return max_l_r 

def findMaxSum(node) :
	recurse.maxsum = -sys.maxsize
	recurse(node)
	return recurse.maxsum
	

# Driver program 
root = Node(10) 
root.left = Node(2) 
root.right = Node(10); 
root.left.left = Node(20); 
root.left.right = Node(1); 
root.right.right = Node(-25); 
root.right.right.left = Node(3); 
root.right.right.right = Node(4); 
print ("Max path sum is " ,findMaxSum(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

