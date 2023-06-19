#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the relevant modules
import requests
import json
from urllib.parse import urlparse, parse_qs


# In[2]:


# define base URL
base_site = "https://itunes.apple.com/search"


# In[3]:


parse_result = urlparse(base_site)
parse_result


# In[4]:


print(parse_result.scheme)


# In[9]:


# Make a request
r = requests.get(base_site, params = {"term": "bon jovi", "country": "id", "limit": 200}) # only pulling bon jovi data
r.status_code


# In[10]:


r


# # Inspect the structure of the response

# In[11]:


# Store the response
info = r.json()
info


# In[16]:


print(json.dumps(r.json(), indent=4))


# In[18]:


r.json().keys()


# # Locate the name and release date of a song

# In[19]:


r.json()['resultCount']


# In[20]:


data = r.json()
data1 = data['results']
data1


# In[21]:


# def calling (x,y):
for z in data['results']:
    x = print(z['artistName'])
    y = print(z['releaseDate'])

# calling(y)
# calling(x,y)


# In[22]:


import pandas as pd


# In[23]:


data_itunes = pd.DataFrame(data['results'])
data_itunes


# In[24]:


data_itunes.to_csv("bon_jovi_itunes_data.csv")


# In[ ]:




