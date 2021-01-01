


def _knapsack (weights, values, maxwt, i) :

	#print ("+++", maxwt, i)

	if maxwt <= 0 or i >= len(weights):
		return 	[]

	# if current wt is greater than maxwt then it must be excluded
	if weights[i] > maxwt:
		return _knapsack(weights, values, maxwt, i + 1)

	# Case 1 : use the current item
	temp1 = _knapsack(weights, values, maxwt - weights[i], i + 1) 

	# Case 2 : do not use the current item
	temp2 = _knapsack(weights, values, maxwt, i + 1) 

	#print (temp1, temp2)

	val1 = sum(list(map(lambda x : values[x], temp1))) + values[i]

	val2 = sum(list(map( lambda x : values[x], temp2)))
	#print ("---", val1, val2)

	if val1 > val2 :
		temp1.append(i)
		return temp1
	else :
		return temp2 
	
	
	

def knapsack (weights, values, maxwt ) :
	out = _knapsack(weights, values, maxwt, 0) 

	print (out)
	for i in out :
		print("wt = %d val = %d "  % (weights[i], values[i]))



weights = [ 1,4,7,3,5]
values = [ 3,5,2,8,9]

#weights = [ 1,4]
#values = [ 3,5]
maxwt = 10

knapsack (weights, values, maxwt)
