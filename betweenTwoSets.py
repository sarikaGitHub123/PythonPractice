import math
import os
import random
import re
import sys


def getTotalX(a, b):
    numbers = []
    maxValueInFirstArray = a[0]
    minValueInSecArray = b[0]
    removingNumbers=[]
    prevresult = []
    result = []

    for i in a:
        if i>maxValueInFirstArray:
            maxValueInFirstArray=i
    for j in b:
        if j<minValueInSecArray:
            minValueInSecArray=j 

    My_list = [*range(maxValueInFirstArray,minValueInSecArray+1)] 

    

    for n in range (maxValueInFirstArray,minValueInSecArray+1):
        for k in a:
            if(n%k!=0 and n not in numbers):
                numbers.append(n)
                
    prevresult = [i for i in My_list if i not in numbers]
      
    for elements in b:
        for number in prevresult:
            if(elements%number!=0 and number not in removingNumbers):
                removingNumbers.append(number)

    result = [i for i in prevresult if i not in removingNumbers]
    print('numbers..',result1,result)            
    
  
    return len(numbers)            

    # for no in numbers:



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    


    