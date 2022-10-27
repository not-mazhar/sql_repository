#!/usr/bin/env python
# coding: utf-8

# In[17]:


import re
msg="This is Zain Bamne Bamne"
msg1="This is Zain Bamne Bamne Bamne"
msg2="This is Zain Bamne B B Bamne"
msg3="This is Zain Bamne"

patt1=re.compile(f" Zain(B)* Bamne")


# In[20]:


ms1=patt1.search(msg)


# In[21]:


ms1.group()


# In[22]:


import re
msg="This is Zain Bamne Bamne"
msg1="This is Zain Bamne Bamne Bamne"
msg2="This is Zain Bamne B B Bamne"
msg3="This is Zain Bamne"

patt1=re.compile(f" Zain(B)+ Bamne")


# In[ ]:





# In[ ]:





# In[23]:


import re
script="12 drumers drumming on the floor, 11 pipers piping on the floor, 10 loaders leaping, 9 girls dancing, 3 men cleaning"


# In[24]:


patrn=re.compile(r"\d+\s\w+")


# In[25]:


fall=patrn.findall(script)


# In[26]:


fall


# In[32]:


import re
biodata="Zain is 25 years old, Mafiz is 21 years old, Umer is 22 years old, Shaazan is 25 years old, Ayusha is 21 years old, Karthik is 21 years old"
age=re.findall(r"\d+",biodata)
name=re.findall(r"[A-Z][a-z]*",biodata)


# In[33]:


age


# In[34]:


name


# In[35]:


info={}
x=0
for i in name:
    info[i]=age[x]
    x=x+1


# In[36]:


info


# In[37]:


import pandas as pd


# In[38]:


dict={"Name":name,"Age":age}


# In[39]:


dict


# In[41]:


df=pd.DataFrame(dict)


# In[42]:


df


# In[43]:


df.to_csv("Biodata.csv",index=False)


# In[45]:


import re
script1="Zain is 25 years old, Mafiz is 21 years old, Umer is 22 years old, Shaazan is 25 years old, Ayusha is 21 years old, Karthik is 21 years old"
age=re.findall(r"\d+",script1)
name=re.findall(r"[A-Z][a-z]*",script1)


# In[46]:


age


# In[47]:


name


# In[48]:


information={}
x=0
for i in name:
    information[i]=age[x]
    x=x+1


# In[49]:


information


# In[50]:


import pandas as pd


# In[51]:


dict1={"Name":name,"Age":age}


# In[52]:


dict1


# In[53]:


df=pd.DataFrame(dict1)


# In[54]:


df


# In[55]:


df.to_csv("Script1.csv",index=True)


# In[56]:


pip install beautifulsoup4


# In[ ]:




