# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:20:11 2021

@author: Kasia
"""
"""The challenge here is to write a mysum function 
that does the same thing as the built-in sum function. 
However, instead of taking a single sequence as a parameter, 
it should take a variable number of arguments. 
Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3)
or mysum(10,20,30,40,50)."""

def mysum(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum

print(mysum(5,10,15,20))
