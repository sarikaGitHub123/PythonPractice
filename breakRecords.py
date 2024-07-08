#!/bin/python3

import math
import os
import random
import re
import sys



def minNumberList(array):
    minNum=array[0]
    for i in array:
        if minNum<i:
            minNum = minNum
        else:
            minNum = i
    return minNum

def maxNumberList(array):
    minNum=array[0]
    for i in array:
        if minNum>i:
            minNum = minNum
        else:
            minNum = i
    return minNum      


def breakingRecords(scores):
    minRecords=[]
    maxRecords=[]
    minBreak = []
    maxBreak = []
    # Write your code here
    scoreLength = len(scores)
    for i in range(1,scoreLength+1):
        newArray = scores[0:i]
        minRecords.append(minNumberList(newArray))
        maxRecords.append(maxNumberList(newArray))
    for j in range(1,scoreLength):
        if (maxRecords[j] not in maxBreak and maxRecords[j]!=maxRecords[0]):
            maxBreak.append(maxRecords[j])
        if minRecords[j] not in minBreak and minRecords[j]!=minRecords[0]:
            minBreak.append(minRecords[j])    
  
    a=len(minBreak)
    b=len(maxBreak)
    return b,a

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
