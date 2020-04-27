from heapq import * 
  
# Blueprint of the job 
class job: 
	  
	# Constructor of the Job 
	def __init__(self, start, end, cpu_load): 
		self.start = start 
		self.end = end 
		self.cpu_load = cpu_load 
	  
	# Operator overloading for the 
	# Object that is Job 
	def __lt__(self, other): 
  
		# min heap based on job.end 
		return self.end < other.end 

def find_max_cpu_load (jobs ) :
	
	hq = []
	if len(jobs) == 0 :
		return -1 

	heappush(hq,jobs[0])
	max_cpu = 0
	cpu = hq[0].cpu_load
	for i in range (1, len(jobs)) :		
		prev = hq[0]
		cur = jobs[i] 
		if prev.end > cur.start :
			heappush(hq, jobs[i]) 
			cpu += cur.cpu_load
			if cpu >= max_cpu:
				max_cpu = cpu
		else :
			v = hq.pop(0) 		
			while (v.end < cur.start) :
				cpu -= v.cpu_load
				if len(hq) <= 0 :
					break	
				v = hq.pop(0) 		
				
		
	return max_cpu			
		

# Driver Code 
if __name__ == "__main__": 
	jobs = [job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)] 
						   
	print("Maximum CPU load at any time: " + str(find_max_cpu_load(jobs))) 
