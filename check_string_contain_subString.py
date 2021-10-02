#!/usr/bin/env python
# coding: utf-8

# # Method 1: Using in Operator

# In[2]:


string = "Python coding day"
substring = "Python"
 
if substring in string:
    print("Found the substring")
else:
    print("Not Found")


# # Method 2: Using find() method

# In[3]:


string = "Python coding day"
substring = "Python"
 
if string.find(substring) != -1:
    print("Found the substring")
else:
    print("Not Found")


# # Method 3: Using index() method

# In[10]:


string = "Python coding day"
substring = "Python"

try:
    string.index(substring)
except ValueError:
    print("Not Found")
else:
    print("Found the substring")


# # Method 4: Using count() method

# In[7]:


string = "Python coding day"
substring = "Python"
 
if string.count(substring) > 0:
    print("Found the substring")
else:
    print("Not Found")


# # Method 5: Using REGEX

# In[9]:


from re import search

string = "Pythoncodingday"
substring = "Python"

if search(substring, string):
    print("Found the substring")
else:
    print("Not found")


# In[ ]:




