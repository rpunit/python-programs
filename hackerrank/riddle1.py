# 6 3 5 1 12
# 0 : [[]]
# 1 : [6], [3]
# 2 : [6,3], [3,5]
from collections import defaultdict
def riddle(arr):
	# complete this function
	stack = []
	for i,a in enumerate(arr) :
		j = len(stack) -1 
		stack2 = []
		while j >= len(stack) - i  :
			v = stack[j]
			#print ("i =%d,j =%d,a =%d, v=%s, queue=%s, stack=%s" % (i,j,a, v, stack2, stack))
			v1 = v.copy()
			v1.append(a)
			stack2.append(v1)
			j-=1 
		stack2.append([a])

		#print ("stack2", stack2)
		while len(stack2) > 0 :
			stack.append(stack2.pop(-1))

	#print(stack)
	maps = defaultdict(list) 
	for i in range(len(stack)) : 
		#print (stack[i])
		maps[len(stack[i])].append(stack[i])
		
	#print(maps)
	out = []
	for i in range(1,len(maps)+1) :
		out.append( max(list(map(lambda x : min(x), maps[i]))))
		
			
	return out

if __name__ == '__main__':

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = riddle(arr)

	print(' '.join(map(str, res)))
	print('\n')


