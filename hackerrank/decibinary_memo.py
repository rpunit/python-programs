import math


def get_decib (temp) :
	s = 0
	l = len(temp)
	for i in range(l) :
		s =s *10 + temp[l -i -1]
	return s

def recurse (n, index, decib, temp):

	if n == 0 :
		decib.append(get_decib(temp))	
		return

	if 2**index > n :
		return
		
	for i in range(10) :
		v = 2**index * i
		if v <= n :
			temp[index] = i
			#print("n,v,index,temp,i", n,v,index,temp, i)
			recurse (n-v, index + 1 , decib, temp)
			temp[index] =0
		
	

def decib_of (n) :
	decib = []
	temp = [0] * (int(math.log(n,2) ) + 1)
	recurse(n,0, decib, temp)
	decib = sorted(decib)
	return decib


dcb_table = [0,1,2, 10]
dec_table = [0,1,2,2]
def decibinaryNumbers(x):
	x = x -1 # assumes 1 based index 
	if x < len(dcb_table):
		return dcb_table[x]

	dec = dec_table[len(dec_table)-1]
	count = len(dcb_table) 
	while count < x + 1 :
		dec += 1
		decib_arr = decib_of(dec)
		dcb_table.extend(decib_arr)
		dec_table.extend([dec]*len(decib_arr))
		count += 1

	return dcb_table[x]

print(decibinaryNumbers (2000))
