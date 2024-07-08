#!/bin/python3

import math
import os
import random
import re
import sys


def findSubset(k,arr):
    count=0
    for i in range(len(arr)):
        newAr=arr[i+1:]
        for n in newAr:
            if((arr[i]+n)%k==0):
                count+=1
    return count   

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)


    return findSubset(4,[l])

         

def nonDivisibleSubset(k, s):
    print('nn',permutation([19,10,12]))
    print(len(permutation(s)))

       
        


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

  
