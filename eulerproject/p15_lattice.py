#https://projecteuler.net/problem=15


def lattice(start, end, x, y) :

	if start == x  or end == y  :
		return 1
	s1 = 0
	s2 = 0
	if m[start + 1][end] != -1 :
		s1 = m[start + 1][end]
	else :
		s1 = lattice( start + 1, end, x , y)
		m[start + 1][end] = s1
		
	if m[start][end + 1] != -1 :
		s2 = m[start][end + 1]
	else :
		s2 = lattice( start, end + 1, x , y)
		m[start][end + 1] = s2

	return s1 + s2  


x = 20
y = 20
m =  [ [ -1  for i in range(x+1)]  for j in range(y+1)]
print (lattice(0,0, x, y))


