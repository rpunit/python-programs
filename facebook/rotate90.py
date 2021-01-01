import sys



def swapRows (mat) :
	nRows = len(mat) 
	nCols = len(mat[0])
	for i in range(nRows) :
		for j in range(nCols) :
			mat[i][j], mat[nRows-1-i][j] = mat[i][j], mat[nRows-1-i][j]
			
		


def transpose(mat) :
	for i in range(len(mat)) :
		for j in range(i, len(mat[i])) :
			if i != j :
				mat[i][j], mat[j][i] = mat[j][i], mat[i][j]



def rotate90 (mat) :
	transpose(mat)
	swapRows(mat)

def printMat(mat) :
	for i in range(len(mat)) :
		for j in range(len(mat[0])) :
			print (mat[i][j], end=" ")	
		print ("")	
	


mat = [ [ 1, 2, 3 ],\
		[4,5,6],\
		[7,8,9]]


printMat(mat)
print ("--")

rotate90(mat)

printMat(mat)


