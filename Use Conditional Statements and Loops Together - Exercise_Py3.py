#!/usr/bin/env python
# coding: utf-8

# ## Use Conditional Statements and Loops Together

# Create a For loop that will print all the variables from a given list multiplied by 2. Let the list contain all numbers from 1 to 10. Create it with the help of the range() function.

# In[1]:


for x in range(1,10):
    x *= 2
    print(x, end=" ")


# Create a little program that runs a loop over all values from 1 to 30. Let it print all Odd numbers, and in the place of the even numbers, it should print "Even".
# Help yourself with the range() function to solve this exercise.

# In[2]:


x = 1 
while x <=30:
    if x % 2 == 0:
        print(f"{x} is odd Number")
        x += 1
    else:
        print(f"{x} is Even Nubmer")
        x += 1


# You have the following list of numbers. Iterate over this list, printing out each list value multiplied by 10.
# Find two solutions of this problem.

# In[3]:


n = [1,2,3,4,5,6]


# In[4]:


for x in n:
    print(x*10, end=" ")


# In[5]:


n = 1
while n <= 6:
    if n <7:
        print(n * 10, end=" ")
    n +=1

