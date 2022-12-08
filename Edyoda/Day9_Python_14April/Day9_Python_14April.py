#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1Find words which are greater than given length k

#1--take input of int
#2--split the sentence
#3--iterate and find length
#4---use if condition
stri = "hello geeks for geeks is computer science portal" 
k=int(input())
#print(list(stri))
l=stri.split(" ")
print(l)
a=[]
#for i in range(len(l))
for i in l:
    if(len(i)>k):
        a.append(i)       
print(a)        


# In[8]:


#Q6 Find whether a word is symmetrical or not
#ex of symm---amaama==ama___ama---divide into two parts --both are same
#palindromic--nitin---forward and backward---same sequence
s=input()
#easiest way --slicing...

#odd length string can never be symmetrical
#even length maybe symmetrical
n=len(s)
if(n%2!=0):
    print("Not Possible")

#left--[0:n]
#right--[n:]
middle=int(n/2)


#/--float
if(n%2==0):
    
 lefts=s[0:middle]
 rights=s[middle:]
else:
    print("Symmetrical not possible")
print(lefts)
print(rights)
if(lefts==rights[::-1]): 
#if(rights==lefts[::-1])    
 print("Symmetrical")


# In[9]:


#Q3

s="14,625,498.002"
#1--iterate through the string
#2--replace . with ,
#3--replace  , with .
#4 dont replace any other charcters
a=""
for i in s:
    if(i=="."):
        a=a+","
    elif(i==","):
        a=a+"."
    else:
        a=a+i        
print(a)


# In[10]:


#Q7--
#1 split--into list of strings
#2 reverse--reverse of list 
#3 join--join using space--list components into string
#1
s=input()
ls=s.split(" ")#list of strings
#2
rsl=ls[::-1]#reverse list of strings
#3
fs=" ".join(rsl)#list of strings into string with a sep.
print(fs)


# In[15]:


#Q2--reverse sort a string
s="sagar"#input
sortstring=sorted(s)#sorted in ascending order
a=sortstring[::-1]#revese
print("".join(a))#join convert list into string
l=[3,9,12,76,34]
#just reverses[::-1]
#2,65,23,22---slicing--22,23,65,2
print(sorted(l))#ascend
print(sorted(l,reverse=True))#descending


# In[18]:


l=[3,9,12,22,34]
print(sorted(l))

print(sorted(l,reverse=True))


# In[24]:


#Revision--if else
age=int(input())
if(age>=18):
    print("Eligible to Vote")
elif(age<0):
    print("Age Data is wrong")
else:
    print("Not Eligible to Vote")


# In[29]:


#Revision-for 
#iterables--gives you the elements from a collection ex list , string and tuple
#1--iterate through collection
l=[4,5,6,7,8]
for i in l:#element wise access
    print(i)
for i in range(len(l)):#index accessing
    print(l[i])
s="EdYoda"
for i in s:#element wise access
    print(i)
for i in range(len(s)):#index accessing
    print(s[i])
t=(7,8,9,10)
for i in t:#element wise access
    print(i)
for i in range(len(t)):#index accessing
    print(t[i])


# In[26]:


age = 15
if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")
print("thank you") 


# In[32]:


#While Loop

a=10#start
while(a>0):#stop/end
    print(a)
    
    a=a-1#step
    if(a==7):
        break   
#break -- stop the loop


# In[37]:


#break , continue and pass

for i in range(2,10):
     if(i==4):
      continue
     if(i==7):
      pass
        
     print(i)


# In[48]:


#count of odd and even in a range

#1--traverse
#2--count odd
#3--count even
odd=0
even=0
for i in range(1,51):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print(odd,even)


# In[60]:


s="RoyalChallengersBangalore"

print(s[::-1])
print(s[2:2])
print(s[1:7])
print(s[1:4:8])
print(s[-3])#not slice but index
print(s[:5])
print(s[7:])
print(s[4:-4])


# In[ ]:


# if you know when to start , when to stop and how to proceed use loop
#for  and while


# In[63]:


l=[1,2,3,4,5,6,7,8,9]   
print(*l)
#print(type(*l))
l.append(10)


# In[ ]:




