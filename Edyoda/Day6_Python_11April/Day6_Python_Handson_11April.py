#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#list of true values--apart from False Values
#false values list--0,None,[],(),{} ,""
#IF  example
age=int(input())
if([3,3]):
    print("Eligible to Vote")
#t should be true or false value
#fortunately in python everything has an equivalent of true and false


# In[ ]:


56


# In[3]:


age=int(input())
if(age>18):
    print("Eligible to Vote")
    
    


# In[ ]:


#list of true values--apart from False Values
#false values list--0,None,[],(),{} ,""


# In[6]:


age=int(input())
if(age>=18):
    print("Eligible to Vote")
else:#we never mention any other condition
    print("Not Eligible to Vote")  
    
    


# In[13]:


Marks=int(input("Enter your Marks"))
#if elif else --to be used for more than 2 options
if(Marks>=90):#we can mention the cond here  
    print("A Grade")
elif(Marks>=80 and Marks<90): #we can mention the cond here
    print("B Grade")    
elif(Marks >=70 and Marks<80):
    print("C Grade")
elif(Marks >=60 and Marks<70):
    print("D Grade")        
else:
    print("Reattempt")    


# In[19]:


state = input()
if (state=="UP") :
    print("The state is UP")    
   #dont mention any other condition
else:
    print("The State is not UP")


# In[20]:


#Nested If else condition

#What is importance of Scope??

#Visibility

a=89
if(a>50):
    sum=1
print(sum)


# In[24]:


#func to return the square of num==input is a num , out is a square of it


# In[7]:


rollno=int(input())
ctry=input()
if(rollno>0):
    if(ctry=="INDIA"):
        print("Yess")
    else:
        print("inner else")
else:
    print("Outer Else")         
#first comp is for rollno
#sec comp is for ctry
#then print


# In[5]:


rollno=int(input())
ctry=input()
if(rollno>0 and ctry=="INDIA"):
        print("Yess")
        
#both rolno and ctry is comp simultenously        


# In[ ]:





# In[10]:


Maths=int(input())
Phy=int(input())
if(Phy>80):
    if(Maths>80):
        print("Scholar")        
    else:
        print("Done Well")
else:
    print("Can do better")  


# In[11]:


#basics of for loop
for i in range(1,6,2):
    print(i)


# In[12]:


s="EDYODA"

for j in s:
    print(j)


# In[13]:


n=int(input("How many elements in a list"))
l=[]
for j in range(n):
    a=input()
    l.append(a)
    
print(l)    


# In[21]:


n=int(input("How many elements sum"))
sumi=0
for j in range(n):
    if(j%2==0):
     print(j)
     sumi=sumi+j    
print("Sum is ",sumi)    


# In[ ]:


#indentation in python is similar to braces in java

a=9
print(a)
b=8
print(b)
c=7
print(c)   
print("Outer")


# In[29]:


#short hand If else operator
a=9
if (a==8):  print("Yess")
elif(a==9): print("Edy")        
else : print("Edyoda")    


# In[ ]:




