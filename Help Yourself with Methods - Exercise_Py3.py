#!/usr/bin/env python
# coding: utf-8

# ## Help Yourself with Methods

# Append the number 100 to the Numbers list. 

# In[1]:


Numbers = [15, 40, 50]


# In[2]:


Numbers.append(100)
print(Numbers)


# With the help of the "extend method", add the numbers 115 an 140 to the list. 

# In[3]:


x = [115,140]
Numbers.extend(x)
print(Numbers)


# Print a statement, saying "The fourth element of the Numbers list is:" and then designate the value of the fourth element. Use a trailing comma.

# In[4]:


print("The fourth element of the Numbers list is:", Numbers[3])


# How many elements are there in the Numbers list?

# In[5]:


len(Numbers)

