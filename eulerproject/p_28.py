

x = 1001 
arr = [ [0 for i in range(x) ] for j in range(x) ]

i=x//2
j=x//2
state = 'right'
delta = 1
turn = 2 

for a in range (1, x*x + 1) :

	#print(a,i,j,turn,delta,state)
	arr[i][j] = a

	# Check if time to turn
	if a == turn :
		if state == 'right' :
			state = 'down'
			turn = a + delta

		elif state == 'down' :
			state = 'left'
			delta = delta  + 1
			turn = a + delta

		elif state == 'left' :
			state = 'up'
			turn = a + delta

		elif state == 'up' :
			state = 'right'
			delta = delta + 1
			turn = a + delta


	if state == 'right' :
		j = j + 1 

	if state ==  'down' :
		i = i + 1 

	if state ==  'left' :
		j = j - 1 

	if state ==  'up' :
		i = i - 1 
	

	
#for i in range (x) :
	#print(arr[i])

sum = 0
for i in range(x) :
	sum += arr[i][i] + arr[i][x-i-1]
	
print(sum)
