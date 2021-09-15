#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Ahmed Shaaban
Date   : Sep 13, 2021
Purpose: demonstrating if condition 
"""

x=4
if (x>0):
    print("x is larger than zero")

#%%
# on blocks 
# if block statment "must" be indented.
decision = True

if (decision == False):
    print("We are using Python")
    print("We still inside the if block")
print("Hi, I am outside the if condition") # this is the only one that should appear


#%% Quick if 
mydecision=True
if mydecision :
    print("yes we are true")

#%% alternative quick if
if True:
    print("yes this is true")
    
#%% if and else if 
x = 0
if (x > 0):
    print("x is positive")
elif (x < 0):
    print("x is negative")
else:
    print("neither positive nor negative")

#%% tip on elif 
# what is wrong with the following if statement. 
x= 91
if (x > 100):
    print("x is larger than 100")
elif (x > 90):
    print("x is larger than 90")
elif (x >80):
    print("x is larger than 80")
elif (x >70):
    print("x is larger than 70")
else:
    print("x is unknown")

# if the if statment is not mutually exclusive, only the first true statment will be exectuted. 
#%% The first solution to the the not mutually exclusive statement
x= 91
if (x > 100):
    print("x is larger than 100")
    
if (x > 90):
    print("x is larger than 90")
    
if (x >80):
    print("x is larger than 80")
    
if (x >70):
    print("x is larger than 70")
#%% The second solution to the the not mutually exclusive statement
x= 81
if (x > 100):
    print("x is larger than 100")
elif (x>90 and  x<= 100):
    print("x is larger than 90 and less than or equal 100")
elif (x>80 and x<= 90):
    print("x is larger than 80 and less than or equal 90")
elif (x>70 and x<=80):
    print("x is larger than 70 and less than or equal 80")
else:
    print("x is unknown")
#%% to understand what is happening
print(x>80 and x<=90)

#%% nested if condition
x=-1.
if (isinstance(x, int)):
    if (x < 0):
        print("x is int less than 0")
        
#%% another way 
x=1
if (isinstance(x, int) and x < 0):
    print("x is int less than 0")