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

	jobs.sort(key=lambda x : x.start) 
	max_cpu = 0
	cpu = 0 
	for i in range (len(jobs)) :		
		cur = jobs[i] 
		# remove all the events that have ended
		while (len(hq) > 0 and hq[0].end <  cur.start) :
			v = hq.pop(0) 		
			cpu -= v.cpu_load
	
		heappush(hq, cur) 
		cpu += cur.cpu_load
		if cpu >= max_cpu:
			max_cpu = cpu
			
		
	return max_cpu			
		

# Driver Code 
if __name__ == "__main__": 
	jobs = [job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)] 
						   
	print("Maximum CPU load at any time: " + str(find_max_cpu_load(jobs))) 
