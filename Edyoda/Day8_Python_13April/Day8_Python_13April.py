#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
s=input()
print(len(s))
count=0
for i in s:
    if i !=" ":
        count=count+1
#count+=1  
#count++
print(count)        
"""
for i in s:
    if i ==" ":
        continue
    else:
        count=count+1
        
"""        


# In[4]:


#Q2
#Python program for removing i-th character from a string
#Given the string, we have to remove the ith indexed character from the string.
s=input()
n=int(input())
a=""
for i in range(len(s)):
    if(i!=n):
        a=a+s[i]        
print(a)

#slicing way

a=s[:n]+s[n+1:]

#Sagarsar
#3
#ans---Sagrsar


# In[8]:


#Q3Python | Check if a given string is binary string or not

#Binary only has 0 or 1

s=input()

for i in s:
    if i not in ['0','1']:
        print("It is not binary")
        break  


#pass- is a keyword  which works like a space filler no func as it os


# In[ ]:





# In[3]:


a=0
if(a>9):
    print("yy")    
else:
    pass


# In[6]:


#Q3Python | Check if a given string is binary string or not

#Binary only has 0 or 1
s=input()
flag=0  # not a keyword      
for i in s:
    if i not in ['0','1']:
      #if i!='0' and i!='1':  
        flag=flag+1
    else:
        pass
if(flag>0):
    print("Not a binary string")
else:
    print("binary string")


# In[8]:


#Q4Python program to swap two elements in a list
#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
l=[2,6,1,7,3,9,8]
print(len(l))
n1=int(input())#1st
n2=int(input())#3rd
a=l[n1]#a=1st value
l[n1]=l[n2]#1st index=3rd value
l[n2]=a#3rd index=a
print(l)


# In[11]:





# In[12]:


# never ever remember
#Remove common elements from two list in Python
#Given two lists, the task is to write a Python program to remove all the common elements of two lists. 
l1=[6,7,2,3,5,11]
l2=[2,3,4,5]
#remove method--used to remove the element from the list
for i in l1:
    if i in l2:     
       l1.remove(i)       
       l2.remove(i)
       print(l1,l2)
    else:
        continue
    
    
    
    
#print(l1,l2)
#Test cases


# In[3]:


s="I study from Edyoda"

s=s.split(" ")#-----listof strings-["I","study",....]
a=[]
for i in s:
    if(len(i)%2==1):#!=
        a.append(i)
        
print(a)        


# In[4]:




x = [3, 5, 3, 4, 7]
y = [4, 3, 6, 7, 8]

for i in x:
	if i in y:
		x.remove(i)
		y.remove(i)

print("list1 : ", x)
print("list2 : ", y)


# In[8]:


#Q10Python | Count the Number of matching characters in a pair of string
s1="engineer" 
s2="manager"
ss1=set(s1)
ss2=set(s2)
print(ss1,ss2)
count=0
for i in ss1:
    if i in ss2:
        count=count+1        
print(count) 

#set to remove the duplicacy


# In[9]:


s1 = "listen"
s2 = "silent"
#
ss1=set(s1)
ss2=set(s2)

if(ss1==ss2):
    print("Yes")


# In[ ]:


a=[1,2,3,2]

#uniqueee
u=[]
for i in a:
    if i not in u:
        u.append(i)
        
print(u)
sumn=0
for i in u:
    sumn=sumn+i
print(sumn)    


# In[15]:


l=[2,3,2,3,4,5,6,3]#3
#dictionary---ke would be value and value would be the freq
d={}
#1st iteration--d={2:1}
#2nd iter--d={2:1,3:1}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
        
print(d) 
#max--helps you to find the highest value
#2,3,4,5,6
#max freq member
#maxa=max(collection, key)
maxa=max(d,key=d.get)
print(maxa)
mina=min(d,key=d.get)
print(mina)
l=[2,3,2,3,4,5,6,3]
print(max(l))
print(min(l))
l=[2,3,2,3,4,5,6,3]
suma=sum(l)
print(suma)


# In[16]:


print(len)


# In[17]:


help(min)


# In[19]:


#calculator

num1=int(input("Enter your first value: "))
num2=int(input("Enter your second value: "))
print("choose the operand below---")

print("your operand are--> +,-,/,*,//,%")
n=input("Enter your operand: ")

if n=="+":
    print(num1+num2)
elif n=="-":
    print(num1-num2)
    
elif n=="/":
    print(num1/num2)
    
elif n=="*":
    print(num1*num2)
    
elif n=="//":
    print(num1//num2)
    
elif n=="%":
    print(num1%num2)
    
else:
    print("wrong input!")


# In[ ]:




