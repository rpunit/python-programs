# Node structure 
class Node: 
  
	# Utility function to create new node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
  
# Returns True if trees with roots as root1 and root 2  
# are mirror 
def isMirror(root1, root2) :
	if root1==None and root2 == None:
		return True

	if root1.key == root2.key :
		return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

	return False

def isSymmetric(root): 
  
	# Check if tree is mirror of itself 
	return isMirror(root, root) 
  
# Driver Program  
# Let's construct the tree show in the above figure 
root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 
print ("1") if isSymmetric(root) == True else "0" 
