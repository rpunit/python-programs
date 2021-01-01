# 6 3 5 1 12

# 0 : [[]]
# 1 : [6], [3]
# 2 : [6,3], [3,5]
from collections import defaultdict
def riddle(arr):
	# complete this function
	stack = []
	maps = defaultdict(int) 

	for i in range(1, len(arr)+1) :
		j = i-1	
		while j >= 0 :
			win_len = i-j
			window = arr[j:i]
			if win_len in maps :
				maps[win_len] = max(maps[win_len],min(window)) 
			else :
				maps[win_len] = min(window)
			j-=1
	
		
	out = []
	for i in range(1,len(arr)+1) :
		out.append(maps[i])
	#print("--",maps, out)
	return out
		
			

if __name__ == '__main__':

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = riddle(arr)

	print(' '.join(map(str, res)))
	print('\n')


