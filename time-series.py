
# coding: utf-8

# In[26]:


import pandas as pd
df = pd.read_excel("restaurant.xlsx")
df.head()


# In[27]:


from dateutil import parser
#df["date"] = df.date.apply(parser.parse)
df.assign(time=df['date'].astype('str'))


# In[28]:


text = df.comments.iloc[0]


# In[45]:


from snownlp import SnowNLP
s = SnowNLP(text)


# In[46]:


s.sentiments


# In[31]:


def get_sentiment_cn(text):
    s = SnowNLP(text)
    return s.sentiments


# In[32]:


df["sentiment"] = df.comments.apply(get_sentiment_cn)


# In[42]:


#df.head()
df.assign()


# In[34]:


df.sentiment.mean()


# In[35]:


df.sentiment.median()


# In[36]:


from ggplot import *


# In[37]:


ggplot(aes(x="date", y="sentiment"), data=df) + geom_point() + geom_line(color = 'blue') + scale_x_date(labels = date_format("%Y-%m-%d"))


# In[54]:


#df.sort_values(['sentiment'])[:1]
df.sort_values(['sentiment'])[1:]


# In[39]:


print(df.sort_values(['sentiment']).iloc[0].comments)

