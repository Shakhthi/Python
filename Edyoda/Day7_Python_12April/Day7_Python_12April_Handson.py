#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Nested if
maths=int(input())
phy=int(input())
if(maths>40):
    if(phy>40):
        print("Passed in Maths and Phy")
    else:
        print("Passed in Maths but not Physics")
else:
    print("Not passed in Maths but dont know about Physics")


# In[ ]:


s=("madhyapradesh","dehli","goa")

for i in s:
    print(i,sep=",",end=" ")


# In[ ]:


e=0#line 1
def square(a):#line 3
   e=a*a#line 4
   return e#line 5
print(square(4))#line2,line 6
print(e)#line 7


# In[ ]:


maths=int(input())
phy=int(input())
if(maths>40 or phy >40):
    if(phy>40):        
        print("Passed in Phy")
    elif(maths>40):
        print("Passed in Maths")
    elif(maths>40 and phy >40):
        print("Passed in Maths and Physics")
else:
    print("Not passed in Maths and  Physics")


# In[ ]:


#Iterables--Is anything which we can iterate upon 
#String, list , tuples and set-- no function
#.keys function is there in dictionary-- to iterate

s="EdYodaUniversity"

#Way1--diff lines
for a in s:
    print(a)
#Way2--same line
for a in s:
    print(a,end=" ")
#Way3

#string ----   -6-5-4-3-2-1
for a in range(-1,-len(s)-1,-1):
    print(s[a],end=" ")
    
    


# In[ ]:





# In[ ]:


s="EdYodaUniversity"

#Way1--diff lines
for a in s:
    print(a)
#Way2--same line
for a in s:
    print(a,end=" ")
#Way3

for a in range(len(s)):
    print(s[a],end=" ")
    


# In[ ]:



s="EdYodaUniversity"
#len is 16
#-17=-16-1==-17
#start is -1 and end is in -17 step -1
#forward -012345
#backward- -1 -2 -3 -4 -5 -6
for a in range(-1,-len(s)-1,-1):
    print(s[a],end=" ")
    
for i in range(-1,-17,-1):
    print(i)


# In[ ]:


l=["INDIA","USA","CHINA","JAPAN"]

#Way1--diff lines
for a in l:
    print(a)
#Way2--same line
for a in l:
    print(a,end=" ")
#Way3

for a in range(len(l)):
    print(l[a])
    
    
#displa    


# In[ ]:


l=["INDIA","USA","CHINA","JAPAN"]
#for a in range(len(l)):
 #s   print(l[a],end=" ")
#0 1 2 3     
# 3 2 1 0
#display list in reverse

#index start at 0,,,, ends at len-1
for i in range(len(l)-1,-1,-1):
    print(l[i]) 
        


# In[ ]:


#slicing --to cut a component of an iterable
#slice a list---get a list
#slice a string--get a string
#slice a tuple--get a tuple

l=[6,7,8,9,10]

#l[a:b:c]
#a==start==def is 0
#b==stop==def is len--excluded like range
#c==step==def is 1==not compulsory
print(l[:])#0 1 2 3 4 
print(l[1:])# 1 2 3 4 
print(l[1:3])#1 2 


# In[ ]:


s="EdYodaUniversity"

print(s[:4])#0123
print(s[::-1])
print(s[::2])#0 2 4 6 8 10....
print(s[1:9:2])#1 3 5 7 


# In[ ]:


## Returns False as x is False

#bool()-convert the boolean equalivalent of all the datatypes
x = False
print(bool(x))

# Returns True as x is True
x = True
print(bool(x))

# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x == y))

# Returns False as x is None
x = None
print(bool(x))


# In[ ]:


n=input("Take the string to be worked upon")
#n[1:1]--empty string
if(n[1:3]): 
 print("Yess")
else:
 print("Noo")   


# In[ ]:


#break---break out of the loop---cancelled
#continue---skip the iteration

for a in range(10):   
    if(a==5):
        continue
        #it will ignore any state after this line
    print(a)    


# In[ ]:



for a in range(10):   
    if(a==5):
        break
        #it will ignore any state after this line
    print(a)    
print("Loop no more")    


# In[ ]:


f="edyodauniversity"

for i in f:
    if(i in ['a','e','i','o','u']):
        break
        
    else:
        print(i)
        


# In[ ]:


for i in range(6):#012345
    for j in  range(4):#0123
        if(i==j):
            continue
        print("i",i,"j",j)
print('New Output')        
for i in range(6):#012345
    if(i==j):
        break    
    for j in  range(4):#0123
        if(i==j):
            break
        print("i",i,"j",j) 
 


# In[ ]:


students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break
    print(student)
for student in students:
    if student == "kishan":
        continue
    print(student)     


# In[ ]:


t=(5,6,7)
#tuple reassignment is not there but slicing is there
#same with string
te=t[1:]
print(te)
print(id(te))
print(id(t))


# In[ ]:


s="INDIA"
#same with string
se=s[:]
print(se)
print(id(se))
print(id(s))


# In[ ]:


#while loop
for i in range(6):
    print(i)
#when we do not know about the end  number

while(a>0):
    
    print(i)
    i=i-1
    


# In[4]:


a=1#start
while(a<10):#stop cond    
    print(a)
  #step
    a=a+1


# In[12]:


#store the single typesvalues from a list which are having duplicat values
l=[2,3,3,2,3,4,5,6,2]
#-->[2,3,4,5,6]
#no use of set or sort
#using for , if and membership operator
a=[]
for i in l:
    print("current element",i)
    if(i not in a):
        print(i,"Not present in list")
        print("added current element",i)
        a.append(i)        
print(a)

#palindromic seq=== reverse and original is same
#like as nitin , malayalam
s=input()
if(s==s[::-1]):
    print("It is Palindromic")
else:
    print("No it is not")
#palindromic number 
s=int(input())
ns=str(s)
if(str(s)==ns[::-1]):
    print("It is Palindromic")
else:
    print("No it is not")


# In[ ]:


#pseudo code --step by step--common for any lan-interview

#coding test--code should be fine


# In[23]:


#3 more questions
s="EDYODA"
if(bool(s[-1:-5])):
    print(bool(s[1:2]))
    
#Finding the highest frequency member in a list

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
maxvalue=0
#d.keys --list of keys
for i in d.keys():    
    if(maxvalue<d[i]):
        
        maxvalue=d[i]
print(maxvalue)            


# In[ ]:


#count----- in list 

