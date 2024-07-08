# import math
# import os
# import random
# import re
# import sys



# def miniMaxSum(arr):
#     val=len(arr)
#     NewList = []
#     sumList = []
#     res = []
#     # sum=[]
#     for i in range(val):
#         NewList = (arr[i:]+arr[:i])[:val-1]
#         sumList.append(sum(NewList))
#     maxVal  = sumList[0]
#     minVal =   sumList[0]
#     length = len(sumList)
#     for j in range(length):
#         if(sumList[j]>maxVal):
#             maxVal = sumList[j]
#         if(sumList[j]<minVal):
#             minVal = sumList[j]
#     print(maxVal,minVal)        
# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)



def miniMaxSum(arr):
    range1 = len(arr)
    maxVal=arr[0]
    result = 0
    for i in range(1,range1):
        if(arr[i]>maxVal):
            maxVal=arr[i]
    for k in range(range1):        
        if(arr[k]==maxVal):
            result+=1
    print('maxval',maxVal,result)        
   
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

