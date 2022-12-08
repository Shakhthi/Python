#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f():
    x=15
    print(x)
    
x=12
f()


# In[3]:


x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)


# In[4]:


s=['a','b']
se="ab"
se.append("r")
s.append


# In[5]:


func = lambda x: x
print(func(2))


# In[10]:


def fun1(name, age):
    print(name, age)

a=tuple("Emma 29".split(" "))
print(*a)
fun1(a)


# In[7]:





# In[11]:


def outerFun(a, b):
    def innerFun(c, d):
        return c + d
    return innerFun(a, b)
    return a

result = outerFun(5, 10)
print(result)


# In[14]:


def fun1(num):
    return num + 25
num=0
print(fun1(5))
print(num)


# In[15]:


def displayPerson(*args):
    for i in args:
        print(i)

displayPerson(name="Emma", age="25")


# In[19]:


gpack={'ts':'I wear Duke','s':'I wear Nike'}


def p(ts,s):
    print("I wear",s.split(" ")[2])

p(**gpack)


# In[22]:


x = 75
def myfunc():
 
    x = x + 1
    print(x)

myfunc()
print(x)


# In[23]:


class Aadhar:
    pass


# In[31]:


class Aadhar:
    org="UIDAI"
    
#CONSTRUCTOR HELPS YOU TO INITIALIZE VALUES TO YOUR OBJECTS
#__init__   
    def __init__(self,ano,name,address):
        self.ano=ano
        self.name=name
        self.address=address        
a1=Aadhar(123,"Sagar","Noida")
#self--reference word not a  keyword--so you can change it
print(a1.ano)
print(a1.name)
print(a1.address)
print(a1.org)
a2=Aadhar(113,"Preeti","Noida") 
print(a2.ano)
print(a2.name)
print(a2.address)
print(a2.org)
print(a2)


# In[ ]:




