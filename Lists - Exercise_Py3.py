#!/usr/bin/env python
# coding: utf-8

# ## Lists

# Create a list, called "Numbers". Let it contain the numbers 10, 25, 40, and 50.

# In[1]:


number = [10,25,40,50]


# Print the element at index 2 from the list.

# In[2]:


print(number[2])


# Print the 0th element.

# In[3]:


print(number[0])


# Print the third-to-last element using a minus sign in the brackets.

# In[4]:


print(number[-3])


# Substitute the number 10 with the number 15.

# In[5]:


number[0] = 15
print(number)


# Delete the number 25 from the Numbers list.

# In[6]:


number.remove(25)
print(number)

