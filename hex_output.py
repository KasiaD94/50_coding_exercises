# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:23:25 2021

@author: Kasia
"""

def hex_output(hex_nr):
    dec_nr = 0
    hex_nr = list(hex_nr)
    for i, x in enumerate(hex_nr):
        if x == "A":
            hex_nr[i] = x.replace("A", "10")
        if x == "B":
            hex_nr[i] = x.replace("B", "11")
        if x == "C":
            hex_nr[i] = x.replace("C", "12")
        if x == "D":
            hex_nr[i] = x.replace("D", "13")
        if x == "E":
            hex_nr[i] = x.replace("E", "14")
        if x == "F":
             hex_nr[i] = x.replace("F", "15")
        
    j = len(hex_nr) - 1

    for i in hex_nr:
        dec_nr = dec_nr + int(i) * 16**j
        j = j - 1 
            
    return dec_nr

print(hex_output("400"))

def hex_output_v2():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
         decnum += int(digit, 16) * (16 ** power)
    print(decnum)
 
hex_output_v2()
