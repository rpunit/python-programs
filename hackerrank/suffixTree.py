
class Node : 
	def __init__ (self) :
		self.children = {} 
		self.isLeaf = False
		self.pos = 0

	def childStartsWith(self, s) :
		
		for l in self.children.keys() :
			if l.startsWith(s) :
				return l
		return None





def recurse(s, node) : 
	i = 1
	while i < len(s)  :
		suf = s[-i:]
		l = suf[0]
		if node.childStartsWith(l) == None :
			cn = Node()
			cn.pos = len(s) - i
			node.children[suf] = cn 
		else :
			suf = node.childStartsWith(l)
			recurse(suf,  node[suf) )
			
		i += 1


	root = Node
