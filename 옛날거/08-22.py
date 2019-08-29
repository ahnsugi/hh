#!/usr/bin/env python
# coding: utf-8

# # 4.1 NumPy ndarray : 다차원 배열 객체

# In[1]:


import numpy as np


# # 4.1.3 nd array 생성

# In[2]:


data1=[6,7.5,8,0,1]


# In[3]:


arr1 = np.array(data1)


# In[4]:


arr1


# In[6]:


type(arr1)


# In[7]:


type(data1)


# In[8]:


data2=[[1,2,3,4],[5,6,7,8]]


# In[14]:


# ㅣ = 리스트, n = npararray


# In[9]:


l  = [[1,2,3],[4,5,6]]
l2 = [[1,2,3],[4,5,6]]
n = np.array(l)
n2 = np.array(l)


# In[10]:


print(l)
print(n)


# In[11]:


print(n + n2)


# In[12]:


print(n*2)


# In[13]:


print(l*2)


# In[15]:


import numpy as np


# In[16]:


r = [4,2,1]
b = [5,1,0]


# In[18]:


r1 = np.array(r)
b1 = np.array(b)


# In[21]:


print(r)
print(b)

print(r1)
print(b1)


# In[44]:


samples = np.random.normal(size=(8,3))


# In[45]:


print(samples)


# # ※ KNN 실습

# In[25]:


import matplotlib.pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# In[76]:


pit.plot([1,2,3,4],[1,2,3,4])


# In[66]:


pit.plot(1,2,marker='o', linestyle='',color='red')
pit.plot(1,3,marker='o', linestyle='',color='red')
pit.plot(2,2,marker='o', linestyle='',color='blue')


# In[65]:


pit.plot(samples, linestyle='')


# # 내가 한 것

# In[129]:


for i in range(0,50):
    sample1 = np.random.normal(1)
    sample2 = np.random.normal(1)
    
    if(i % 2 == 0):
        cir = 'red'
    else:
        cir = 'blue'
    
    pit.plot(sample1,sample2, marker = 'o', color = cir)


# # 교수님 하신거

# In[215]:


import random


# In[216]:


r = [] #여자 1
b = [] #남자 2
for i in range(50):
    r.append([random.randint(40,70),random.randint(140,180),1])
    b.append([random.randint(60,90),random.randint(160,200),0])


# In[214]:


for i in range(50):
    pit.plot(r[i][0], r[i][1], marker ='o', color = 'red')
    pit.plot(b[i][0], b[i][1], marker ='o', color = 'blue')
    
new = [55,170,1] # 여자
pit.plot(new[0],new[1],marker='x',color='black')


# # 거리 구하는 함수

# In[133]:


dist = np.sqrt(
    pow((new[0]-r[0][0]),2)
    +pow((new[1]-r[0][1]),2)    
)


# In[134]:


print(dist)


# In[137]:


def distance(x,y):
    return int (np.sqrt(pow((x[0]-y[0]),2) +pow((x[1]-y[1]),2)))


# In[139]:


distance (new, r[0])


# In[142]:


result = []
for i in range(50):
    result.append([distance(new, r[i]), r[1][2]])
    result.append([distance(new, b[i]), b[1][2]])


# In[152]:


result.sort()
print(result)


# # 1. 키를 입력해주세요
# 
# # 2. 몸무게를 입력해주세요
# 
# # 3. K의 개수를 입력해주세요
# 
# # #. 당신은 남자 혹은 여자입니다.

# In[ ]:





# In[235]:


def distance(x,y):
    #주 점 사이의 거리를 구하는 함수
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2))

def knn(x,y,k):
    result = []
    cnt = 0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[1][2]])
    result.sort()
    for i in range(k):
        if(result[i][1]==1):
            cnt +=1
    if(cnt > (k/2)):
        print("당신은 여자입니다.")
    else:
        print("당신은 남자입니다.")


# In[236]:


weight = input("몸무게를 입력해주세요. ")


# In[237]:


height = input("키를 입력해주세요. ")


# In[238]:


num = input("k를 입력해주세요. ")


# In[239]:


new = [int(weight), int(height)]


# In[240]:


knn(new, r+b, int(num))


# In[ ]:





# In[ ]:




