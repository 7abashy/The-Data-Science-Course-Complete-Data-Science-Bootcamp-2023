#!/usr/bin/env python
# coding: utf-8

# ## Using a Function in Another Function

# Define a function that adds 5 to the parameter. Then, define another function that will multiply the newly obtained number by 3.
# Verify your code was correct by calling the second function with an argument of 5. 
# Was your output equal to 30?

# In[1]:


def add_fun(x):
    return x + 5

def multi_fun(y):
    x = add_fun(y) * 3
    return x

multi_fun(5)


# In[ ]:




