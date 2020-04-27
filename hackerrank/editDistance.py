
def recurse (a, b, m, n ) :

	#print(m,n)
	if m == 0 :
		# insert all n chars
		return n

	if n == 0 :
		# delete all m chars
		return m

	# if characters match the just move to previous
	if a[m-1] == b[n-1] :
		#print("found match",a[m-1], b[n -1]) 
		return recurse(a, b,m -1,n -1)

	# if they don't match, try all three 
	ins = recurse(a, b, m, n-1) 	#insert
	rem = recurse(a, b,m -1 , n)     # remove
	rep = recurse(a, b,m -1, n -1)   # replace

	minv = min(ins,rem,rep) 

	"""
	if ins == minv :
		print("Insert " + b[n-1])
	if rem == minv :
		print("Remove " + b[n-1])
	if rep == minv :
		print("update " + b[n-1])
	"""

	return minv + 1

def editDistance (a, b) :
	return recurse(a,b,len(a), len(b))


print (editDistance("stowasdfasdfasdfasdfasdf", "showskkkkasdfkkksdfkkkk"))
