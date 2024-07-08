#!/bin/python3

import math
import os
import random
import re
import sys

#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    reachedAppleDis = []
    reachedOrangeDis = []
    for i in apples:
        i=i+a
        if(i>=s and i<=t):
            reachedAppleDis.append(i)
    for i in oranges:
        i=i+b
        if(i>=s and i<=t):
            reachedOrangeDis.append(i)
    print('reachedAppleDis',reachedAppleDis)
    print('reachedOrangeDis',reachedOrangeDis)
    print('reachedAppleDis',len(reachedAppleDis),'\n',len(reachedOrangeDis))
    print('reachedOrangeDis',len(reachedOrangeDis))

 
    # for k in newAppleRange:
    #     if k>=s and k<=t:
    #         print('k',k)
    # for j in newOrangeRange:
    #     if j>=s and j<=t:
    #         print('k',j)        
        



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
