#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Quiz3 Discussion
#Q1
a=input()
print(ord(a))


# In[5]:


#Q2
s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))
print(2 * (s + t))


# In[9]:


#Q3

print('p' + 'q' if '12'.isnumeric() else 'r' + 's')
#isdigit is a subset of isnumeric


# In[13]:


#Q4

i=1
while True:
    if i%3==0:
        break
    print(i)
    i+=1


# In[14]:


#Q8

x='abcd'
for i in range(len(x)):
    x='a'
    print(x)


# In[15]:


print('ab,cd,ef,cd,gh.cd'.split(','))


# In[16]:


a="T"
b="C"
c=a+b
print(c)


# In[ ]:


#Quiz4 Q2

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
index = 0
for i in range(1,11,2):
    l1.insert(i, l2[index])
    index += 1
print(l1)


# In[17]:


a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]

print(b)


# In[19]:



print(type(t))
l=["foo"]
t = ('foo',)
se=set('foo')
#{a,b} and set()
#{a:b} dict
st = ('foo')


# In[22]:


l1 = [[1,2,3],[4,5,6]] 
l2 = []
for list1 in l1:
    l2.extend(list1)
print(l2)
#extend and + is same for lists


# In[24]:


a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

d={}
for i in a:
    d[i[-1]]=i
print(d)
# n loops= total loops in two nested loops=n*n
a=[]
for i in sorted(d.keys()):
    print(i,d[i], end=" ")

    a.append(d[i])
print(a)


# In[ ]:


def last(n): 
    return n[-1]

def sort(tuples):
    return sorted(tuples, key=last)

print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[ ]:


list_tuples= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# nested for loop 
for i in range(1,len(list_tuples)):
    for j in range(len(list_tuples)- i):
        if list_tuples[j][1] > list_tuples[j+1][1]:
            temp=list_tuples[j] #--->created temp varaible and stored list_tuples[j]
            list_tuples [j] =list_tuples[j+1]
            list_tuples [j+1] = temp
print("Result output: ",end="")

print(list_tuples)


# In[27]:


#range 97 to 122
d={}
for i in range(97,123):
   d[chr(i)]=i
print(d)


# In[29]:


import string
print(string.ascii_lowercase)

d={}

for i in string.ascii_lowercase:
    d[i]=ord(i)
print(d)    


# In[34]:


#Functions
def name_function():
    pass
def square(x):
    print(x*x)
def cube(x):
    return x*x*x
print("This")
#standard guidelines---func call after func definition
#if no func call then no func definition
def welcomeMsg(name1,name2):    
    print("Welcome",name1," , ",name2)      
#conventional parameter passing    
welcomeMsg("Sagar","Sarkar")#1  
print("kkk")
square(4)
print(cube(3))  
    


# In[ ]:





# In[38]:


def cube(x):
    a=x*x*x
    return a
#return x*x*x

ans=cube(3)
print(ans)

def cube(x):
    print(x*x*x)
    
ans=cube(3)
print(ans)


# In[40]:


def add(x,y):
    s=x+y
    return s

print(add(3,4))

def add(x,y):
    s=x+y
    print(s)

add(5,6)    


# In[58]:


def welcomeMsg(name1,name2,name3="India"):    
    print("Welcome",name1,name2,name3)      
#conventional parameter passing    
#welcomeMsg("Sagar","Sarkar")
#welcomeMsg("Sagar")#default parameter passing
#positional argument
welcomeMsg("s","Sagar","Sarkar")
welcomeMsg("sagar",name2="Sarkar",name3="S")
#welcomeMsg(name2="Sarkar",name3="S","TCS")
welcomeMsg("sagar",name2="Sarkar")#mixture of all 3 types


def si(p,r,t=3):
    return p*r*t/100


print(si(12000,12,2))
print(si(12000,r=12))
ans=si(12000,r=12)
print(ans)


# In[ ]:




