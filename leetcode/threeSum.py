from collections import defaultdict

def threeSum( nums):
		out = []
		nums.sort()
		hmap = defaultdict(list)
		for i in range(len(nums)):
			hmap[nums[i]].append(i)
			
		print (nums, hmap)
		
		i = 0
		j = len(nums) -1
		while  i < j  and i < len(nums) and j > 0:
			tsum = nums[i] + nums[j]
			print(i,j, "tsum", tsum)
			if nums[i] < 0 and nums[j] > 0 :
				if tsum >= nums[i] and tsum <= nums[j] :
					if -tsum in hmap : 
						mi = list(filter(lambda x : x != i and x != j,hmap[-tsum]))
						print ("mi", mi)
						if len(mi) > 0 :
							out.append([nums[i],-tsum, nums[j]])
			if tsum < 0 :
				i+=1
			else :
				j-=1

		return out


arr = [-1,  0, 1, 2, -1, -4]
print(threeSum(arr))


