#!/usr/bin/env python
# coding: utf-8

# In[5]:


a="EdYoda"
print(a[-1])
print(a[::-1])
#a[0]="y"
#del-- delete the whole string
#but cannot delete the members of string
del a[2]
#cannot delete or update the string members
print(a)


# In[6]:


s="Ed"
d="Yoda"
s=s+d
print(id(s))
print(id(d))


# In[9]:


#upper function

s="India"#INDIA
t="iNdIa"
print(s.upper())
print(t.upper())


# In[11]:


#lower() function

a="INDIA3455"

print(a.lower())


# In[18]:


#isalnum---tells whether it should have either numeric or alpha no symbols--__ ,/
# ()*
#isalpha----tells whether it should have only alpha
p="123ut/"
print(p.isalnum())
print(p.isalpha())
z="123abc"
print(z.isalnum())


# In[17]:


p="53iusd"
print(p.isalnum())
o="bbvBBYYYUUUsswa"
print(o.isalpha())


# In[23]:


#isdigit----members should always be digits--(0-9)
d=input()
print(d.isdigit())
#-9--- string two characters-- "-" and 9


# In[25]:


a="Shivangi24"
print(a.isalnum())


# In[ ]:


#islower--all members are in lower case or not(only considers alphabets)
s=input()
print(s.islower())


# In[ ]:





# In[5]:


#isupper()-all members are in upper case or not(only considers alphabets)

w=input()
print(w.isupper())


# In[10]:


#Roman , Hindi , Greek ---all numbers are identified here
#digits are the subset of numerics
#digits--0 to 9
#numerics- number system in any language (Roman, Greek that is in Unicode)



i=input()
print(i.isnumeric())


# In[2]:


#istitle --whether first alphabet of the string is capital or not
#title--convert into title case

e=input()

print(e.istitle())
print(e.title())


# In[4]:


#swapcase--changes the resp cases in a string

n=input()
print(n.swapcase())


# In[10]:


#find--lowest index of occurence
#str.find(sub, start, end)

u=input()
t=input()
print(u.find(t,2,6))


# In[12]:


#rfind----last/highest index of occurence
u=input()
t=input()
print(u.find(t))
print(u.rfind(t))


# In[17]:


#count()--counts the occurence

l=input()
k=input()
print(l.count(k))


# In[15]:


s=input()
g=input()
print(s.count(g))


# In[19]:


#index-retirn the position of first occurence of string
#find vs index---find gives -1 on being
#not found and index gives error on being not found
q=input()
w=input()
print(q.index(w))


# In[26]:


#endswith vs startwith

#endswith---OP is true or false - based on test
#startsswith---OP is true or false - based on test
x=input()
c=input()

print(x.endswith(c,1,5))
print(x.startswith(c,1,5))


# In[29]:


#capitalize vs title

s=input()
print(s.capitalize())
print(s.title())

#capitalize
ans=""
for i in range(len(s)):
    
    if(i==0):
        ans=ans+s[i].upper()
    else:
        ans=ans+s[i].lower()
print(ans)


# In[ ]:




