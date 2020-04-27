import random

class TrieNode  :


	char = ''
	is_word = False

	def __init__(self, c) :
		self.char = c 
		self.id = random.randrange(10000)
		self.children = [] 

	def __str__ (self) :
		return "id = %d  char = %s is_word = %d num_children=%d" %(self.id, self.char, self.is_word, len(self.children))

	def add_child (self, c) :
		nodes = list(filter (lambda x: c == x.char, self.children))
		if len(nodes) == 0 : 
			node = TrieNode(c)
			self.children.append(node)
			#print("---1" + str(self))
			#print("---2" + str(node))
			return node
		return nodes[0]  

	def find_child (self, c) :
		out =  list(filter (lambda x: c == x.char, self.children))
		if len(out) == 0:
			return None
		else :
			return out[0]




def add_word (node, word) :
	#print("Adding: " + word + " to " + str(node))
	if len(word) == 1 :
		child = node.add_child(word[:1])	
		child.is_word = True
		#print("Added final letter:" + word[:1])
		#print(child)
		return 
		
	child = node.add_child(word[:1])	
	#print(child)
	add_word(child, word[1:]) 


def find_word (node, word):
	if len(word) == 1:
		child =  node.find_child(word[:1])  
		if child != None and child.is_word :
			return True
		return False

	child =  node.find_child(word[:1])  
	if child == None :
		return False
	else :
		return find_word(child, word[1:])

def print_trie(node, out) :
	
	if len(node.children) == 0:
		return

	for c in node.children :
		#print(c.char)
		
		if c.is_word :
			print(c)
			print ("Found : " + out + c.char)
		print_trie(c, out + c.char)
		

rootNode = TrieNode(None)

add_word(rootNode, "that")
add_word(rootNode, "dog")
add_word(rootNode, "them")
add_word(rootNode, "crazy")
add_word(rootNode, "crazy")

print_trie(rootNode, "")

print( "that: " + str(find_word(rootNode, "that")))
print( "this: " + str(find_word(rootNode, "this")))

