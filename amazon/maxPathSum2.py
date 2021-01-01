# Python program to find maximumpath sum between two leaves 
# of a binary tree 

INT_MIN = -2**32

# A binary tree node 
class Node: 
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
	
# Utility function to find maximum sum between any 
# two leaves. This function calculates two values: 
# 1) Maximum path sum between two leaves which are stored 
# in res 
# 2) The maximum root to leaf path sum which is returned 
# If one side of root is empty, then it returns INT_MIN 

def recurse(root): 

	if root == None :
		return 0

	v = root.data
	vr = recurse(root.right) 	
	vl = recurse(root.left) 	

	max_lr = max(vr +v , vl +v ) 
	max_top = max(max_lr,  vr+ vl + v) 

	if recurse.res < max_top:
		recurse.res = max_top

	return max_lr
		
	
	

# The main function which returns sum of the maximum 
# sum path betwee ntwo leaves. THis function mainly 
# uses maxPathSumUtil() 
def maxPathSum(root): 
		recurse.res = INT_MIN 
		recurse(root) 
		return recurse.res 


# Driver program to test above function 
root = Node(-15) 
root.left = Node(5) 
root.right = Node(6) 
root.left.left = Node(-8) 
root.left.right = Node(1) 
root.left.left.left = Node(2) 
root.left.left.right = Node(6) 
root.right.left = Node(3) 
root.right.right = Node(9) 
root.right.right.right= Node(0) 
root.right.right.right.left = Node(4) 
root.right.right.right.right = Node(-1) 
root.right.right.right.right.left = Node(10) 

print ("Max pathSum of the given binary tree is", maxPathSum(root) )

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

