#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author   : Ahmed Shaaban
Date     : Sep 1, 2021
purpose  :
"""

#%% mutalbe vs immuatalbe
# mutable : could be changed while keeping the same id
# immutable : could not be changed when keeping the same id.
#%%
##### immuable  ########
# immutable object can not be changed without changing the ID of the variable.
a=4
id(a)
a=a+1
id(a)


myword='hello'
id(myword)
myword[0]='a' # Don't mess with immutable

#%%
####### mutable #########
# mutable object could be changed witout changing the ID
mylist=[1,2,3,4]
id(mylist)
mylist[0]=100
print(mylist)
id(mylist)


#%%  assignment
x=100
y1=x 
print('Id of x ='+str(id(x))) 
print('Id of y1='+str(id(y1)))


y2=x*1
y3=x*1.
print('Id of y2='+str(id(y2)))
print('Id of y2='+str(id(y3)))

#https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper

# Immuatable : copy is pointer.

#"The concept of copying is irrelevant to immutable objects like integers and strings. Since you can't modify those objects, there is never a need to have two copies of the same value in memory at different locations. So integers and strings, and some other objects to which the concept of copying does not apply, are simply reassigned. "


#%% copy 
# colors1 contains one imutable object (string) and one mutable object (list)
colors1 = ["red", ["blue","green"]]
colors2 = colors1

print(colors1)
print(colors2)
# do colors1 and colors2 share the same location?
print('Is the id of colors1=colors2 '+str(id(colors1)==id(colors2)))

# what about the items?
print('Is the id of the colors1[0] = colors2[0] '+str(id(colors1[0]) ==id(colors2[0])))

print('Is the id of the colors1[1] = colors2[1] '+str(id(colors1[1]) ==id(colors2[1])))

#%% 
# if colors1 changes, then colors2 will also change.
colors1[0]= "black"
print(colors1)
print(colors2)

# if colors2 changes, then colors1 will also change.
colors2[0]="gray"
print(colors1)
print(colors2)


#%% shallow copy
import copy
print(colors1)
colors_shw=copy.copy(colors1) # shallow copy
print(colors_shw)
# do colors1 and colors2 share the same location?
print('Is the id of colors1=colors2:: '+str(id(colors1)==id(colors_shw)))

print('Is the id of colors1[0]=colors2[0]:: '+str(id(colors1[0])==id(colors_shw[0])))

print('Is the id of colors1[1]=colors2[1]:: '+str(id(colors1[1])==id(colors_shw[1])))

#%%
colors1[0]='red'
print(colors1)
print(colors_shw)

colors1[1][0]="rose"
print(colors1)
print(colors_shw)
#%% Deep copy
colors1 = ["red", ["blue","green"]]

colors_deep=copy.deepcopy(colors1) # deep copy
print(colors1)
print(colors_deep)
# do colors1 and colors2 share the same location?
# do colors1 and colors2 share the same location?
print('Is the id of colors1=colors2 '+str(id(colors1)==id(colors_deep)))

print('Is the id of colors1[0]=colors2[0] '+str(id(colors1[0])==id(colors_deep[0])))

print('Is the id of colors1[1]=colors2[1] '+str(id(colors1[1])==id(colors_deep[1])))

#%%
colors1[0]='black'
print(colors1)
print(colors_deep)

colors1[1][0]="rose"
print(colors1)
print(colors_deep)