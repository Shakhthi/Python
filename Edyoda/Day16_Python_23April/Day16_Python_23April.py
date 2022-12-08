#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q9
nums = [3,2,1,5,4]
k = 2
c=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(abs(nums[i]-nums[j])==k):
            c=c+1            
print(c)            


# In[6]:


#Q12

word = "abcd"
ch = "z"
a=word.find(ch)
if(a==-1):
    print(word)
else:
    os=word[:a+1][::-1]+word[a+1:]
    print(os)


# In[12]:


#Q13

text = "leet code trrrr"
brokenLetters = "e"
#A1
lb=list(brokenLetters)
lw=text.split(" ")
print(lw)
print(lb)
c=0
for i in lw:
    if(set(i).intersection(set(brokenLetters))):
        pass
    else:
        c=c+1
print(c)        


# In[17]:


#Q14

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"

sl=s.split(" ")
print(sl)
nl=[]
for i in sl:
    if(i.isnumeric()):
        nl.append(int(i))
print(nl)        
if(nl==sorted(nl)):
    print("True")
else:
    print("False")    


# In[18]:


#Q15

arr = ["d","b","c","b","c","a"]
k = 2
u=[]
for i in arr:
    if(arr.count(i)==1):
        u.append(i)
print(u[k-1])        


# In[19]:


#Q9

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
d=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if(abs(arr[i] - arr[j])<= a and abs(arr[j] - arr[k])<= b and abs(arr[i] - arr[k])<= c):
                d=d+1
print(d)                


# In[ ]:




