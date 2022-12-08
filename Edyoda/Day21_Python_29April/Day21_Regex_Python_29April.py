#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
p="[^a-z]"#starting position
s=input()
r=re.findall(p,s)
print(r)


# In[14]:


import re
p="[^a-zA-Z]$"#starting position
s=input()
r=re.findall(p,s)
print(r)


# In[36]:


import re
p="m*n"#starting position
s=input()
r=re.findall(p,s)
print(r)


# In[42]:


import re
p="m+n"
s=input()
r=re.findall(p,s)
print(r)


# In[46]:


import re
p="m?n"
s=input()
r=re.findall(p,s)
print(r)


# In[54]:


import re
p="ad{2,3}"
s=input()
r=re.findall(p,s)
print(r)


# In[59]:


import re
p="[0-9]{3,4}"
s=input()
r=re.findall(p,s)
print(r)


# In[62]:


import re
p="[a-c]"
s=input()
r=re.findall(p,s)
print(r)


# In[68]:


import re
p="(a|b)[^0-9]$"
s=input()
r=re.findall(p,s)
print(r)


# In[73]:


import re
p="\$a+"
s=input()
r=re.findall(p,s)
print(r)


# In[79]:


import re
p="\A[A]"
s=input()
r=re.findall(p,s)
print(r)


# In[86]:


import re
p="foo\b"
s=input()
r=re.findall(p,s)
print(r)


# In[94]:


import re
p=r"foo\b"
s=input()
r=re.findall(p,s)
print(r)


# In[95]:


import re
p=r"\Bfoo"
s=input()
r=re.findall(p,s)
print(r)


# In[103]:


import re
p=r"\S"
s=input()
r=re.findall(p,s)
print(r)
aa="".join(r)
print(aa)


# In[105]:


import re
p=r"\w"
s=input()
r=re.findall(p,s)
print(r)
aa="".join(r)
print(aa)


# In[ ]:




