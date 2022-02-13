# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:11:13 2021

@author: user
"""
"""
Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
"""
m = int(input("Enter the number\n"))
n = 1
for i in range(m):
    print(n, end=" ")
    n += 2