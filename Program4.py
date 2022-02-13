# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:07:17 2021

@author: user
"""
"""
problem-4: Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
"""
a = [int(i) for i in input("Enter the elements").split()]
b = {}
count = 0
for i in range(1, 10):
    for j in a:
        if j % i == 0:
            count+=1
    b[i] = count
    count = 0
print(b)