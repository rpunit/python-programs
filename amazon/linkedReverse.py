



class Node :
	def __init__ (self, v) :
		self.val = v
		self.next = None

head = None
prev = None
for i in range (1,10) :
	node = Node(i)
	if head == None:
		head = node
	if prev != None:
		prev.next = node
	prev = node


def printLL(head) :
	
	cur = head
	while cur != None :
		print (cur.val)
		cur = cur.next

def reverseLLRec(node) :
	if node.next == None :
		return (node, node)

	head,nxt = reverseLLRec(node.next)
	nxt.next = node	
	return head,node


def reverseLLRec1 (node ) :
	if node == None:
		return None
	if node.next == None :
		return node

	prev = reverseLLRec1(node.next)	
	node.next.next = node
	node.next = None 
	return prev
		

def reverseLL(head) :
	prev = None
	cur = head	
	nxt = None

	while cur :
		nxt = cur.next
		cur.next = prev
		prev = cur
		cur = nxt

	return prev

#printLL(reverseLL(head))
#h, node = reverseLLRec1(head)
#node.next = None

h = reverseLLRec1(head)
printLL(h)
	
