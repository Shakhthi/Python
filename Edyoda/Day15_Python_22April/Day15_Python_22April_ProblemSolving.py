#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Ques1
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]

#A1

if("".join(word1))=="".join(word2):
    print("True")
    
else:
    print("False")
    
#A2
w1=""
w2=""
for i in word1:
    w1=w1+i
for i in word2:
    w2=w2+i    
print(w1==w2)    


# In[10]:


#Q2

words = ["leetcode","win","loops","success"]
pref = input()
c=0
for i in words:
    if(i.startswith(pref)):
        c=c+1
print(c)        


# In[12]:


word1 =["ab" , "c"]
word2 = ["a","bc"]

if ("".join(word1)) == ("".join(word2)):
        print("true")
else:
    print("false")


# In[14]:


#Q3

nums1 = [1,2,2,1]
nums2 = [2,2]

print(list(set(nums1).intersection(set(nums2))))


# In[15]:


#Q4

s = "Hello how are you Contestant"
k = 4
ls=s.split(" ")
als=ls[:k]
print(" ".join(als))


# In[19]:


#Q6
s = "   fly me   to   the moon  "
sl=s.split(" ")
print(sl)
wl=[]
for i in sl:
    if(i!=""):
        wl.append(i)        
print(wl)   
print(len(wl[-1]))


# In[25]:


#List comprehension

l=[2,3,4]
numbers= [i*5 for i in range(1,11)]
print(numbers)


# In[27]:


#Q5

nums = [1,2,3,2]

a=[]
sumi=0
for i in nums:
    if(nums.count(i)==1):
        #a.append(i)
        sumi=sumi+i  
#print(sum(a))
print(sumi)


# In[28]:


#Q7
nums1 = [1,2,3]
nums2 = [2,4,6]

a=[]
a.append(list(set(nums1)-set(nums2)))
a.append(list(set(nums2)-set(nums1)))
print(a)


# In[30]:


sentence = "thequickbrownfoxjumpsoverthelazydog"

print(len(sentence))
if(len(set(sentence))==26):
    print("Yess")
else:
    print("Noo")
c=0   
for i in set(sentence):
    if(ord(i)>=97 and ord(i)<=122):
        c=c+1
        
if(c==26):
    print("Pangram")
else:
    print("Non Pangram")


# In[ ]:




