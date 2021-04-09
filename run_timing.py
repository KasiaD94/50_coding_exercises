# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:07:37 2021

@author: Kasia
"""

"""Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, 
until the user presses Enter. At that point, the function exits--
but only after calculating and displaying the average time that 
the 10 km runs took."""

def run_timing():
    time_sum = 0
    count = 0
    while True:
        user_input = input("How long have you run today? ")
        if user_input == "":
            break
        if user_input.replace('.','',1).isdigit():
            time_sum = time_sum + float(user_input)
            count = count + 1
        else: print("It's no valid number")
        
    return f"Average time: {time_sum/count} over {count} runs"

print(run_timing())
