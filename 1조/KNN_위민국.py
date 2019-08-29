#!/usr/bin/env python
# coding: utf-8

# # # 2조 최종본입니다.
# # ## 추가사항 : 3. 머리카락 길이, 4. 옷 크기
# # ### k = 3, 5, 7, 11일 때 결과값

# In[1]:


import numpy as np # numpy : 다차원 함수 
import random # 랜덤함수
import matplotlib.pyplot as plt # 시각화로 표현함. 애칭을 pit로 지정
get_ipython().run_line_magic('matplotlib', 'inline')
r = [] # 여자
b = [] # 남자
size = [85, 90, 95, 100, 105, 110] #[추가사항]옷 사이즈.
for i in range(50):
    r.append([random.randint(40, 70), random.randint(140, 180), random.randint(20, 40), size[random.randint(0, 4)], 1])
    b.append([random.randint(60, 90), random.randint(160, 200), random.randint(1, 20), size[random.randint(1, 5)], 0])
    
def distance(x,y):# 두점 사이의 거리
    return np.sqrt(pow((x[0]-y[0]), 2) + pow((x[1] - y[1]), 2) + pow((x[2] - y[2]), 2) + pow((x[3] - y[3]), 2))

def knn(x, y, k): # knn 함수
    result = []
    cnt = 0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[i][4]])
    result.sort()
    for i in range(k-1):
        if(result[i][1] == 1):
            cnt += 1
    if(cnt > (k/2)):
        print("당신은 여자입니다.")
    else:
        print("당신은 남자입니다.")

for i in range(50): 
    plt.plot(r[i][0], r[i][1], r[i][2], r[i][3], marker='o', color = 'red')
    plt.plot(b[i][0], b[i][1], b[i][2], b[i][3], marker='o', color = 'blue')

new = [] #새로운 좌표

for i in range(3): 
    num = random.randint(1,3)
    if(num == 1):   # 여자일때
        new.append([random.randint(40, 70), random.randint(140, 180), random.randint(20, 40), size[random.randint(0, 4)]])
    elif(num == 2): # 남자일떄
        new.append([random.randint(60, 90), random.randint(160, 200), random.randint(1, 20), size[random.randint(1, 5)]])
    else:           # 애매한상황
        new.append([random.randint(60, 70), random.randint(160, 180), 20, size[random.randint(1, 4)]])

#weight = input("몸무게를 입력해주세요.")
#height = input("키를 입력해주세요.")
#Hair_length = input("머리길이를 입력해주세요.")
#Clothes_size = input("옷 크기를 입력해주세요.")

#new = [int(weight), int(height), int(Hair_length), int(Clothes_size)]

#for i in range(50):
 #   plt.plot(r[i][0], r[i][1], r[i][2], r[i][3], marker='o', color = 'red')
  #  plt.plot(b[i][0], b[i][1], b[i][2], b[i][3], marker='o', color = 'blue')
for i in range(3): 
    plt.plot(new[i][0], new[i][1], new[i][2], new[i][3], marker = 'x', color = 'black')
for j in range(3):
    print(j+1, "번째 사람", end = " → ")
    print("키 : ", new[j][1], end = ", ")
    print("몸무게 : ", new[j][0], end = ", ")
    print("머리 길이 : ", new[j][2], end = ", ")
    print("옷 크기 : ", new[j][3])
    for i in range(3, 12, 2):
        if(i == 9):
            continue
        print("k가", i, "일 때 : ")
        knn(new[j], r+b, i)
    print("\n")


# In[ ]:




