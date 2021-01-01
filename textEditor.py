# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

"""
1 append - Append string  to the end of .
2 delete - Delete the last  characters of .
3 print - Print the  character of .
4 undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.
"""
num = int(sys.stdin.readline().strip())
inputs = []
for i in range(num) :
	inputs.append(sys.stdin.readline().strip().split(" "))
text = [""]*16
stack = []
prev = ()
last_deleted= ""
cur_index = 0
for i,t in enumerate(inputs) :
	#print (t, text, cur_index)
	oper = int(t[0])
	if oper == 1 :
		i = 0
		if cur_index + len(t[1]) > len(text):
			# resize 
			text.extend([""]*(len(text) + len(t[1]))*2)
		while  i <  len(t[1]) :
				text[cur_index +i ] = t[1][i]
				i+=1
		cur_index += len(t[1])
		prev = (t[0], t[1], len(t[1]))
		stack.append(prev)
	elif oper == 2:
		k = int(t[1])
		if  (k <= cur_index) :
			deleted_chars = text[cur_index-k:cur_index]
			cur_index -= k
			prev = (t[0], t[1], deleted_chars)
			stack.append(prev)
	elif oper == 3:
		k = int(t[1])-1
		if  ( k <= cur_index):
			print(text[k])
	elif oper == 4 :
		p = stack.pop(-1)
		#print ("undo", p)
		if p[0]  == "1":
			cur_index -= p[2]
		elif p[0]  == "2":
			dc = p[2]
			i = 0
			while  i <  len(dc)  :
				text[cur_index +i ] = dc[i]
				i+=1
			cur_index += len(dc)


