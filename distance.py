#!/usr/bin/env python
# coding: utf-8

# ## 4차원 거리 함수

# In[ ]:


def distance(x, y):
    return (np.sqrt(pow((x[0]-y[0]), 2) + pow((x[1]-y[1]),2)) + pow((x[2]-y[2],2)) + pow((x[3]-y[3],2)))

