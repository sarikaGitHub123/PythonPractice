import math
import os
import random
import re
import sys


def countArr(i,arr):
    sum=0
    for k in arr:
        if i==k:
            sum+=1
    return [i,sum]     

def migratoryBirds(arr):
    print('arrrrr',arr)
    length = len(arr)
    count=[]
    newList= []
    dt = []
    res = 0
    maximum=0

    for i in arr:
        if i not in newList:
            newList.append(i)
    for j in newList:
           count.append(countArr(j,arr))
     
    if len(count)>0:
        maximum=count[0][1]

    for k in range(1,len(count)):
        if(maximum<count[k][1]):
            maximum=count[k][1]
    
    for n in count:
        if n[1]==maximum:
            dt.append(n)
            print('count',n)

    print('dtt',dt,maximum)

    for n in range(len(dt)):
        if(dt[0][0]>dt[n][0]):
            res=dt[n]
        else:
            res=dt[0][0]  
        
    print('count',count,res,len(arr))
    return res 


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

  