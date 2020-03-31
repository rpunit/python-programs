import os,sys



pmap = { 1:['1'], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y' 'z'], 0: ['0'] } 


def print_pnos (pmap, arr, index, out) :
	if index == len(arr) :
		print ("".join(out))	
		return 

	for c in pmap[arr[index]] :
		out[index] = c
		print_pnos(pmap, arr, index + 1, out)


arr = [int(c) for c in "5712254746"]
print_pnos(pmap, arr, 0, ['']*len(arr) )
