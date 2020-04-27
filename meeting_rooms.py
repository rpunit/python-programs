# driver code 


def findMeetingRooms(arr, dep, n) :
	max_count = 0
	count = 1
	i = 1
	j = 0
	while ( i < n and  j < n ) :
		
		while dep[j] < arr[i]  :
			count -= 1
			j += 1

		count += 1
		print("i,arr[i],j,arr[j],count ",i,arr[i],j,dep[j],count ) 
		if count > max_count :
			max_count = count
		i += 1

	return max_count
		
		
	
	

  
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
  
print("Minimum Number of Platforms Required = ", 
        findMeetingRooms(arr, dep, n)) 
