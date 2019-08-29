#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline #도표 그림, 애니메이션 표현')
import numpy as np #as 이후는 별칭
import random
import matplotlib.pyplot as plt 


# In[14]:


r = []# 여자
b = []# 남자

for i in range(50):
    r.append([random.randint(40, 70),
              random,randint(20,140),
              random,randint(80,105),
              random.randint(140, 180), 1])
    #무게,머리길이,옷 크기, 키,
    
    b.append([random.randint(60, 90),
              random,randint(1,60),
              random,randint(90,120),
              random.randint(160, 200), 0])


# In[15]:


for i in range(50):
    plt.plot(r[i][0], r[i][1], marker='o', color = 'red')
    plt.plot(b[i][0], b[i][1], marker='o', color = 'blue')
    
print("키를 입력해주세요.")
height = int(input())
print("머리길이를 입력해주세요.")
hair = int(input())
print("옷 크기를 입력해주세요.")
size = int(intput())
print("몸무게를 입력해주세요.")
weight = int(input())

new = [weight, height, 0]
print("k의 갯수를 입력해주세요.")
kcount = int(input())

plt.plot(new[0], new[1], marker = 'x', color = 'black')


# In[7]:


def distance(x, y):
    return int(np.sqrt(pow((x[0]-y[0]), 2) + pow((x[1]-y[1]), 2)))


# In[10]:


result = []
for i in range(50):
    result.append([distance(new, r[i]), r[i][2]])
    result.append([distance(new, b[i]), b[i][2]])


# In[11]:


sum = 0.0
for i in range(kcount):
    sum += result[i][1]
avg = sum / kcount

if(avg > 0.5):
    print("당신은 여자입니다.")
else:
    print("당신은 남자입니다.")


# # 뭐야 어떻게 하는거야...
# # 우리 이거 배운거 맞아?

# In[ ]:




