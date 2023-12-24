#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# This is the menu of a close-by restaurant:

# In[1]:


Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}


# What is the second meal in the list?

# In[2]:


Menu['meal_2']


# Add a new meal - "Soup".

# In[3]:


Menu['meal_5'] = 'Soup'
Menu


# Replace the Hamburger with a Cheeseburger.

# In[4]:


Menu['meal_3'] = 'Cheeseburger'
Menu


# Attach the Desserts list in the form of a sixth meal.

# In[5]:


Dessert = ['Pancakes', 'Ice-cream', 'Tiramisu']


# In[6]:


Menu['meal_6'] = Dessert
Menu


# Create a new dictionary that contains the first five meals as keys and assign the following five values as prices (in dollars):
# 10, 5, 8, 12, 5. 
# Start by *Price_list = {}*.

# In[7]:


price_list = {}
price_list['Spaghetti'] = 10
price_list['Fries'] = 5
price_list['Hamburger'] = 8
price_list['Lasagna'] = 12
price_list['Soup'] = 5
print(price_list)


# Use the *.get()* method to check the price of the Spaghetti.

# In[8]:


print(price_list.get('Spaghetti'))

