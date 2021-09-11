#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name :  Ahmed Shaaban
Date :  Aug 25, 2021
Purpose : 
"""


#%%
# the first statment being taught in any programming language.
print('Hello')
print(' Welcome to Python' )

#%% assignment
# print your name please 



#%%
#================ variable  and datatype ==================
# variable is container that is used to hold some value

var1 = 11
print(var1)
print('var1 is '+str(var1))
type(var1)
id(var1) # location 

#%%  assignment
# ================= float =================================
# copy the last few lines and change the value of var1 to 11.2 and run the curent cell.
# what is the new data type that you got?



#%% assignment
# ================ string ================================
# copy the last few lines and change the value of var1 to your first name and run the curent cell.





#%%  assignment
# ================ complex =============================
com=1j
print(com)
type(com)
print(com*com)

#%% list 
mylist=['temp','wind','moisture']
print(mylist)
type(mylist)
# for more data types.
# https://www.w3schools.com/python/python_datatypes.asp
#http://www.python-course.eu/numpy_dtype.php

#%% assignment : what is the datatype of figure
import matplotlib.pyplot as plt 
fig=plt.figure()


#%%  assignment
# ================ list the name of 5 datatypes of Python and print them out=======
dt=['int','','','','']
type(dt)


#%% variable name 
var=1
Var=2
VAR=3
print(var)
print(Var)
print(VAR)

# what does it mean to you?

#%% how to name variable 
# you can use any combination:
#1- letters 
#2- numbers 
#3- underscore

var4calculation=4
_var = 5

#%% Donot begin with  & donot use 

# beging with number
0_var=5 
# synatax error

# prohibted names to used 
else = 3 
# to know all keywords tyep help then type  keywords

#%% naming styles

# underscore
Correlation_between_tem_pre=0.2
# camel case
CorrelationBetweenTemPre = 0.2
#%% assignment 
S='He was not here'
# print it below


# uncomment the below line and try to print it 
S1='He wasn't here'
S2="He wasn't here"
S3=""" he was n't here"""

S4='He wasn\'t here'
S5='He was here \n'
#https://www.w3schools.com/python/python_operators.asp

#%% operation on string 
# concatenation 
print("hello"+"world")
# repetion 
print("abc"*3)
# index
print("Hello"[0])
# slicing 
print("Hello"[0:3])
