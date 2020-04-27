# Complete the reverseShuffleMerge function below.

def remdup  (s) :
	index = 0
	lis = list(s)
	l = len(s) 
	for i in range(l) :
		for j in range(0, i+1) :
			if lis[i] == lis[j] :
				break
		if i == j :
			lis[index] = lis[i]
			index +=1 
	return lis[:index]
			

def select_r_n(s,index, r, tmp, out) :
	
	if index == len(s) :
		return
	
	if r == 0 :
		out.append(tmp.copy())
		return

	i = index
	while i < len(s) - r + 1:
		tmp[len(tmp) -r] = s[i]
		select_r_n(s,i +1, r -1, tmp, out)
		i += 1


def remove(s,a) :
	s1 = s.copy()
	for e in a:
		s1.remove(e)
	return s1
		

def split(s) :
	r = len(s)//2
	out = []
	tmp = [0] * r
	select_r_n(s,0, r, tmp, out) 
	res = [] 
	added =  set()
	
	for a in out :	
		diff = remove(s,a) 
		if sorted(a) == sorted(diff) :
			stra = "".join(map(lambda x :str(x), sorted(a))	)
			if stra not in added :
				res.append(a)
				added.add(stra)

	return res

v = [1,2,3,1,2,3]
print(split(v))

			 
	
	
	

def reverseShuffleMerge(s):
	us = remdup(s)
	min_len = len(us)	
	for i in range(min_len, len(s)) :
		s1 = split(s, i )
		if s in merge(reverse(s1), shuffle(s1)) :
			return s1
