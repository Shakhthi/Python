#!/usr/bin/env python
# coding: utf-8

# In[3]:


t=(1,2,[3,4])
print(t)
t[2].append(5)
#t[2]=[8,9]
print(t)


# In[6]:


l=[1,2,(8,9)]
print(l)
l[2]=l[2]+(2,3)
print(l)


# In[7]:


s=input()

print(len(s))
#len==4
#0 1 2 3--3 2 1 0

a=""
for i in range(len(s)-1,-1,-1):
    a=a+s[i]
    
print(a)    



# In[9]:


n=int(input())
odd=0
even=0
for i in range(1,n+1):
  if(i%2!=0):  
    
    odd=odd+1
  else:
    even=even+1
    
print(odd)
print(even)
    


# In[11]:


#0 1 1 2 3 5 8.....50

x,y=0,1
#print(x)
while y<50:

    print(y)
    x,y = y,x+y


# In[13]:


x,y=0,1
print(x)
while y<50:

    print(y)
    x,y = y,x+y


# In[ ]:


Totalterms = int(input("How many terms? "))

a = 10
b = 11
num = 4

if Totalterms <= 0:
   print("Please enter a positive integer")
elif Totalterms == 1:
   print("Fibonacci sequence upto",Totalterms,":")
   print(a)

else:
   print("Fibonacci sequence:")
   while num < Totalterms:
       print(a)
       z = a + b
       
       a = b
       b = z
       num += 1


# In[15]:


a=0
b=1
print(b,end=' ')
for i in range(2,10):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    
    

    


# In[20]:


#Center

s=input()

a=s.center(30,"*")

print(a)


# In[23]:


s=input()
print(s.isidentifier())


# In[30]:


a=input()

print(a.zfill(20))


# In[40]:


s=input()
print(s.strip("*"))
print(s.lstrip("*"))
print(s.rstrip("*"))


# In[43]:


s=input()
result = s.rindex('1')
print(result)


# In[48]:



s=input()
print(s.rjust(13,"*"))
print(s.ljust(13,"*"))
print(s.center(13,"*"))


# In[51]:


s=input()
print(s.replace("E", "e",2))


# In[52]:


string = "pawan is a good"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('bad '))


# In[ ]:




