
import math
import os
import random
import re
import sys



def pickingNumbers(a):

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print('result..',result)




# li = [4,6,5,3,3,1]
# resList=[]
# def arrDiff(no, arr):
#     n=len(arr)
#     count=0
#     for i in range(n):
#         if (arr[i]>no and arr[i]-no>1):
#             count+=1
#         elif(i<no and no-arr[i]>1):
#             count+=1
#     return count
    
# def checkDiff(arr):
#     ct=0
#     for i in range(len(arr)):
#         newArr=arr[i+1:]
#         if(arrDiff(arr[i],newArr)>0):
#             ct+=1
#     return ct      
        
        
# def isDiff(arr):
#     n=len(arr)
#     for i in range(n):
#         for k in range(i,n):
#             newArr=arr[i:k+1]
#             if(checkDiff(newArr)==0):
#                  resList.append(newArr)
#                 #  print('newArr..',newArr)
# isDiff(li)

# def get_longe_list(lst):
#     longest = lst[0] if lst else None
#     for x in lst:
#         if len(x) > len(longest):
#             longest = x
#     return longest



  

# print('resList',get_longe_list(resList))        

