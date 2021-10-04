#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reversal_array(arr): #Declaring a function 
    li=arr[::-1]         #Through indexing reversing array and storing it in 'li' list
    return li            # Returning li
arr=[int(x) for x in input().split()] #Through list comprehension taking input
res=reversal_array(arr)               # Calling function and storing the result in 'res'
print(res)                            # printing Result

