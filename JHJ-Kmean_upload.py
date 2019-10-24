#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
r = [] # 남자
b = [] # 여자
p1_save = []
p2_save = []

for i in range(50): # 남.여 각각 50개의 샘플을 생성한다
    r.append([random.randint(160, 200), random.randint(60, 100)])
    b.append([random.randint(140, 180), random.randint(45, 70)])
man = r+b


def number_is_upper(p1, p2, man):
    m  = (p2[1]-p1[1]) / (p2[0]-p1[0])
    a = (p1[0]+p2[0])/2
    b = (p1[1]+p2[1])/2
    line = man[0]- m * man[1] - a + m * b
    if line > 0:
        return True
    else:
        return False
# 이 루프는 함수를 간략화하기 위해 기울기가 0또는 무한대가 나오지 않는 두 점을 뽑는다
while True:
    #p1 = [random.randint(100, 200), random.randint(45, 100)]
    #p2 = [random.randint(100, 200), random.randint(45, 100)]
    p1 = [random.randint(0, 200), random.randint(0, 200)]
    p2 = [random.randint(0, 200), random.randint(0, 200)]
    print("랜덤 시작점: ", p1,"#", p2)
    if (p1[0] != p2[0] and p1[1] != p2[1]):
        break;
#비교를 위해 초기값을 저장한다
p1_init = p1
p2_init = p2

cnt = 0
while(cnt < 50):
    print(p1, ";", p2)
    upper = []
    lower = []
    # 선분 위쪽의 점과 아래쪽 점을 분리하여 upper, lower 리스트에 저장한다
    for i in range(len(man)):
        if (number_is_upper(p1, p2, man[i])):
            upper.append(man[i])
        else:
            lower.append(man[i])
    #upper, lower리스트가 비어있으면 기존 포인트를 그대로 사용하고,
    #그렇지 않으면 리스트의 평균값으로 p1, p2를 바꾼다
    if(len(upper) == 0):
        p1=p1
    else:
        p1 = np.mean(upper, axis= 0 )
        
    if(len(lower) == 0):
        p2=p2
    else:
        p2 = np.mean(lower, axis=0 )
    cnt+=1
    #optional: p1, p2가 변해온 과정을 저장한다
    p1_save.append(p1)
    p2_save.append(p2)

#데이터를 그래프로 출력
for i in range(len(r)):
    plt.plot(r[i][0], r[i][1], marker = 'o', color = 'red')
    plt.plot(b[i][0], b[i][1], marker = 'o', color = 'blue')
for i in range(len(p1_save)):
    plt.plot(p1_save[i][0], p1_save[i][1], marker = 'o', color = 'green')
    plt.plot(p2_save[i][0], p2_save[i][1], marker = 'o', color = 'black')

#plt.plot(p1[0], p1[1], marker = 'o', color = 'green')
#plt.plot(p2[0], p2[1], marker = 'o', color = 'black')
plt.plot(p1_init[0], p1_init[1], marker = 'x', color = 'green')
plt.plot(p2_init[0], p2_init[1], marker = 'x', color = 'black')


# In[ ]:




