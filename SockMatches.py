import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    countOfSocks = [0]*100
    
    #Get a count of each color of socks
    for sock in range(len(ar)):
        print(ar[sock])
        countOfSocks[ar[sock]] += 1
    
    numOfMatches = 0
    #Calculate the number of matches found
    for i in range(len(countOfSocks)):
        numOfMatches += countOfSocks[i] // 2
        
    return numOfMatches

print(sockMerchant(100,[2,1,1,2,1,2,1,99,98]))