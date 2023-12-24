#!/usr/bin/env python
# coding: utf-8

# ## Tuples

# Create a tuple, called "Cars", with elements "BMW", "Dodge", and "Ford". 

# In[1]:


Cars = ("BMW", "Dodge","Ford")
type(Cars)


# Access the second element of this tuple.

# In[2]:


Cars[1]


# Call a method that would allow you to extract the provided name and age separately. Then print the "name" and "age" values to see if you worked correctly.

# In[6]:


name, age = 'Peter,24'


# In[3]:


name, age = 'Peter,24'.split(',')
# x = ("peter", 24)
# name, age = x
print(name)
print(age)


# Or

# In[4]:


name, age = "Peter", 24
name, age


# Create a function that takes as arguments the two values of a rectangle and then returns the Area and the Perimeter of the rectangle.
# Call the function with arguments 2 and 10 to verify it worked correctly.

# In[5]:


def rec_info(x,y):
    A = x * y
    P = 2 * (x+y)
    print("Area and Perimeter: ")
    return A,P

rec_info(2,10)

