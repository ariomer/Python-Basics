#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv("Automobile_data_v2.csv")
df = df [['company','price']][df.price==df['price'].max()]
df


# In[2]:


df.to_csv("Automobile_data_v1.csv")


# In[ ]:




