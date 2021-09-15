#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Ahmed Shaaban
Date   : Sep 13, 2021
Purpose: demonstrating functions
"""

print("converting celsius to fahrenheit and Kelvin")
tem_cel = 30
tem_fahr = (tem_cel*9./5.)+32
tem_kel = tem_cel + 273.15
print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
print(str(tem_cel)+" degree cel is "+str(tem_kel)+" degree Kelvin")


print("converting celsius to fahrenheit and Kelvin")
tem_cel = 10
tem_fahr = (tem_cel*9./5.)+32
tem_kel = tem_cel + 273.15
print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
print(str(tem_cel)+" degree cel is "+str(tem_kel)+" Kelvin")


print("converting celsius to fahrenheit and Kelvin")
tem_cel = 25
tem_fahr = (tem_cel*9./5.)+32
tem_kel = tem_cel + 273.15
print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
print(str(tem_cel)+" degree cel is "+str(tem_kel)+" Kelvin")

#%% function to say hello 
def Hello_all():
    print("Welcom to Functions! ")
    
#%% calling the function
Hello_all()
#%% temperature conversion function
def temp_conversion(tem_cel):
    print("converting celsius to fahrenheit and Kelvin")
    tem_fahr = (tem_cel*9./5.)+32
    tem_kel = tem_cel + 273.15
    print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
    print(str(tem_cel)+" degree cel is "+str(tem_kel)+"  Kelvin")
    
#%% 
temp_conversion(30)
#%% function with defintion 
help(abs)
#%%  docstring
def temp_conversion(tem_cel):
    '''
    temp_conversion function is used to convert 
    temperature from degree celsius to degree Fahreheit
    Parameters
    ----------
    tem_cel : TYPE
        temperature in celsius.

    Returns
    -------
    temperature in Kelvin and Fahreheit.

    '''
    print("converting celsius to fahrenheit and Kelvin")
    tem_fahr = (tem_cel*9./5.)+32
    tem_kel = tem_cel + 273.15
    print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
    print(str(tem_cel)+" degree cel is "+str(tem_kel)+"  Kelvin")
#%%
help(temp_conversion)
#%%
print(temp_conversion.__doc__)
#%% coverting a list of temperatures ...
for x in [10,20,30]:
    temp_conversion(x)
#%% return statement 
def temp_conversion(tem_cel):
    '''
    temp_conversion function is used to convert 
    temperature from degree celsius to degree Fahreheit
    Parameters
    ----------
    tem_cel : TYPE
        temperature in celsius.

    Returns
    -------
    temperature in Kelvin and Fahreheit.

    '''
    print("converting celsius to fahrenheit and Kelvin")
    tem_fahr = (tem_cel*9./5.)+32
    tem_kel = tem_cel + 273.15
    print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
    print(str(tem_cel)+" degree cel is "+str(tem_kel)+"  Kelvin")
    return tem_fahr,tem_kel
#%% 
x=temp_conversion(30)
print(x)
print(type(x))
#%% 
x[0]=100
print(id(x))
#%% 
temp_conversion(20)
temp_conversion(tem_cel=20)
#%% 
temp_conversion()

#%% default input value
def temp_conversion(tem_cel=30):
    '''
    temp_conversion function is used to convert 
    temperature from degree celsius to degree Fahreheit
    Parameters
    ----------
    tem_cel : TYPE
        temperature in celsius.

    Returns
    -------
    temperature in Kelvin and Fahreheit.

    '''
    print("converting celsius to fahrenheit and Kelvin")
    tem_fahr = (tem_cel*9./5.)+32
    tem_kel = tem_cel + 273.15
    print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
    print(str(tem_cel)+" degree cel is "+str(tem_kel)+"  Kelvin")
    return tem_fahr,tem_kel
#%% 
temp_conversion()
print(temp_conversion.__defaults__)
temp_conversion(20)

#%% raise error if the tem_cel > 100
def temp_conversion(tem_cel=30):
    '''
    temp_conversion function is used to convert 
    temperature from degree celsius to degree Fahreheit
    Parameters
    ----------
    tem_cel : TYPE
        temperature in celsius.

    Returns
    -------
    temperature in Kelvin and Fahreheit.

    '''
    import sys
    if (tem_cel > 100):
        print("existing as tem > 100")
        sys.exit()
        
    print("converting celsius to fahrenheit and Kelvin")
    tem_fahr = (tem_cel*9./5.)+32
    tem_kel = tem_cel + 273.15
    print(str(tem_cel)+" degree cel is "+str(tem_fahr)+" degree fahrenheit")
    print(str(tem_cel)+" degree cel is "+str(tem_kel)+"  Kelvin")
    return tem_fahr,tem_kel
#%% 
temp_conversion(100)
#%% 
def test():
    print("test")
    return -1

#%% local and global variables:
    
#%% local variable used after assignment
a = None # ensure that a is not defined... this is better than del a

def f():
    a="ali"
    print("inside function "+a+" "+str(id(a)))
    
f()
print(f.__code__.co_varnames)

#%% variable inside function could be defined outside function
a = None # ensure that a is not defined... this is better than del a

def f():
    print("inside function "+a+" "+str(id(a)))
    
a="ahmed"
print("outside function "+a+" "+str(id(a)))
f()
print(f.__code__.co_varnames)

#%% 
a = "ahmed" # ensure that a is not defined... this is better than del a

def f():
    a="ali"
    print("inside function "+a+" "+str(id(a)))
    
print("outside function "+a+" "+str(id(a)))
f()
print("outside function "+a+" "+str(id(a))) 

print(f.__code__.co_varnames)

#%% the trickest one 
a = None # ensure that a is not defined... this is better than del a


def f():
    print("inside function "+a+" "+str(id(a)))
    # if variable is assigned to specific value, then it must be used only after assignment even it has been defined outside the scope of the function
    a="ali" # comment this line to see the difference

a="ahmed"
f()

#%% 
a = None # ensure that a is not defined... this is better than del a

def f():
    global a
    print("inside function "+a+" "+str(id(a)))
    a="ali" # comment this line to see the difference

a="ahmed"
f()
# see this post on stackoverflow https://stackoverflow.com/questions/8943933/variables-declared-outside-function

#%% unknown number of values 
def mysum(first, *values):
    mysum=first+sum(values)

    return mysum

print(mysum(1,2,3))
print(mysum(2,4,5,6,78))

#%% unkonwn number of arguments 
def f(temp,**kwargs):
    pres       =kwargs.get('pres')
    rh         =kwargs.get('rh')
    
    print("temperature is "+str(temp))
    if pres is not None:
        print("pressue is "+str(pres)) 
    if rh is not None:
        print("rh is "+str(rh))
    
f(30)
print("-----------------")
f(30,pres=1004)
print("-----------------")
f(30,rh=100)
print("-----------------")
f(30,pres=1002,rh=100)