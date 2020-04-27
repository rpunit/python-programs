import re
# Custom reorderFunction
def reorderFunction (l) :
   
    words = re.split("\s+", l)
    newList = []
    if len(words)> 0:
        newList.extend(words[1:])
        newList.extend(words[0])
        return " ".join(newList)
    return l

    
def lineWithInt(l) :
    tokens = re.split("\s+", l)
    for i in range(1, len(tokens)) :
        if not tokens[i].isdigit():
            return False
    return True

def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE
    listWithInt = []
    listWithWords = []
    for l in logLines :
        if lineWithInt(l) :
            listWithInt.append(l)
        else :
            listWithWords.append(l)
            
    out = sorted(listWithWords, key=reorderFunction)
    #out = sorted(listWithWords, lambda x : x.split(" ")  )
    
    out.extend(listWithInt)
    return out
    
    
    

