import functools
#Item class to hold the values
class item:
  
  def __init__ (self, name, time, payout) :
    self.name = name
    self.time = time
    self.payout = payout

  def __str__ (self ) :
    return "(%s,%d,%d)" % (self.name, self.time, self.payout)
    

items = []
lines = "Pac-man,80,400|Mortal Kombat,10,30|Super Tetris,25,100|Pump it Up,10,40|Street Fighter II,90,450|Speed Racer,10,40".split("|")


def print_sack(sack) :
  for s in sack:
    print(s)

for i in range(0, len(lines)) :
  (name, time, payout) = lines[i].split(",")
  items.append(item(name, int(time), int(payout)))
  
#This is classic knapsack algorithm

def knapsack (items, rem_time, index) :
  print(rem_time, index)
  if index >= len(items)  or rem_time <= 0:
    return []
  
  # if the time of current time is > rem_time, it cannot 
  # be included, exclude it
  if items[index].time > rem_time :
    return knapsack(items, rem_time, index+11)

  # Include the rlen - 1 item
  sack1 = knapsack(items, rem_time - items[index].time, index+1)

  # Do not Include the rlen - 1 item
  sack2 = knapsack(items, rem_time, index+1 )

  print(items[index])
  #print("Sack1")
  #print_sack(sack1)
  #print("Sack2")
  #print_sack(sack2)
  n1 = items[index].payout + functools.reduce(lambda x,y: x + y.payout, sack1, 0)
  n2 = functools.reduce(lambda x,y: x + y.payout, sack2, 0)

  print("n1=%d, n2=%d" % (n1,n2))
  
  if n1 >= n2 :
    sack1.append(items[index])
    return sack1
  else :
    return sack2
  
  
games = knapsack(items, 120, 0)

for g in sorted(map(lambda x:x.name, games)):
  print (g)
