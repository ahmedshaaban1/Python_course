#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Ahmed Shaaban
Date     : Sep 1, 2021
purpose  :
"""

#%% operators : 

print(2+3)
print(2-3)
print(4/2)
print(4*2)
print(4**2)

#%% operators precedence of +,-,*,/

# What the following print yields different outputs?
print(5*3+2)
print(5*(3+2))

# state your conclusion : 
#  
#  without brackets, 
# multiplication ............... addition and subtraction.
# 


#%% the same also happen to happen for minus and division
print(10./5.+2)
print(10./(5.+2))

# state your conclusion : 
#  
#  without brackets, 
#  division ............... addition and subtraction.
# 

#%% logical (boolen) operator truth table 

# and truth table
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#%% nice print, but what is wrong with following : 

print('True and True equal'+True and False)
print('True and False equal'+True and False)
print('False and True equal'+False and False)
print('False and False equal'+False and False)

#%% Print the truth table for OR





#%% miscellaneous

# what is wrong with this statement: 
print(true and true) 
print(true and false)

#%% negation 

print(not True)
print(not False)

#%% what is wrong with these

print (Not True)
print (Not False)
#%%  Operator precedence

print(True or True and False)
print((True or True) and False)

# so "and" is evaluated          "or"
# see this table for operators precedence 
# https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html


#%% comparison 

print(3 > 2)
print(5 == 5)
print( 5 != 1)

#%%  how this is evalueted : recall truth table for and
print( 3>2 and 4>2)
print( 3<2 and 4>2)

#%% bitwise operator 

print(1 & 2)
print(bin(1))
print(bin(2))

#%% 
print(2 & 2)
print(bin(2))
print(bin(2))


#%% operator in 
print(4 in [1,4,9])
print(4 in [3,6,10])

#%% swap operators
# replace a with b and b with a.
a=2
b=4



tmp = a
a   = b
b   = tmp
print(a,b)


#%% dvision , truncated division, modulus

# dvision  (python3)  
# see in python 2.7
print('5/2 =  '+str(5/2))
print('5./2=  '+str(5./2))
print('5/2.=  '+str(5/2.))
#%%
# truncated division 
print('5//2=  '+str(5//2))

#%%
# modulus : finds the remainder from dividing the two numbers you specify.
print('5 %2= '+ str(5%2))

#%% is that even or odd : 
# find if 4 is even or odd 


# find if 9 is odd

#%% operator overloading
# https://www.programiz.com/python-programming/operator-overloading
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

#%% operatoros on string : note the operator overloading
# concatenation 
print("hello"+"world")
# repeation 
print("abc"*3)
