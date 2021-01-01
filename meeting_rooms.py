# driver code 


def findMeetingRooms(arr, dep, n) :
	max_count = 0
	count = 1
	arr.sort()
	dep.sort()
	i = 1
	j = 0
	while (i < n and j < n ) :

		# if arr[i] is less then its the next event in sorted order
		if arr[i] <= dep[j] :
			count += 1 
			i += 1
		# if dep[j] is less then its the next event in sorted order
		elif arr[i] > dep[j] :
			count -= 1
			j += 1


		if count > max_count :
			max_count = count

	return max_count
		
  
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
  
print("Minimum Number of Platforms Required = ", 
        findMeetingRooms(arr, dep, n)) 
