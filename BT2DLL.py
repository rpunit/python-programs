# Python3 program to convert a given Binary  
# Tree to Doubly Linked List  
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
  
class BinaryTree: 
	root, head = None, None
	  
	# A simple recursive function to convert a given 
	# Binary tree to Doubly Linked List 
	def BToDll(self, root: Node): 
	
		if root == None :
			return  
		
		self.BToDll(root.right)

		root.right = self.head
		
		if self.head != None :
			self.head.left = root	

		self.head = root

		print (root.data) 

		self.BToDll(root.left)

		

	  
	@staticmethod
	def print_list(head: Node): 
		print('Extracted Double Linked list is:') 
		while head is not None: 
			print(head.data, end = ' ') 
			head = head.right 
  
# Driver Code 
if __name__ == '__main__': 
	  
	""" 
	Constructing below tree 
			5 
		// \\ 
		3 6 
		// \\ \\ 
		1 4 8 
	// \\ // \\ 
	0 2 7 9 
	"""
	tree = BinaryTree() 
	tree.root = Node(5) 
	tree.root.left = Node(3) 
	tree.root.right = Node(6) 
	tree.root.left.left = Node(1) 
	tree.root.left.right = Node(4) 
	tree.root.right.right = Node(8) 
	tree.root.left.left.left = Node(0) 
	tree.root.left.left.right = Node(2) 
	tree.root.right.right.left = Node(7) 
	tree.root.right.right.right = Node(9) 
  
	tree.BToDll(tree.root) 
	tree.print_list(tree.head) 
  
