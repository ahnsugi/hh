#!/usr/bin/env python
# coding: utf-8

# ## 약 인공지능 - 입력해준 데이터 안에서 판단하는 인공지능
# ## 강 인공지능 - 완전히 스스로 사고하는 인공지능
# 
# ## 기존코드 - 프로그래머가 모든 절차를 코딩한다
# ## 인공지능 - 입력한 데이터에서 스스로 모델의 가중치를 설정해 판단한다
# 
# ## 기계학습 -지도학습(Supervised Learning)  vs  자율학습(Unsupervised Learning)
# #### 지도학습 - 이것은 고양이다 이것은 강아지다하는 식으로 모든 데이터를 일일이 입력
# #### 자율학습 - 임의의 군집을 주고 무엇이 고양이이고 강아지인지 스스로 찾도록 한다
# 
# 

# ### 인공지능에 중요한 요소
# - 데이터
# 
# ## 지도학습 인공지능의 종류
# 
# ### 분류(Classification)
# - 수많은 데이터를 컴퓨터가 학습하게 하고 학습한 데이터에 의해 판단
#   ex) 스팸메일
# 
# ### 예측(Regression)
# - 회귀분석
# - 여러 데이터에서 하나의 함수를 추출
# - 목적값의 연속석을 판단
# - 함수를 기반으로 새로운 데이터를 예측할 수 있다

# ### 지도학습 모델
# 1) 무엇을 분석할 것인가?
# - 키와 몸무게의 상관관계
# 
# 2) 분석을 위한 준비
# - 키와 몸무게 등 요소
# - 데이터 수집 범위
# - 언제 어디서?
# 
# 3) 데이터 준비
# - 한국인을 한정
# - 한국인의 키
# - 한국인의 몸무게
# - 크롤링 등으로 자료수집

# ## 지도학습 - KNN
# #### 새로운 음악의 장르는 어떤것인가?
# - 음악 장르는 정확한 기준이 없음
# - 경험적 판단에 의해 결정함
# - 기존에 구분된 장르를 분석하여 판단
# - 아티스트, 재생시간, 비트 수 등을 컴퓨터가 학습하여 판단
# 
# ### KNN = K Nearest Neighbors
# - 임의의 데이터에 대하여 근접한 값을 찾아내는 알고리즘
# - 어떤 데이터가 들어왔을 때, 주변 좌표에 있는 k개 데이터를 통해 값을 판단한다
# 
# #### 장점
# - 정확도가 높다
# - 오류 데이터가 크게 영향을 주지 않는다
# 
# #### 단점
# - 느리다(모든 데이터를 비교해야 함)
# - 기존 데이터가 많을수록 더욱 느려짐
# - 처리시간이 계속 증가함
# - 많은 메모리를 사용함
# - 고사양의 하드웨어가 필요함

# ## 알고리즘
# - d = sqrt((x1^2 - x2^2)+(y1^2-y2^2))
# - random으로 점을 찍는다
# - 데이터를 입력받는다
# - 기존 데이터들과 d를 구한다
# - 가장 가까운 데이터 3개를 뽑는다
# - 데이터가 어떤 값인지 판단한다
# 
# 

# ## NumPy ndarray: 다차원 배열 객체 - 파이썬의 존재의의

# In[2]:


import numpy as np


# ## ndarray 생성

# In[3]:


data1 = [ 6, 7.5, 8, 0, 1]


# In[4]:


arr1 = np.array(data1)


# In[5]:


arr1


# In[6]:


type(arr1)


# In[7]:


type(data1)


# In[8]:


data2 = [[1,2,3,4], [5,6,7,8]]


# In[11]:


l = [[1,2,3,], [4,5,6]]
l2 = [[1,2,3,], [4,5,6]] 
n = np.array(l)
n2 = np.array(l2)


# In[10]:


print(l)
print(n)


# In[12]:


print (l2)
print(n2)


# In[17]:


l3 = l+l2
print(l3)


# In[18]:


n3 = n+n2
print(n3)


# In[19]:


print(n*2)


# In[20]:


print(l*2)


# #### red = (x, y, 1)
# #### blue=(u, v, 0)

# In[21]:


r = [4,2,1]
b = [5,1,0]


# In[22]:


r1 = np.array(r)
b1 = np.array(b)


# In[23]:


print(r1)
print(b1)


# In[25]:


samples = np.random.normal(size=(4,4))  #numpy로 4x4 정규분포 배열을 생성한다
print(samples)


# ## 그래프를 그리는 라이브러리

# In[26]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


plt.plot(r, b)


# In[28]:


plt.plot(1,2, marker = 'o', linestyle='', color = 'red')
plt.plot(3,2, marker = 'o', linestyle='', color = 'red')
plt.plot(4,3, marker = 'o', linestyle='', color = 'blue')


# In[65]:


r = [[170, 80, 1], [180, 60, 1], [190, 100, 1], [165, 60, 1], [185, 75, 1], [173, 68, 1],[182, 55, 1], [169, 95, 1],[171, 80, 1], [140, 50, 1]]


# In[31]:


len(r)


# In[66]:


b = [[130, 46, 0],[160, 57, 0], [150, 45, 0], [145, 55, 0], [170, 65, 0], [163, 60, 0], [159, 55, 0], [190, 60, 0], [177, 54, 0], [165, 70, 0]]


# In[33]:


len(b)


# In[34]:


for i in range(0, 10):
    plt.plot(r[i][0], r[i][1], marker = 'o', linestyle='', color = 'red')
    plt.plot(b[i][0], b[i][1], marker = 'o', linestyle='', color = 'blue')


# In[70]:


data = r+b
print (data)
len(data)


# In[71]:


point = [165, 80, 0]
plt.plot(point[0], point[1], marker = 'o', linestyle='', color = 'green')
for i in range (0, 20):
    if (data[i][2] == 1):
        plt.plot(data[i][0], data[i][1], marker = 'o', linestyle='', color = 'red')
    else:
        plt.plot(data[i][0], data[i][1], marker = 'o', linestyle='', color = 'blue')
        


# In[72]:


data2 = np.array(data)
print(data2)


# In[73]:


data2 = data2 - point


# In[74]:


print(data2)


# In[75]:


data2 ** data2


# In[81]:


distance = []
for i in range(0, 20):
    distance.append([data2[i][0]*data2[i][0] +data2[i][1]*data2[i][1], data2[i][2]] )
print(distance)


# In[82]:


sorted(distance)


# In[122]:


data3 = list(sorted(distance))
target = 7
count=0
for j in range(target):
    count = count + data3[j][1]
    
if (count >= target/2):
    print("남자")
    point[2] = 1
else:
    print("여자")
    point[2] = 0

print(point)
    


# In[123]:


print(data3)
print(count)
type(data3)


# In[93]:


type(data3[1][1])


# In[125]:


print("입력")
a= int(input())
type(a)


# In[ ]:




