import matplotlib.pyplot as plt
import pandas as pd
import pymysql
from collections import Counter
import json

#建立数据库连接
conn = pymysql.connect(host="127.0.0.1",user="root",password="15987645691sf",database="test",charset="utf8")
print("连接成功")
cursor = conn.cursor()

#读取数据库表数据
data_ = pd.read_sql("SELECT f1,Source,Target,weight from GroupOD1",con=conn)



for i in range(len(data_.f1)):
    a = []
    if len(data_.Source[i]) == 4:
        for j in range(len(data_.Source[i])-3):
            a.append(data_.Source[i][j+3])
        data_.Source[i] = a[0]
    if len(data_.Source[i]) == 5:
        for j in range(len(data_.Source[i])-3):
            a.append(data_.Source[i][j+3])
        data_.Source[i] = a[0] + a[1]
    if len(data_.Source[i]) == 6:
        for j in range(len(data_.Source[i])-3):
            a.append(data_.Source[i][j+3])
        data_.Source[i] = a[0] + a[1] + a[2]


for i in range(len(data_.f1)):
    a = []
    if len(data_.Target[i]) == 4:
        for j in range(len(data_.Target[i])-3):
            a.append(data_.Target[i][j+3])
        data_.Target[i] = a[0]
    if len(data_.Target[i]) == 5:
        for j in range(len(data_.Target[i])-3):
            a.append(data_.Target[i][j+3])
        data_.Target[i] = a[0] + a[1]
    if len(data_.Target[i]) == 6:
        for j in range(len(data_.Target[i])-3):
            a.append(data_.Target[i][j+3])
        data_.Target[i] = a[0] + a[1] + a[2]

y = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
yy1 = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
yy2 = []
yy3 = []
yy4 = []
yy = []
b = []
bb = []
bbb = []
n = 0
m = 0



for i in range(1,169):
    bb.append(i)
for i in range(len(bb)):
    b.append(str(bb[i]))
for i in range(len(bb)):
    bbb.append("Sta"+str(b[i]))


for j in range(168):
    for i in range(len(data_.f1)):
        aa = []
        if data_.Source[i] == b[j]:
            aa.append(data_.Source[i])
            aa.append(data_.Target[i])
            aa.append(data_.weight[i])
            y.append(aa)
            if (int(b[j])-1) % 17 == 0 &  n<9:
                if y[len(y)-1][0] != y[len(y)-2][0]:
                    for k in range(m, len(y) - 1):
                        yy1[n].append(y[k])
                    m = len(y) - 1
                    n = n + 1


for k in range(m, len(y) - 1):
    yy1[9].append(y[k])



for i in range(len(data_.f1)):
    aa = []
    for j in range(3):
        if j<=1:
            aa.append(int(y[i][j]) - 1)
        if j==2:
            aa.append(int(y[i][j]))
    yy.append(aa)

for i in range(len(yy1)):
    yy2 = []
    for j in range(len(yy1[i])):
        aa = []
        for k in range(3):
            if k<=1:
                aa.append(int(yy1[i][j][k])-1)
            if k==2:
                aa.append(int(yy1[i][j][k]))
        yy2.append(aa)
    yy3.append(yy2)

# print(len(yy3[9]))

for i in range(1,9):
    mm = 0
    for j in range(len(yy3[i])-1):
        if yy3[i][j+1][0] != yy3[i][j][0]:
            yy3[i][j][0] = mm
            mm = mm + 1
        if yy3[i][j+1][0] == yy3[i][j][0]:
            yy3[i][j][0]=mm

    yy3[i][len(yy3[i])-1][0] = 16

# print(len(yy3[9]))
# print(yy3[9])

mm = 0
for i in range(153,168):
    for j in range(len(yy3[9])):
        if yy3[9][j][0] == i:
            yy3[9][j][0] = mm
    mm = mm + 1
        # if yy3[9][j + 1][0] == yy3[9][j][0]:
        #     yy3[9][j][0] = mm




filename = "1.6.json"
with open(filename, 'w') as file_obj:
  json.dump(yy, file_obj)
filename = "1.6_.json"
with open(filename, 'w') as file_obj:
  json.dump(bbb, file_obj)
filename = "1.6_1.json"
with open(filename, 'w') as file_obj:
  json.dump(yy3[9], file_obj)


# print(yy3[9])
# for i in range(5):
#     print(yy[i])


cursor.close()
#关闭数据库连接
conn.close()


