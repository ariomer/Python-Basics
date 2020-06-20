#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_csv("Automobile_data_v1.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf


# In[ ]:




