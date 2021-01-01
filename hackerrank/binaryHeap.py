class binaryHeap  :

	def __init__ (self , maxh=True) :
		self.maxs = 16
		self.maxheap = maxh
		self.n = 0 
		self.arr = [0]*self.maxs
		self.arr[0] = None

	def resizeup (self ) : 
		if self.n >= self.maxs :
			self.maxs *= 2 
			temp = [0]*self.maxs
			for i in range(n) :
				temp[i] = self.arr[i]
			self.arr = temp

	def resizedn (self ) : 
		if self.n < self.maxs//4 :
			self.maxs = self.maxs//2
			self.arr = self.arr[:self.maxs]

	def getMaxChild(self, index) :
		ci1 = index*2
		ci2 = index*2 + 1
		if self.arr[ci1] > self.arr[ci2] :
			return ci1
		else :
			return ci2
			

	def sink(self) :
		curi = 1
		min_child = min (self.arr[curi*2], self.arr[curi*2+1])
		comp = self.arr[curi] <  min_child and self.maxs
		while comp and curi <= self.n :
			maxi = self.getMaxChild(curi)	
			self.arr[curi],self.arr[maxi] = self.arr[maxi], self.arr[curi]	
			curi=maxi
			comp = self.arr[curi] <  min_child and self.maxs
			

		
		

	def swim (self) :
		curi = self.n
		parent = self.n//2 

		if curi <= 1:
			return
		comp = self.arr[curi] > self.arr[parent] and self.maxs
		while comp and parent >= 1 :  
			print ("curi,parent", curi, parent, self.arr[curi],self.arr[parent] )
			self.arr[curi],self.arr[parent] = self.arr[parent], self.arr[curi]	
			curi = parent
			parent = curi//2 
			if parent < 1 :
				break
			comp = self.arr[curi] >  self.arr[parent] and self.maxheap
		
		
	
	def put (self, v) :
		# we start the index at 1
		self.resizeup()
		self.n+=1 
		self.arr[self.n] = v
		print (self.n, self.arr)
		self.swim()


	def delMinOrMax(self ) :
		ret = None
		if self.n >= 1:
			ret = self.arr[1]
			self.arr[1] = self.arr[self.n]
			self.arr[self.n] = 0
			self.n-=1
			self.sink()
		self.resizedn()
		return ret	

	def get(self) :
		ret = None
		if self.n >= 1:
			return self.arr[1]
		return ret

	def print(self) :
		print("n=%d, arr=%s" %(self.n, self.arr))


if __name__ == "__main__":
	heap = binaryHeap ()	

	heap.put(7)
	heap.put(6)
	heap.put(10)
	heap.put(5)
	print (heap.get()) 
	heap.put(11)
	heap.put(23)
	heap.put(3)
	print (heap.delMinOrMax()) 
	heap.print()
	print (heap.delMinOrMax()) 
	heap.print()
	print (heap.delMinOrMax()) 
	heap.print()

	
		
		
	

