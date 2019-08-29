# -*- coding: utf-8 -*-
import numpy as np
import random
apple= []
banana = []
orange = []
grape = []
watermelon = []
fruit = []
result=[]
lists = []
ok =[]
#apple,banana,orange,grape,watermelon 랜덤으로 20개
for i in range(50):
    apple.append([random.randint(0,5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), 0])
    banana.append([random.randint(0,5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), 1])
    orange.append([random.randint(0,5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), 2])
    grape.append([random.randint(0,5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), 3])
    watermelon.append([random.randint(0,5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), 4])
p = apple + banana + orange + grape + watermelon
k = input("3,5,7,9,11 중에 넣으시요 제발")
#5개의 과일 변수
for i in range(0,5):
    fruit.append([random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5)])


# 점과 점사이의 거리 계산
for j in range(0,5):
    for i in range(0,250):
        result.append([distance(fruit[j],p[i]),p[i][4]])
    lists.append(sorted(result))
# k값으로 과일 구분
for j in range(0,5):
    a,b,o,g,w = 0,0,0,0,0
    for i in range(0,int(k)):
        if (lists[j][i][1] == 0):
            a += 1
        elif (lists[j][i][1] == 1):
            b += 1
        elif (lists[j][i][1] == 2):
            o += 1
        elif (lists[j][i][1] == 3):
            g += 1
        elif (lists[j][i][1] == 4):
            w += 1
    ok.append([a,b,o,g,w])
print(ok)
# 확인
for i in range(0,5):
    
    if (max(ok[i]) == ok[i][0]):
        print("apple")
    elif(max(ok[i]) == ok[i][1]):
        print("banana")
    elif(max(ok[i]) == ok[i][2]):
        print("orange")
    elif(max(ok[i]) == ok[i][3]):
        print("grape")
    elif(max(ok[i]) == ok[i][4]):
        print("watermelon")
    else:
        print("구분이 안되요")
#점과 점사이의 거리 공식
def distance(x,y):
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2)+pow((x[2]-y[2]),2)+pow((x[3]-y[3]),2))