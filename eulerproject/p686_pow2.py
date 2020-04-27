import math

## Not original work. I got this from the forums.
def engine(limit):
  log210 = math.log2(10)
  solutions = 0
  low_log = math.log2(1.23)
  high_log = math.log2(1.24)
  x = 1
  
  while solutions < limit:
    low=low_log+(x)*log210
    high=high_log+(x)*log210
    if math.floor(low)!=math.floor(high):
      print(math.floor(low), math.floor(high), x)
      solutions+=1
    x+=1

  return math.floor(high)

#print(engine(45))
print(engine(678910))
