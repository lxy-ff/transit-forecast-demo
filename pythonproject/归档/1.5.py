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
data1 = pd.read_sql("SELECT Line1_Sta,Line1_num,Line10_Sta,Line10_num,Line11_Sta,Line11_num,Line12_Sta,Line12_num,Line2_Sta,Line2_num,Line3_Sta,Line3_num,Line4_Sta,Line4_num,Line5_Sta,Line5_num from morn_in",con=conn)
data2 = pd.read_sql("SELECT Line1_num,Line10_num,Line11_num,Line12_num,Line2_num,Line3_num,Line4_num,Line5_num from morn_out",con=conn)
data3 = pd.read_sql("SELECT Line1_num,Line10_num,Line11_num,Line12_num,Line2_num,Line3_num,Line4_num,Line5_num from noon_in",con=conn)
data4 = pd.read_sql("SELECT Line1_num,Line10_num,Line11_num,Line12_num,Line2_num,Line3_num,Line4_num,Line5_num from noon_out",con=conn)

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x10 = []
x11 = []
x12 = []
y = ['进站早高峰','进站晚高峰','出站早高峰','出站晚高峰']
Line1_data = []
Line2_data = []
Line3_data = []
Line4_data = []
Line5_data = []
Line10_data = []
Line11_data = []
Line12_data = []


for i in range(20):
    x1.append(data1.Line1_Sta[i])
for i in range(23):
    x2.append(data1.Line2_Sta[i])
for i in range(42):
    x3.append(data1.Line3_Sta[i])
for i in range(7):
    x4.append(data1.Line4_Sta[i])
for i in range(8):
    x5.append(data1.Line5_Sta[i])
for i in range(19):
    x10.append(data1.Line10_Sta[i])
for i in range(31):
    x11.append(data1.Line11_Sta[i])
for i in range(18):
    x12.append(data1.Line12_Sta[i])

# for i in range(4):
#     bb = []
#     for j in range(20):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line1_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line1_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line1_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line1_num[j]))
#         bb.append(aa)
#     Line1_data.append(bb)
#
# for i in range(4):
#     bb = []
#     for j in range(23):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line2_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line2_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line2_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line2_num[j]))
#         bb.append(aa)
#     Line2_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(42):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line3_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line3_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line3_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line3_num[j]))
#         bb.append(aa)
#     Line3_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(7):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line4_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line4_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line4_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line4_num[j]))
#         bb.append(aa)
#     Line4_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(8):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line5_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line5_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line5_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line5_num[j]))
#         bb.append(aa)
#     Line5_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(19):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line10_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line10_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line10_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line10_num[j]))
#         bb.append(aa)
#     Line10_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(31):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line11_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line11_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line11_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line11_num[j]))
#         bb.append(aa)
#     Line11_data.append(bb)

# for i in range(4):
#     bb = []
#     for j in range(18):
#         aa = []
#         if i == 0:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data1.Line12_num[j]))
#         if i == 1:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data2.Line12_num[j]))
#         if i == 2:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data3.Line12_num[j]))
#         if i == 3:
#             aa.append(i)
#             aa.append(j)
#             aa.append(int(data4.Line12_num[j]))
#         bb.append(aa)
#     Line12_data.append(bb)

filename = "1.5.json"
with open(filename, 'w') as file_obj:
  json.dump(x1, file_obj)

print(x12)

















cursor.close()
#关闭数据库连接
conn.close()