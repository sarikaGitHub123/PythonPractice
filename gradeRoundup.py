#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    loopRange = len(grades)
    for i in range(loopRange):
        for k in range(1,3):
            if (grades[i]>37 and (grades[i]+k)%5==0):
                grades[i]=grades[i]+k
    return grades

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

