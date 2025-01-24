#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
dataset=pd.read_csv("salary_data.csv")
dataset


# In[8]:


dataset.tail()


# In[5]:


dataset.head(10)


# In[ ]:


dataset_house=pd.read_csv("housing.csv",sheet_name='housing')


# In[10]:


import os
os.getcwd()


# In[12]:


import numpy as np
a=np.zeros(3)
a


# In[13]:


type(a)


# In[14]:


type(a[0])


# In[17]:


z=np.zeros(10)
z


# In[18]:


z.shape


# In[19]:


z.shape=(10,1)
z


# In[20]:


z=np.ones(10)
z


# In[21]:


z=np.ones(10)
type(z[0])
z


# In[24]:


z=np.empty(3)
z


# In[30]:


z=np.linspace(1,9,5)
z


# In[31]:


z=np.array([10,20])
z


# In[ ]:


matplotlib

