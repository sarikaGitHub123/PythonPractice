#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    print('arrrr',ar)
    res=0
    for i in range(len(ar)):
        newArr=ar[i+1:]
        for n in newArr:
            if((ar[i]+n)%k==0):
                res+=1
                print('..',ar[i],n,k)

    print('resres',res) 
    return res           

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    
