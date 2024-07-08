#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2 42 3 94 2 Yes
#  4. INTEGER v2  26 6 47 3 No
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    a=x1+v1
    b=x2+v2
    con1 = a>b and a%b==0
    con2 = b>a and b%a==0
    con3 = x1<x2 and v1>v2
    con4 = x2<x1 and v2>v1
    for i in range(2,11):
        n=a%i 
        k=b%i
        if(a!=b  and n==k):
          print('n,k',n,k,'and',i)
    print('a,b',a,b, b%a, a%b)
  

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)

