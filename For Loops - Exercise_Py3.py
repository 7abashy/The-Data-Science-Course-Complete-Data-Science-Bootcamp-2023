#!/usr/bin/env python
# coding: utf-8

# ## For Loops

# Create a For loop that prints every digit on a new line.

# In[1]:


digits = [0,1,2,3,4,5,6,7,8,9]


# In[2]:


for x in digits:
    print(x)


# Adjust the code, so the digits are all printed on the same line.

# In[3]:


for x in digits:
    print(x, end = " ")

