#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()


# #### In Data Analysis What All Things We Do
# 1.Missing Values
# 2.Explore About the Numerical Variables
# 3.Explore About categorical Variables
# 4.Finding Relationship between features

# In[6]:


df.shape


# In[7]:


df.isnull().sum()


# In[8]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[9]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[11]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[12]:


df.columns


# In[13]:


final_df=pd.merge(df,df_country,on='Country Code', how='left')


# In[14]:


final_df.head(3)


# In[15]:


final_df.dtypes


# In[16]:



final_df.columns


# In[17]:


country_names=final_df.Country.value_counts().index


# In[18]:


country_val=final_df.Country.value_counts().values


# In[19]:


## Pie Chart- Top 3 countries that uses zomato
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# In[20]:


final_df.columns


# In[21]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[22]:


ratings


# #### Observation
# When Rating is between 4.5 to 4.9---> Excellent
# When Rating are between 4.0 to 3.4--->very good
# when Rating is between 3.5 to 3.9----> good
# when Rating is between 3.0 to 3.4----> average
# when Rating is between 2.5 to 2.9----> average
# when Rating is between 2.0 to 2.4----> Poor

# In[24]:


ratings.head()


# In[25]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)


# In[26]:


sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# #### Observation:
# 
# Not Rated count is very high,
# Maximum number of rating are between 2.5 to 3.4

# In[27]:


## Count plot
sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[28]:


ratings


# In[29]:


### Find the countries name that has given 0 rating 
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[30]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# In[31]:


##find out which currency is used by which country?
final_df.columns


# In[32]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[33]:


## Which Countries do have online deliveries option


# In[34]:


final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()


# In[35]:


final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# In[36]:


final_df.columns


# In[37]:


## Create a pie chart for top 5 cities distribution
final_df.City.value_counts().index


# In[38]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[39]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# In[ ]:




