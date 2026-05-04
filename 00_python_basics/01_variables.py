import random
from unittest import result

def max_min(mlist):
    minimum = mlist[0]
    for num in mlist:
        if num < minimum:
            minimum = num
    #print(f"Minimum: {minimum}")
    return minimum

def getvalues():
    mlist = random.sample(range(1,30),5)
    print(mlist)
    result = max_min(mlist)
    print(result)


getvalues()