#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
import numpy as np

import matplotlib.pyplot as plt


data = []
for i in range(50):
    data.append([random.randint(40, 70),random.randint(140, 180)])
    data.append([random.randint(60, 90),random.randint(160, 200)])


# In[31]:


# 랜덤 남자, 여자 값
random_points = [[random.randint(40, 90),random.randint(140, 200)],[random.randint(40, 90),random.randint(140, 200)]]
print(random_points)


# In[32]:


for i in data:
    plt.plot(i[0],i[1],'o',color='k')
plt.plot(random_points[0][0],random_points[0][1],'x',color='r')
plt.plot(random_points[1][0],random_points[1][1],'x',color='b')


# In[33]:


tmp1 = []
tmp2 = []


# In[34]:


# 두 점의 거리를 구하는 함수
def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2)


# In[38]:


# 랜덤 점과 다른 점들과 거리를 구해
for k in range(10):
    tmp1 = []
    tmp2 = []
    if (k != 0):
        random_points = new_points

for i in data:
    if (dist(random_points[0],i) > dist(random_points[1],i)):
        tmp2.append(i)
    else:
        tmp1.append(i)    


# In[39]:


for i in tmp1:
    plt.plot(i[0],i[1],'o',color='y')
for i in tmp2:
    plt.plot(i[0],i[1],'o',color='g')
plt.plot(random_points[0][0],random_points[0][1],'x',color='r')
plt.plot(random_points[1][0],random_points[1][1],'x',color='b')


# In[40]:


# 점 이동
sum1=0
sum2=0
for i in tmp1:
    sum1 +=i[0]
    sum2 +=i[1]
    
new_points = []
new_points.append([sum1/len(tmp1),sum2/len(tmp1)])
sum1=0
sum2=0
for i in tmp2:
    sum1 +=i[0]
    sum2 +=i[1]
new_points.append([sum1/len(tmp2),sum2/len(tmp2)])


# In[41]:


for i in tmp1:
    plt.plot(i[0],i[1],'o',color='y')
for i in tmp2:
    plt.plot(i[0],i[1],'o',color='g')
plt.plot(new_points[0][0],new_points[0][1],'x',color='r')
plt.plot(new_points[1][0],new_points[1][1],'x',color='b')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




