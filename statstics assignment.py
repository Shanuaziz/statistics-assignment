#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[31]:


data=pd.read_csv('Students_Performance (1).csv')


# In[32]:


data.head()


# In[33]:


data.shape


# In[34]:


data.info()


# In[35]:


data.isna().sum()


# In[36]:


data.columns


# In[57]:


data['gender'].value_counts()


# In[59]:


data['parental level of education'].value_counts()


# In[45]:


data['math score'].mean()


# In[46]:


data['reading score'].mean()


# In[47]:


data['writing score'].mean() 


# In[48]:


print('Avrage Maths Score : ',data['math score'].mean())
print('Avrage Reading Score : ',data['reading score'].mean())
print('Avrage Writing Score : ',data['writing score'].mean())


# In[53]:


data.groupby('gender').mean()


# In[55]:


data.groupby('test preparation course').mean()


# In[56]:


data.groupby('test preparation course').var()


# In[60]:


data['math_pass status']=np.where(data['math score']<40,'F','P')
data['read_pass status']=np.where(data['reading score']<40,'F','P')
data['write_pass status']=np.where(data['writing score']<40,'F','P')


# In[62]:


data


# In[63]:


data['math_pass status'].value_counts()


# In[64]:


data['read_pass status'].value_counts()


# In[65]:


data['write_pass status'].value_counts()


# In[81]:


pivot_gender_race = data.pivot_table(index=['gender','race/ethnicity'],values=['math score', 'reading score', 'writing score'])


# In[82]:


display(pivot_gender_race)


# In[89]:


parental_education = data.pivot_table(
                     index=['parental level of education'], 
                     values=['math score', 'reading score', 'writing score'],
                     aggfunc=np.mean
                     )


# In[90]:


display(parental_education)


# In[ ]:




