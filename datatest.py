# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:04:06 2020

@author: 64584
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm



data_d = pd.read_excel("data.xlsx", usecols=[1])
data_ex = data_d.values.tolist()
res = []
for dire in data_ex:
    res.append(dire[0])

data_s = pd.read_excel("data.xlsx", usecols=[2])
data_li = data_s.values.tolist()
res1 = []
for sp in data_li:
     res1.append(sp[0])
 
data_day = pd.read_excel("data.xlsx", usecols=[0])
data_date = data_day.iloc[:,0].tolist()


X = data_date
Y = res1


plt.figure(figsize=(16,9))

norm = plt.Normalize(min(res), max(res))
norm_res = norm(res)
map_vir = cm.get_cmap(name='hsv')
color = map_vir(norm_res)
ax = plt.bar(X,Y,width = 0.0007,color=color)


plt.xlabel("time",fontsize = 20)
plt.ylabel("speed",fontsize = 20)
plt.xticks(pd.date_range('2019-09-19','2019/10/14', freq = '1d'))
plt.gcf().autofmt_xdate()
plt.yticks(range(0, 60, 5))


plt.title("bar chart")
plt.show()