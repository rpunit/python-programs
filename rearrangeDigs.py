import functools

def comparator(a, b): 
    ab = str(a) + str(b) 
    ba = str(b) + str(a) 
    return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 

	
def rearr (digits) :

	ls = map (lambda x : str(x), digits)
	return sorted(ls, key=functools.cmp_to_key(comparator) , reverse=False ) 


print(rearr ([3,30,34,5,9]))

	
