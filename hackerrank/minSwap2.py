# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	count = 0
	i=0

	while i < len(arr) :	
		print(i, arr[i], arr)
		if  arr[i] == i+1 :
			i+=1
			continue
		if arr[i] != i+1 :
			a = arr[i]
			arr[a-1], arr[i] = arr[i], arr[a-1]
			count +=1
	return count

arr = [ 4,3,1,2]
#arr = [ 1,3,5,2,4,6,7] 
#arr = "2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19".split(" ")
#arr=list(map(lambda x : int(x), arr))
print(minimumSwaps(arr))
