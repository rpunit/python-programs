def parse_input()  :
	triangle = []
	for l in open("./p067_triangle.txt").readlines() :
		print (l)
		entries = l.strip().split(" ")
		triangle.append(list(map(lambda x: int(x), entries)))
	return triangle


max_val = 0
def max_sum (tri, i, j, map_max ) :

	if i == len(tri) - 1 :
		return  tri[i][j]
	
	val = tri[i][j]	
	if map_max[i+1][j] == 0 :
		v1 = max_sum (tri, i+1, j, map_max) 
	else :
		v1 = map_max[i+1][j]  
		
	if map_max[i+1][j+1] == 0 :
		v2 = max_sum (tri, i+1, j+1, map_max) 
	else :
		v2 = map_max[i+1][j + 1]  

	print(i, j, v1, v2)
	mv = val + max (v1, v2) 
	map_max[i][j] = mv 
	return mv
	
	
def main () :
	tri = parse_input()
	mm = [ [ 0 for i in range(len(tri)) ]  for j in range (len(tri)) ]
	max_sum(tri, 0, 0, mm)
	print(mm[0][0])

main()
	
