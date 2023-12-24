#!/usr/bin/env python
# coding: utf-8

# ## Combining Conditional Statements and Functions

# Define a function, called **compare_the_two()**, with two arguments. If the first one is greater than the second one, let it print "Greater". If the second one is greater, it should print "Less". Let it print "Equal" if the two values are the same number.

# In[5]:


def compare_the_two(x,y):
    if x > y:
        print("Great")
    elif x < y :
        print("Less")
    else:
        print("Equal")
        
compare_the_two(10,10)

