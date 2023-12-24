#!/usr/bin/env python
# coding: utf-8

# ## Notable Built-In Functions in Python

# Obtain the maximum number among the values 25, 65, 890, and 15.

# In[1]:


x = (25,65,890,15)
b = max(x)
print(b)


# Obtain the minimum number among the values 25, 65, 890, and 15.

# In[2]:


x = (25,65,890,15)
b = min(x)
print(b)


# Find the absolute value of -100

# In[3]:


abs(-100)


# Round the value of 55.5. Did you obtain 56.0?

# In[4]:


round(55.5,0)


# Round 35.56789 to the third digit.

# In[5]:


round(35.56789,3)


# Find the sum of all elements in the provided list, called "Numbers".

# In[7]:


Numbers = [1, 5, 64, 24.5]


# In[8]:


x = sum(Numbers)
print(x)


# Use a built-in function to raise 10 to the power of 3.

# In[9]:


pow(10,3)


# How many characters are there in the word "Elephant"?

# In[10]:


len("Elephant")


# Create a function, called "distance_from_zero", that returns the absolute value of a provided single argument and prints a statement "Not Possible" if the argument provided is not a number.
# Call the funtion with the values of -10 and "cat" to verify it works correctly.

# In[11]:


def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        print(abs(x))
    else:
        print("Not Possible")

        


# In[12]:


distance_from_zero("cat")


# In[13]:


distance_from_zero(-100)

