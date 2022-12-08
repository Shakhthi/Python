#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Single Line comment


# In[2]:


# Print
print("INDIA")


# In[3]:


'''
This is a multi line comment
This is EdYOda classroom 

'''
print("EdYoda")


# In[4]:


a="India"
b=a+"Republic"
print(int(b))


# In[5]:


a="India"
b=a+"Republic"
print(String(b))


# In[6]:


a="India"
b=a+"Republic"
print(str(b))


# In[8]:


for i in range(2,10,-1):
 print(i,sep=" ")


# In[9]:


for i in range(2,10,-1.5):
 print(i,sep=" ")


# In[10]:


a=input("Enter your age")
print(float(a))


# In[15]:


a=[]
b=input("Enter the values of the list")
#user must give the input to the console in comma sepearted values
#like 3,4,5,6-----[3,4,5,6]

#split function
# typecasted string to list datatype
#split output datatype is list
#inputvariable.split("seperator")---syntax of split function
a=b.split(".")
print(a)


# In[22]:


l=["A","B","C","D"]
#l is a list
# join function to create a string from list of string
#Seperator.join(list)
#charcter between the values in string
print("#".join(l))


# In[34]:


a=input("Enter the roll no")
print("This is my roll number",int(a))
# store the digits of a roll number in a list
#lis=a.split("")
#print(lis)
# using for loop  to access the elements of string
print(type(a))
l=[]
for i in a:
    l.append(i)
    print(l)
    print(i)    
  


# In[29]:


lis=["Sagar",33,56.6,33]
# using for loop  to access the elements of list
for i in lis:
  print(i,end=" ")


# In[30]:


s="NewDelhi"
# using for loop  to access the elements of string
for i in s:
  print(i,end=" ")


# In[35]:


#append helps to add a list member into a list

l=[1,2,3,4]

l.append(5)


# In[38]:


#I want to generate a new string from and old string which will not contain repeated values
#"sagar"-----"sgar"
# conversion from string to set and again back to string
s=input()
sets=set(s)
#conversion from string to set 
nrs=str(sets)
print(nrs)

#conversion from set to string 

#no surety of order ...


# In[40]:


# how to enter values in a tuple ??

#we cannot mutate a tuple

t=(3,4,5)
t.append(6)
print(t)


# In[41]:


a=input()
b=a.split(",")

t=tuple(b)
print(t)
print(type(t))


# In[44]:


l=[]
#this is the way of declaring an empty list
a=int(input("How many elements do want in a tuple"))
for i in range(a):
    print(i,"term")
    e=input()
    l.append(e)
t=tuple(l)    
print(t,type(t)) 


# In[47]:


l=[]
#this is the way of declaring an empty list
# how to convert tuple into list

a=int(input("How many elements do want in a tuple"))
for i in range(a):
    print(i,"term")
    e=input()
    l.append(e)
t=tuple(l)    
print(t,type(t)) 

listlast=list(t)
n=int(input("Enter the new numbers to be added into the list"))
for i in range(n):
    print(i,"term")
    e=input()
    listlast.append(e)
print(listlast,type(listlast))
print(tuple(listlast),type(tuple(listlast)))


# In[52]:


#append example

l1=[2,3,4]
l2=[9,5,6]
print(l1+l2)

# type operation
s1="Elon"
l=['M','8','s','k']

for i in l:
    s1=s1+i
    
print(s1) 


# In[53]:


l1=[2,3,4]

l2=[4,5,6]
# I want to find out the list of elements which are present in l1
#but not in l2

diffset=set(l1)-set(l2)

print(list(diffset))


# In[55]:


s1= "Elon"
l = ['M','8', 's', 'k']
for i in l:
    s1 = s1+i
    print("Current value of s1",s1)
    
print(s1)        
#Why am I getting Elonk as output


# In[58]:


numbers = range(5)
print(numbers)
for j in range(5):
    print(j)
#range generates a sequence of numbers one by one not a list of numbers
numbers = range(1 , 5 , 2)
print(numbers)
for j in range(1,5,2):
    print(j)


# In[60]:


x= int(input("enter x")) 
y = int(input("enter y")) 
for i in range(x,y,2):
    print(i)
 


# In[ ]:


dicti={rollno:}


# In[62]:


a=98
b=9.67
#implicit type conversion
print(a+b)
#explicit type conversion
print(float(a)+b)


# In[65]:


a=2
b=5
c=str(a)+str(b)
print(c)
print(type(c))
#str +str===25
#int +Int===7
print(a+b)


# In[ ]:




