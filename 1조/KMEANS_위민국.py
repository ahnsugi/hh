#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random # 랜덤함수 호출
import numpy as np 
import matplotlib.pyplot as plt 

data = [] #데이터 리스트
for i in range(50): # 반복문
    data.append([random.randint(40, 70),random.randint(140, 180)]) # 여자(몸무게,키)
    data.append([random.randint(60, 90),random.randint(160, 200)]) # 남자(몸무게,키)


# In[19]:


print(data) #데이터의 랜덤 좌표값 100개 남자50,여자50


# In[20]:


random_points = [[random.randint(40, 90),random.randint(140, 200)],[random.randint(40, 90),random.randint(140, 200)]]
print(random_points) #새로운 좌표 두개 생성


# In[21]:


for i in data: #data 반복문
    plt.plot(i[0],i[1],'o',color='k') #
plt.plot(random_points[0][0],random_points[0][1],'rx')#위에 좌표 하나를 "빨간색 x"로 표시
plt.plot(random_points[1][0],random_points[1][1],'bx')#위에 나머지 좌표를 "파란색 x"로 표시


# In[22]:


tmp1 = []#팀을 나누기 위함
tmp2 = []


# In[23]:


def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2)#함수 두점 사이의 거리 구하는 공식


# In[24]:


for i in data:
    if (dist(random_points[0],i) > dist(random_points[1],i)):#두점중에 가까운 것으로 추가 / tmp1,2
        tmp2.append(i)
    else:
        tmp1.append(i)


# In[25]:


for i in tmp1:
    plt.plot(i[0],i[1],'o',color='y')
for i in tmp2:
    plt.plot(i[0],i[1],'o',color='g') 
    #편 나누기 색깔별로.
plt.plot(random_points[0][0],random_points[0][1],'rx') 
plt.plot(random_points[1][0],random_points[1][1],'bx')


# In[26]:


# 점 이동
sum1=0 #평균값을 구하기 위함
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


# In[27]:


print(new_points) # 평균값 


# In[28]:


for i in tmp1:
    plt.plot(i[0],i[1],'o',color='y')
for i in tmp2:
    # 다시 편가름 가까운 것으로
    plt.plot(i[0],i[1],'o',color='g')
plt.plot(new_points[0][0],new_points[0][1],'rx')
plt.plot(new_points[1][0],new_points[1][1],'bx')


# In[32]:


#전체코드

#1. 거리 구하는 공식
def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2)

#2. 랜덤 값 넣고. 새로운 좌표값 만들기
data = []
for i in range(50):
    data.append([random.randint(40, 70),random.randint(140, 180)])
    data.append([random.randint(60, 90),random.randint(160, 200)])
random_points = [[random.randint(40, 90),random.randint(140, 200)],[random.randint(40, 90),random.randint(140, 200)]]

#3. 10번 반복한다.
for k in range(10): 
    tmp1 = []
    tmp2 = []
#4. 편 나누기
    if(k != 1): random_points = new_points
    for i in data:
        if (dist(random_points[0],i) > dist(random_points[1],i)):
            tmp2.append(i)
        else:
            tmp1.append(i)
#5. 편 나눈것 모두 더하기
    sum1=0
    sum2=0
    for i in tmp1:
        sum1 +=i[0]
        sum2 +=i[1]
#6. 편 나눈것의 평균값을 구해 새로운 포인트에 넣기.
    new_points = []
    new_points.append([sum1/len(tmp1),sum2/len(tmp1)])
    sum1=0
    sum2=0
    for i in tmp2:
        sum1 +=i[0]
        sum2 +=i[1]
    new_points.append([sum1/len(tmp2),sum2/len(tmp2)])

#7. 다시 그리기
for i in tmp1:
    plt.plot(i[0],i[1],'o',color='y')
for i in tmp2:
    plt.plot(i[0],i[1],'o',color='g')
plt.plot(new_points[0][0],new_points[0][1],'rx')
plt.plot(new_points[1][0],new_points[1][1],'bx')


# In[ ]:




