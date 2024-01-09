#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[52]:


data=pd.read_csv('Sales_add (1).csv')


# In[53]:


data


# In[54]:


from scipy.stats import ttest_ind


# In[55]:


mark1=data['Sales_before_digital_add(in $)']


# In[56]:


mark2=data['Sales_After_digital_add(in $)']


# In[57]:


ttest_ind(mark1,mark2)


# In[58]:


t_test,pvalue=ttest_ind(mark1,mark2)


# In[59]:


pvalue


# In[60]:


if pvalue <0.05:
    print('Reject Null Hypothesis')
else:
    print('Accept Null Hypothesis')


# In[ ]:




