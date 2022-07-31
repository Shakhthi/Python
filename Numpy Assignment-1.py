#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ### 1. Create a null vector of size 10 but the fifth value which is 1.
# 

# In[5]:


null_vector  = np.zeros(10, dtype='int8')
null_vector[4] = 1
print(null_vector)


# ### 2. Create a vector with values ranging from 10 to 49.
# 
# 

# In[108]:


a,b = input(" Enter the Low and High of the  Vector range ").split(",")
vec1 = np.random.randint(10,50,size=(int(a),int(b)))
vec = vec1.ravel().copy()

print( " Vector of the Specified Range: ", vec)


# ### 3. Create a 3x3 matrix with values ranging from 0 to 8
# 

# In[40]:


array1  = np.arange(9).reshape(3,3)
print(array1)


# ### 4. Find indices of non-zero elements from [1,2,0,0,4,0]
# 

# In[53]:


vec2 = np.array([1,2,0,0,4,0])
l = []
for i in range(len(vec2)):
    if vec2[i] != 0:
        l.append(i)
    else:
        pass
print(" The Non-Zero Elements Indices: ", *l)    
        


# ### 5. Create a 10x10 array with random values and find the minimum and maximum values.
# 

# In[107]:


#np.random.seed(4)

array2 = np.random.randint(1,1000,size=(10,10))
print(array2)

print(array2.min()) 
print(array2.max())


# ### 6. Create a random vector of size 30 and find the mean value.
# 

# In[106]:


vec3 = np.random.ranf(30)*100
print(vec3.round())
print( " Mean of the Array: ",vec3.mean())


#print(np.average(vec3))


# In[ ]:




