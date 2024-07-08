
import os
import sys


def getMoneySpent(keyboards, drives, b):

    sumList = []
    for k in keyboards:
        for j in drives:
            if((k+j)<=b):
              sumList.append(k+j)
    res = -1 if len(sumList)==0 else sumList[0]
    if (len(sumList)>0):         
        for i in sumList:
            if i>res:
                res=i
    return res
    # print('total sum is',sumList,res)      

     
if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

 
    moneySpent = getMoneySpent(keyboards, drives, b)
    print('moneySpent',moneySpent)

    
