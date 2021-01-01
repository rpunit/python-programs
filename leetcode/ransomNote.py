from collections import defaultdict
class Solution:
	
	def matches(self, src, target) :
		for x in target :
			if x not in src :
				return False
			elif target[x] >  src[x] :
				return False
		return True
	
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		
		if ransomNote == None :
			if magazine == None :
				return True
			else :
				return False
		else :
			if magazine == None :
				return False
			else :
				if len(ransomNote) == 0 :
					return True
		
		
		
		rnMap = defaultdict(int)
		source = defaultdict(int)
		for x in ransomNote :
			rnMap[x] += 1
			
		for x in magazine :
			if x in rnMap :
				source[x] +=1 
				print (x, source, rnMap)
				ret =   self.matches(source, rnMap) 
				if ret :
					return ret
				
		return False

sol = Solution ()
a = "bg"
b = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print (sol.canConstruct(a, b))


