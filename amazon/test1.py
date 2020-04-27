import re
def popularNToys(numToys, topToys, toys, numQuotes, quotes):
    # WRITE YOUR CODE HERE
    
    toys =map(lambda x: x.lower(), toys)
    toySet = set(toys)
    #print(toySet)
    toyMap = {}
    for toy in toys :
        toyMap[toy] = 0
        
    for quote in quotes :
        # Assume the quotes are space separated
        words = set(map(lambda x: x.lower(), re.split("\s+", quote)))
        for word in words:
            if word in toySet :
                toyMap[word] += 1
    
    # Sort by value then key            
    sortedItems = sorted(toyMap.items(), key = lambda (k,v) : (-v,k))
    
    #print(sortedItems)
    return map(lambda x: x[0], sortedItems)[:topToys]
