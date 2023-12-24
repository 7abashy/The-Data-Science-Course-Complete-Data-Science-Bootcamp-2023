#!/usr/bin/env python
# coding: utf-8

# ## All in - Conditional Statements, Functions, and Loops

# You are provided with the 'nums' list. Complete the code in the cell that follows. Use a while loop to count the number of values lower than 20. 
# *Hint: This exercise is similar to what we did in the video lecture. You might prefer using the x[item] structure for indicating the value of an element from the list.*

# In[1]:


nums = [1,16,18,10,12,24,31,51,70,100]
len(nums)


# In[2]:


y=[]
n = 1
while n < len(nums):
    for x in nums:
        if x < 20:
            y.append(x)
        n += 1   
    print(f"Total numbers lower than 20 = {len(y)}", end=" ")   


# In[3]:


def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total       


# In[4]:


count(nums)

