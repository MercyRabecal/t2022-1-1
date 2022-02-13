# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:40:49 2021

@author: user
"""
"""problem 1
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
"""
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    # Function to subtract two numbers 
    def subtract(self):
        return self.a - self.b
    # Function to multiply two numbers
    def multiply(self):
        return self.a * self.b
    # Function to divide two numbers
    def divide(self):
        return self.a / self.b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
obj=cal(a,b)
while True:
    select = str(input("Select operations form\n+  Add\n-  Subtract\n*  Multiply\n/  Divide\n"))
    if select == "+":
        print("Result of addition is:",obj.add())
        break
    elif select == "-":
        print("Result of subtraction is:",obj.subtract())
        break
    elif select == "*":
        print("Result of multiplication is:",obj.multiply())
        break
    elif select == "/":
        print("Result of division is:",obj.divide())
        break
    else:
        print("Invalid input")
        break
