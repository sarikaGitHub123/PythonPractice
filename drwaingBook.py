#!/bin/python3

import math
import os
import random
import re
import sys


def pageCount(n, p):
    pageList = [*range(0,n+1)]
    bookFlip=[]

    newListFront=[]
    for i in range(0,len(pageList),2):
        lst=pageList[i:i+2]
        newListFront.append(lst)

    for k in range(0,len(newListFront)):
        if p in newListFront[k]:
            bookFlip=newListFront[k]

    indexFront = newListFront.index(bookFlip)
    indexBack = (len(newListFront)-1)-indexFront


    print('newList',newListFront,indexFront,indexBack)

    if indexFront<=indexBack:
        return indexFront
    else: return indexBack    


if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print('result is',result)

    
