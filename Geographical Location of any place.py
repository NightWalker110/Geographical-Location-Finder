#!/usr/bin/env python
# coding: utf-8

# In[2]:


from geopy.geocoders import Nominatim
from pprint import pprint


# In[11]:


app = Nominatim(user_agent="Location")
location = app.geocode("Chandigarh").raw
pprint(location)


# In[ ]:




