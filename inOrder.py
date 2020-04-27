"""Python3 program for nth nodes of 
   inorder traversals"""
  
# A Binary Tree Node  
# Utility function to create a  
# new tree node  
class newNode:  
  
	# Constructor to create a newNode  
	def __init__(self, data):  
		self.data = data  
		self.left = None
		self.right = None
		self.visited = False
  
count = [0] 
  
""" Given a binary tree, prits nth  
	nodes of inorder"""
def NthInorder(node, n): 
	if node == None :
		return 0

	count = 0 
	if node.left != None :
		count = NthInorder (node.left, n) + 1

	print(count, n, node.data)
	if count == n: 
		print (node.data) 
	

	if node.right != None :
		count = NthInorder (node.right, n) + 1

	return count + 1


def bft (node, ) :
	queue = []
	queue.append(node) 
	while (len(queue) != 0 ) :
		n = queue.pop(0)
		if n != None :
			print (n.data)
			queue.append(n.left) 
			queue.append(n.right) 

# Driver Code 
if __name__ == '__main__': 


  
	root = newNode(10)  
	root.left = newNode(20)  
	root.right = newNode(30)  
	root.left.left = newNode(40)  
	root.left.right = newNode(50)  
  
	n = 2
  
	NthInorder(root, n) 
  
	bft(root)
