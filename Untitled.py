#!/usr/bin/env python
# coding: utf-8

# In[35]:


with open('change.txt') as f:
    lines = f.readlines()


# In[40]:


lines


# In[41]:


backups=[]
date=''


# In[42]:


for line in lines:
    signal = len(line.split(','))==1
    
    if signal:
        date=line.split(',')
        print(date)


# In[43]:


for line in lines:
    signal = len(line.split(','))==1
    
    if signal:
        date=line.split(',')
        continue
    else:
        backups.append(f"{date[0]}{line}")


# In[44]:


backups


# In[ ]:




