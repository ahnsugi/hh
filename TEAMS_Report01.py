<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
>>>>>>> e18241db4c39c31b1f7f4b6a336facf97e7b5594
import numpy as np
import random
r = []
b = [] 
man = []
result=[]
list = []
<<<<<<< HEAD
#r,b�� ���ڿͿ��� �������� 50��
=======
>>>>>>> e18241db4c39c31b1f7f4b6a336facf97e7b5594
for i in range(50):
    r.append([random.randint(40,70), random.randint(140, 180), random.randint(200, 260), random.randint(25, 60), 1])
    b.append([random.randint(60,90), random.randint(160, 200), random.randint(240, 300), random.randint(1, 20), 0])
p = r+b
k = input("3,5,7,9,11 �߿� �����ÿ� ����")
<<<<<<< HEAD
#3���� ��� ����
for i in range(0,3):
    man.append([random.randint(40,90),random.randint(140,200),random.randint(200,300),random.randint(1,60)])

#���� �������� �Ÿ� ����
def distance(x,y):
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2)+pow((x[2]-y[2]),2)+pow((x[3]-y[3]),2))
# ���� �������� �Ÿ� ���
=======
for i in range(0,3):
    man.append([random.randint(40,90),random.randint(140,200),random.randint(200,300),random.randint(1,60)])
def distance(x,y):
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2)+pow((x[2]-y[2]),2)+pow((x[3]-y[3]),2))
>>>>>>> e18241db4c39c31b1f7f4b6a336facf97e7b5594
for j in range(0,3):
    for i in range(0,100):
        result.append([distance(man[j],p[i]),p[i][4]])
    list.append(sorted(result))
<<<<<<< HEAD
# k������ ���� ����
=======
>>>>>>> e18241db4c39c31b1f7f4b6a336facf97e7b5594
for j in range(0,3):
    female = 0
    male = 0
    for i in range(0,int(k)):
        if (list[j][i][1] == 1):
            female += 1
        elif (list[j][i][1] == 0):
            male += 1
<<<<<<< HEAD
# Ȯ��
=======
print(list)
>>>>>>> e18241db4c39c31b1f7f4b6a336facf97e7b5594
for h in range(0,3):
    if (female < male):
        print(k,"�� ��",man[h],"�� ����")
    else:
        print(k,"�� ��",man[h],"�� ����")