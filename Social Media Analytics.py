#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


social_media_df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Social Media Analytics\Simulated_Social_Media_Data.xlsx")


# In[3]:


social_media_df.head()


# In[4]:


# Calculating average engagement metrics by post type
average_engagement_by_type = social_media_df.groupby('post_type').mean()
average_engagement_by_type


# In[5]:


# Calculating the correlation matrix
correlation_matrix = social_media_df[['likes', 'comments', 'shares', 'new_followers']].corr()
correlation_matrix


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


# Setting the style for the plots
sns.set(style="whitegrid")


# In[8]:


# Aggregating data by date
date_aggregated_data = social_media_df.groupby('date').sum()


# In[9]:


# Plotting
plt.figure(figsize=(15, 6))


# In[10]:


# Total Engagement (likes + comments + shares) over time
plt.subplot(1, 2, 1)
plt.plot(date_aggregated_data.index, date_aggregated_data['likes'] + date_aggregated_data['comments'] + date_aggregated_data['shares'], label='Total Engagement', color='b')
plt.xlabel('Date')
plt.ylabel('Total Engagement')
plt.title('Total Engagement Over Time')
plt.xticks(rotation=45)


# In[11]:


# New Followers over time
plt.subplot(1, 2, 2)
plt.plot(date_aggregated_data.index, date_aggregated_data['new_followers'], label='New Followers', color='g')
plt.xlabel('Date')
plt.ylabel('New Followers')
plt.title('New Followers Over Time')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# In[ ]:




