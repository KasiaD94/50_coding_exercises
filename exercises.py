# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:20:43 2021

@author: Kasia
"""

from random import shuffle
import array

def decorator_lowercase(function):   # defining python decorator
    def wrapper():
        func = function()
        input_lowercase = func.lower()
        return input_lowercase
    return wrapper
@decorator_lowercase    ##calling decoractor
def intro():                        #Normal function
    return 'Hello,I AM SAM'
#print(intro())

List = ['He', 'Loves', 'To', 'Code', 'In', 'Python']
shuffle(List)
#print(List)

def calculateSq(n):
    return n*n
numbers = (2, 3, 4, 5)
result = map(calculateSq, numbers)
#print(list(result))

x=array.array('d', [11.1 , 2.1 ,3.1] )
x.append(10.1)
#print(x)

x=array.array('d', [8.1, 2.4, 6.8, 1.1, 7.7, 1.2, 3.6])
#print(x.pop())
#print(x.pop(3))
x.remove(8.1)
#print(x)

l = lambda x,y : x*y
#print(l(5, 6))

import numpy as np

ar = np.array([1, 3, 2, 4, 5, 6])
#print(ar.argsort()[-3:][::-1])

a = np.array([1,2,3,4,5,6,7])
p = np.percentile(a, 25)  #Returns the 50th percentile which is also the median
#print(p)

