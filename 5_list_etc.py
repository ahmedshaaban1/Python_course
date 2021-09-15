#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Ahmed Shaaban
Date     : Sep 5, 2021
purpose  : breif on loops.
"""
#%%================================
mystring="python is a nice language"
mylist  = ["python","is","a nice","language"]
mytuple =  ("python","is","a nice","language")

# print the data type of each data type above.



# print the length of each of the above.



# print the first element of each of the above data types.




# could we change the first element in mystring, mylist, and mytuple
# mystring

# mylist

# mytuple

#%% slicing
mylist=[10,20,30,40,50,60,70,80,90,100]

print("mylist[-1] is "+str(mylist[-1]))
print("mylist [::2] is "+str(mylist[::2]))
print("mylist[1:2] is "+str(mylist[1:2]))
print("mylist[1] is "+str(mylist[1]))

#%%  Operator overloading
mylist=[10,20,30,40,50,60,70,80,90,100]


added_list=mylist+mylist
print(added_list)

multiplied_list=mylist*2
print(multiplied_list)

#%% tricky point : nested lists
multiplied_list1=[mylist]*2
print("multiplied list is")
print(multiplied_list1)
print("my new list")
multiplied_list1[0][0]=0
print(multiplied_list1)
# explanation 
id(multiplied_list1[0])
id(multiplied_list1[1])
#%%
mylist1=["a",["b","c"],["d","e","f"]]

# print the lenght of mylist1


# print the first element 


# print the second element ["b","c"] 


# print the third elemenet ["d","e","f"] 


# print c


# print d 


# replace the third element (nested list) with "z"

#%%  list functions:::  append
myvariables=['pressure','temperature','u','v','w']
myvariables.append('rh')
print(myvariables)

#%%  list functions:::  append
myvariables=['pressure','temperature','u','v','w']
myvariables.append(['rh','r'])
print(myvariables)

#%%  list functions:::  extend
myvariables=['pressure','temperature','u','v','w']
myvariables.extend(['rh','r'])
print(myvariables)

#%% list functions:::  insert
myvariables.insert(0,'station')
print(myvariables)

#%% list functions::: pop
myvariables=['pressure','temperature','u','v','w']
mypop=myvariables.pop()
print(mypop)
print(myvariables)
#%% list functions::: pop
myvariables=['pressure','temperature','u','v','w']
mypop=myvariables.pop(-1)
print(mypop)
print(myvariables)

#%% list functions::: pop
myvariables=['pressure','temperature','u','v','w']
mypop=myvariables.pop(2)
print(mypop)
print(myvariables)

#%% 
old_variables = ['pressure', 'tem', 'u', 'v', 'w', 'rh']
new_variables = []
while old_variables != []:
    tmp = old_variables.pop()
    new_variables.append(tmp) 
    print(tmp,old_variables,new_variables)

#%% list functions:: remove 
myvariables=['pressure','temperature','u','v','w']
myvariables.remove("pressure")
print(myvariables)
#%% list functioon : remove 
myvariables=['pressure','temperature','u','v','w']
print(myvariables.index("u"))
#%% list functions : insert
myvariables=['pressure','temperature','u','v','w']
myvariables.insert(0,"u")
print(myvariables)

#%%
# the purpoose of the following code snippet is to compare the speed of the 
# normal assignment(i=i+1) vs augmented assingment (+=) vs append function on list.

import time
n= 100000
start_time = time.time() 
l = []
for i in range(n):
    l = l + [i * 2] 
    #print(id(l))
print(time.time() - start_time)

#%%
start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
    #print(id(l))
print(time.time() - start_time)
#%% 
start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
    #print(id(l))
print(time.time() - start_time)


#%% take home messages from the last exercise
# augmented assigment is faster than normal assignment
# built in functions are fast.

# but how about numerical data type 
#%%
import time
n= 100000
start_time = time.time() 
l = 0
for i in range(n):
    l = l + 1 
    #print(id(l))
print(time.time() - start_time)

#%%
start_time = time.time()
l = 0
for i in range(n):
    l += 1
    #print(id(l))
print(time.time() - start_time)
#%% 
start_time = time.time()
l = 0
for i in range(n):
    l=l.__add__(1)
    #print(id(l))
print(time.time() - start_time)