#!/usr/bin/env python
# coding: utf-8

# In[3]:


t=(2,3,4)
n=t+(5,6)#allowed
#not allowed
#t[0]=1
print(n)
print(t*2)
s=(0,1,2)
print(s+t)


# In[17]:


t=(56,67,78,89,12,23,24)

print(t[1:3])
print(t[-2])
print(t[::-1])

#del t[1]
print(t)
del t
#print(t)

l=[3,4,5]
e=tuple(l)
print(id(e))
print(id(l))
#max and min
#t=(3,4,5,"Ed")
#print(max(t))
#print(min(t))
s="EdYoda"
t=tuple(s)
t=("Edyoda")
print(max(t))
print(min(t))


# In[21]:


#List Operations
l=[34,54,23.5,22,12]
l.append(78)# one elemengt at once at last
print(l)
l.insert(1,89)
print(l)
l.insert(0,29)#one element at once anywhere
print(l)
a=[6,7]
l.extend(a)#multiple elements at once
print(l)
#strings--40 builtin functions--30-35 covered imp
#tuple-only 3 -4
#lists-20 builtin functions-15-16 imp


# In[32]:


#sum, max,min, sorted , sort
l=[34,54,23.5,22,12]
print(sum(l))
print(max(l))
print(min(l))
print(sorted(l,reverse=True))
print(l[2:2])
print(l[3:4])
print(l[1:])
print(l[-3])


# In[48]:


#sorted-return a new updated list and does not changes the ori. list
#sort-updates the original list and does not return anything

l=[34,54,23.5,22,12]
#print(sorted(l))
l.sort()
print(l)


# In[36]:


l=[34,54,23.5,22,12]
a=sorted(l)
#l.sort()
print(l)

print(a)


# In[41]:


#count

l=[2,3,3,2,1,4,5,6,"a","a"]
print(l.count(9))


# In[44]:


#index of string is same as index of list
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2,2,8))
print()


# In[49]:


l=[34,54,23.5,22,12]
print(id(l))
l.reverse()
print(l)
print(id(l))
#only reverse---use reverse..working is same as sort--changes the original list
#sort in reverse--use sort/sorted along with reverse parameter


# In[58]:


#del and pop
l=[34,54,23.5,22,34,12]
#del l[0]
print(l)
#del l
#print(l)
#del is used to remove the value and does nothing else
#pop is used to remove and return the value to you
a=l.pop(1)
print(a*2)
#by default  last value
print(l)
l.remove(34)
print(l)


# In[ ]:


#find the occur. using count

 #run for loop till count value
  #   and remove


# In[ ]:


#Scenario--I wanted to delete 23 from a list but do not know the index or prsence


# In[61]:


#clear --removes all the elments at once
l=[2,3,4]
l.clear()
print(l)
l.append(8)
print(l)


# In[67]:


#list operations

l=[3,4]
l1=[2,"TT"]

print(l+l1)
print(l1*3)


# In[82]:


#Dictionary introduction
#no repe in keys and no indexing
#latest value will be considered--IMPPPPP!!!!
d={}
#key values-----TUple, int, string only
#values ----any datatype
#key:value
d["ID"]=233454
d["Name"]="Sagar"
d["City"]="Delhi"
#print(d)
d["City"]="Noida"
d[0]=[9,8]
#print(d)
#del d[0]
#print(d)
d[0].append(7)
#print(d)
#print("Sagar" in d)
#print("City" in d)
d["Exam"]="Noida"
#print(d)
d["Noida"]="Noida"
#print(d)
d["Nested"]={1:2,"3":4}
print(d)
print(d["ID"])
print(d["Nested"][1])
#membership is always decided by the presence of keys


# In[ ]:




