#!/usr/bin/env python
# coding: utf-8

# <h1>Cancer Research Study using Numpy and Pandas

# >Using a dataset from Kaggle and the libraries Numpy and Pandas, we will be doing an exploratory data analysis to answer the following questions:
# 
# >Which states have the most annual cancer diagnosies?
# 
# >Which states have the most anual deaths from cancer?

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('cancer_reg.csv')


# In[5]:


df.head()


# >Cleaning up data

# In[7]:


df.drop(columns=df.loc[:, 'percentmarried':'birthrate'], inplace=True)


# In[8]:


df.drop(['medincome'], axis=1)


# In[1]:


df.drop(columns=df.loc[:, 'povertypercent':'medianagefemale'], inplace=True)


# In[162]:


df.head(22)


# >filling all null values if any

# In[164]:


nan_count = df.isnull().sum().sum()
print('Number of NaN values:', nan_count)


# In[165]:


def replace_values(x):
    if 'Washington' in x:
        return 'Washington'
    elif 'West Virginia' in x:
        return 'West Virginia'
    elif 'Wisconsin' in x:
        return 'Wisconsin'
    elif 'Nebraska' in x:
        return 'Nebraska'
    elif 'Nevada' in x:
        return 'Nevada'
    elif 'New Hampshire' in x:
        return 'New Hampshire'
    elif 'New Jersey' in x:
        return 'New Jersey'
    elif 'New Mexico' in x:
        return 'New Mexico'
    elif 'New York' in x:
        return 'New York'
    elif 'Virginia' in x:
        return 'Virginia'
    elif 'Michigan' in x:
        return 'Michigan'
    elif 'Minnesota' in x:
        return 'Minnesota'
    elif 'North Carolina' in x:
        return 'North Carolina'
    elif 'North Dakota' in x:
        return 'North Dakota'
    elif 'Alabama' in x:
        return 'Alabama'
    elif 'Arkansas' in x:
        return 'Arkansas'
    elif 'California' in x:
        return 'California'
    elif 'Kansas' in x:
        return 'Kansas'
    elif 'Iowa' in x:
        return 'Iowa'
    elif 'Indiana' in x:
        return 'Indiana'
    elif 'Illinois'in x:
        return 'Illinois'
    elif 'Tennessee' in x:
        return 'Tennessee'
    elif 'South Dakota' in x:
        return 'South Dakota'
    elif 'South Carolina' in x:
        return 'South Carolina'
    elif 'Arizona' in x:
        return 'Arizona'
    elif 'Alaska' in x:
        return 'Alaska'
    elif 'Georgia' in x:
        return 'Georgia'
    elif 'Louisiana' in x:
        return 'Louisiana'
    elif 'Kentucky' in x:
        return 'Kentucky'
    elif 'Mississippi' in x:
        return 'Mississippi'
    elif 'Idaho' in x:
        return 'Idaho'
    elif 'Montana' in x:
        return 'Montana'
    elif 'Missouri' in x:
        return 'Missouri'
    elif 'Texas' in x:
        return 'Texas'
    elif 'Pennsylvania' in x:
        return 'Pennsylvania'
    elif 'Oklahoma' in x:
        return 'Oklahoma'
    elif 'Oregon' in x:
        return 'Oregon'
    elif 'Ohio' in x:
        return 'Ohio'
    elif 'Florida' in x:
        return 'Florida'
    elif 'Delaware' in x:
        return 'Delaware'
    elif 'Connecticut' in x:
        return 'Connecticut'
    elif 'Colorado' in x:
        return 'Colorado'
    elif 'Wyoming' in x:
        return 'Wyoming'
    elif 'Wisconsin' in x:
        return 'Wisconsin'
    elif 'Massachusetts' in x:
        return 'Massachusetts'
    elif 'Vermont' in x:
        return 'Vermont'
    elif 'Utah' in x:
        return 'Utah'
    elif 'Maryland' in x:
        return 'Maryland'
    elif 'Maine' in x:
        return 'Maine'
    elif 'Rhode Island' in x:
        return 'Rhode Island'
    elif 'Hawaii' in x:
        return 'Hawaii'
    else:
        return 'District of Columbia'


# In[166]:


df['geography'] = df['geography'].apply(replace_values)


# In[167]:


agg_functions = {'popest2015': 'sum', 'avganncount': 'sum', 'avgdeathsperyear': 'sum', 'target_deathrate': 'mean', 'incidencerate': 'mean'}


# In[168]:


df.rename(columns = {'geography':'State'}, inplace = True) 


# In[169]:


df_new = df.groupby(df['State']).aggregate(agg_functions)


# In[170]:


df_new['avganncount'] = df_new['avganncount'].astype(int)


# In[171]:


df_new['target_deathrate'] = df_new['target_deathrate'].astype(int)
df_new['incidencerate'] = df_new['incidencerate'].astype(int)


# In[172]:


df_new.rename(columns = {'popest2015':'Population', 'avganncount': 'Annual_Diag', 'avgdeathsperyear': 'Deaths', 'target_deathrate': 'Target Rate', 'incidencerate': 'Curr_Rate'}, inplace = True) 


# In[173]:


df_new


# In[174]:


df_new['Perc_Diag'] = ((df_new['Annual_Diag']/df_new['Population'])*100).round(2)


# In[175]:


df_new['Perc_TotalDeaths'] = ((df_new['Deaths']/df_new['Population'])*100).round(2)


# In[176]:


df_new['Perc_DeathFromDiag'] = ((df_new['Deaths']/df_new['Annual_Diag'])*100).round(2)


# In[177]:


df_new


# In[185]:


df_MostAnuualDiag=df_new['Annual_Diag'].sort_values(ascending=False)


# In[193]:


df_MostAnuualDiag


# In[194]:


df_HighestPercDiag=df_new['Perc_Diag'].sort_values(ascending=False)


# In[195]:


df_HighestPercDiag


# In[189]:


df_MostAnuualDeaths=df_new['Deaths'].sort_values(ascending=False)


# In[190]:


df_MostAnuualDeaths


# In[ ]:




