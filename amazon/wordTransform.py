from collections import defaultdict
import heapq

def readWordsOfLen(wlen) :
	with open("/usr/share/dict/words", "r") as f :
		arr = f.readlines()
		return  list(filter(lambda x: len(x) == wlen, map(lambda x : x.strip(), arr)))


"""
HEAD  -- > TAIL
TEAD


"""	

def recurse(w1,w2,index) :

	if index == len(w1)  :
		return [""] 

	prev = recurse(w1,w2, index +1) 
	out = []
	for p in prev :
		out.append(w1[index] + p)
		out.append(w2[index] + p)

	return out
		


def getDictionaryWordsFor(w1, w2) :
	wlen = len(w1)
	dictwords = readWordsOfLen(wlen)
	allwords = recurse(w1, w2, 0)	
	fwords = list(filter(lambda x : x in dictwords, allwords) )
	return fwords
			

class Graph :
	
	def __init__(self) :
		self.visited = defaultdict(bool)
		self.nodes = defaultdict(list)

	def addEdge(self, e1, e2) :
		self.nodes[e1].append(e2) 
		self.visited[e1] = False
		self.visited[e2] = False

	def _rec_bfs (self, e1, e2 , queue, out) :

		#print(queue,self.visited, out)
		if len(queue) == 0 :
			return False

		edge = queue.pop(0)
		out1 = out
		if not self.visited[edge] : # possible that the edges are same
			out1 = "" + out + "-->" + edge
		self.visited[edge]  = True
		if edge == e2 :
			print(out)
			return True
		for e in self.nodes[edge] :
			if not self.visited[e] :
				#print ("Adding " , e, self.visited)
				queue.append(e) 
		
		return self._rec_bfs(e1, e2, queue, out1)
			
		
	def rec_bfs(self, e1, e2) :

		print(self.nodes)
		queue = []
		queue.append(e1) 
		out = ""
		if self._rec_bfs (e1,e2,queue, out) :
			print (out)

	def bfs (self, e1, e2) :
		queue = []
		queue.append(e1) 
		while (len(queue)) :
			edge = queue.pop(0)
			self.visited[edge] = True
			arr[i]=edge 
			if edge == e2 :
				print ("Found")
				break
			for e in self.nodes[edge] :
				if not self.visited[e] :
					queue.append(e) 
				
		print (arr)	
		

def getWordsWithDist1(word1, words ) :
	dist1 = []
	for w  in words :
		if w == word1 :
			continue
		s = 0
		for i in range(len(w)) :
			if w[i] == word1[i] :
				s+=1
		if s == len(word1) -1:
			dist1.append(w)
		
	return dist1
			
			
	
word1 = "head"
word2 = "mole"

words = getDictionaryWordsFor(word1, word2)
print(words)

graph = Graph()

for w in words :
	dist1 = getWordsWithDist1(w, words)
	for e in dist1 :
		graph.addEdge(w, e)

graph.rec_bfs(word1, word2)

