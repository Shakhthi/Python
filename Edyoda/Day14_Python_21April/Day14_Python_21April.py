#!/usr/bin/env python
# coding: utf-8

# In[7]:


#dictionary Buiultin functions

d={1:2,2:3}
print(id(d),d)
d2=d.copy()

print(id(d2),d2)

#clear function

d2.clear()
#clear vs del---clear empties the dict and del deletes the dict
print(d2)




# In[13]:


#pop and popitem

d={1:2,5:6,7:8}
ans=d.pop(1)
print(ans)
print(d)
ans2=d.pop(9,"Key not found")
print(ans2)
print(d)
#ans3=d.pop(10)
#print(ans3)
#print(d)
ans3=d.popitem()
print(ans3)
print(d)

d[10]=11
ans4=d.popitem()
print(ans4)
print(d)


# In[15]:


d={1:2,5:6,7:8}

ans3=d.popitem()
print(ans3)
print(d)

d[10]=11
print("new dict",d)
ans4=d.popitem()
print(ans4)
print(d)


# In[22]:


d={1:2,5:6,7:8}

#print(d[8])# error if key not found
print(d.get(8,0))#none if key not found also custime value possible to return


# In[27]:


dictionary = {"raj": 2, "striver": 3, "vikram": 4,"Sagar":6}
print(type(dictionary.values()))


# In[30]:


dic={"ram":18,"satveer":1, "viraj":5, "rahul":15}
print(type(dic.value()))


# In[34]:


Dictionary1 = {'A': 'India', 'B': 'Nepal','C':"Bangladesh" }
Dictionary2 = {'B': 'AUstralia','A':'Pakistan'}
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)
Dictionary1['C']="Sri Lanka"
print(Dictionary1)


# In[47]:


Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# Printing keys of dictionary
for i in Dictionary1.keys():
    print(i,Dictionary1[i])
for i in Dictionary1.values():
    print(i)   
for i,j in Dictionary1.items():
    print(i," ",j)
    
print(Dictionary1.haskey('A'))


# In[46]:


Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# Dictionary to be checked
print("Dictionary to be checked: ")
print(Dictionary1)

# Use of has_key() to check
# for presence of a key in Dictionary
print(Dictionary1.has_key('A'))
print(Dictionary1.has_key('For'))


# In[51]:


#job is to change my list of values into key and some values
#list of students--convert into dictionary of student:marks before evaluation

l="EdYoda"#keys
#values-- some constant values later in change it
a=dict.fromkeys(l,0)
print(a)


# In[53]:


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 40, 90, 56, 78 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))


# In[60]:


#Set

s={1,"India",3.24}
print(s)

l=[2,3,44,2,4,56]

s=set(l)
print(s)

a=set()
d={}#emptydict
e=set()#emptyset
q={1,2}#non emptyset
w={1:2,3:4}#non empty dict
print(a,type(a))


# In[61]:


s={1,"India",3.24}

s.add("USA")

print(s)


# In[62]:


#add the numbers odd numbers from 1  to 10 into a set

a=set()
for i in range(1,11):
    if(i%2!=0):
        a.add(i)
        
print(a)        


# In[67]:


a={1,4,5,7,8}#1,8-2,6==1,8
b={2,4,5,6,7}

c=a.union(b)#sames as b.union(a)
d=a|b
print(c,d)

e=a.intersection(b)#same as a.inter(a) 
f=a&b

print(e,f)
#a-b ==b-a

print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))
a.clear()
print(a)
#subset and superset


# In[74]:


#subset and superset

A={5,10,15,20}
B={10,20}
C={10,10,20,20}
D={9,18}

print(B<A)
print(B==C)
print(A.isdisjoint(D))
D.update([2, 3, 4])
print(D)


# In[80]:


A={5,10,15,20}
A.discard(10)
print(A)
A.discard(4)
print(A)
A.remove(15)
print(A)
A.remove(0)
print(A)


# In[ ]:




