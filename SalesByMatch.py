#!/bin/python3

import math
import os
import random
import re
import sys



def findCount(e,arr):
    count = 0
    for k in arr:
        if e==k:
            count+=1
    return count        

def sockMerchant(n, ar):
    print('arr is',ar, findCount(2,ar),13%2)
    newAr = []
    res=0
    for k in ar:
        if k not in newAr:
            newAr.append(k)
    for n in newAr:
        ct=findCount(n,ar)
        if(ct>1):
            print('ct',ct//2,n)
            res+=ct//2


    print('new result',res)           
        


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print('result..',result)

