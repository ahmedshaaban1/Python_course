#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Ahmed Shaaban
Date     : Sep 5, 2021
purpose  : breif on loops.
"""

#%% range (start,end, step) datatype 

# what is range? datatype that return object.
print(type(range(4)))

# note the end 
print(list(range(0,4)))

# note the begining.
print(list(range(4)))

# note the dataytype 
print(type(list(range(4)))) # now list and not range


#%% print numbers from 1 to 10
for i in range(1,10+1):
    print(i)
#%% print numbers from 1 to 10 in one line
for i in range(1,10):
    print(i,end=" ")
#%% print odd numbers 
for i in range(1,10+1,3):
    print(i)
#%% print even numbers 
for i in range(0,10+1,2):
    print(i)
#%% print number from -10,1
for i in range(10,0,-1):
    print(i)
#%% reversed function
for i in reversed(range(1,10+1)):
    print(i)
#%% print 1 to 10 and their squares.
for i in range(0,10+1):
    print(i,i**2)
#%% print range attributes 
print(range(3).start)
print(range(3).stop)
print(range(3).step)
#%% classical assingment (sum numbers from 1 to n)
n=10
mysum=0
for i in range(1,n+1):
    mysum=mysum+i
    
print(mysum)

#%% arange (numpy)
import numpy as np
print(type(np.arange(4)))
# no need for list 
print(np.arange(4))
#%% another trick to include 10
for i in np.arange(1.,10.1):
    print(i)
#%% difference between the arange and range.
np.arange(0.1,1,0.1)
range(0.1,1,0.1)
#%% 
import sys

x = range(1,10000)
print(sys.getsizeof(x))  # --> Output is 48

y=list(x)
print(sys.getsizeof(y))

a = np.arange(1,10000)
print(sys.getsizeof(a))  # --> OutPut is 80096
#%% 
print(np.arange(-5,1, dtype=np.int32)) # signed int
print(np.arange(-5,1, dtype=np.uint32)) # unsigned int
print(np.arange(-5,1, dtype=np.float16)) #float

#%%  accessing list 
languages = ["C","C++","Python","Fortran"]
for lang in languages:
    print(lang)
#%% another way to access list 
for i in range(len(languages)):
    print(languages[i])
    
#%% else after loop

for i in range(5):
    print(i)
    if (i == 5):
        print('oh no')
        break
else: # executed if break was not encountred. 
    print("intersting!")

#%% continue
for i in range(5):
    if (i == 2): # skip 2 and continue.
        continue
    print(i)
