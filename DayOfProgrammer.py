#!/bin/python3

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    res=0
    dateString=''
    monthsDays=[31,31,30,31,30,31,31,30,31,30,31]
   
    if(year>=1700 and year<=1917):
        print('this is the year')
        if(year%4==0):
            feb=29
            monthsDays.insert(1,29)
        else:
            monthsDays.insert(1,28)
    if(year>=1919 and year<=2700):
        if(year%400==0 or (year%4==0 and year%100!=0)):
             monthsDays.insert(1,29)
             print('this leap year')
        else:
             monthsDays.insert(1,28)
    if(year==1918):
             monthsDays.insert(1,15)

    for i in range (len(monthsDays)):
            print('res+i..',res+monthsDays[i], i)
            res = res+monthsDays[i]
            print('res',res)
            if(res>=256):
                no=res-monthsDays[i]
                date = str(256-no)
                month=str(i+1)
                datestr='0'+date if len(date)==1 else date
                monthstr='0'+month if len(month)==1 else month
                dateString= datestr + '.' + monthstr+ '.'+str(year)
                print('monthNumber',res,res-monthsDays[i],'answers...',dateString,)
                break
    print('dateString',dateString)
    return dateString           
   
if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print('result...',result)
