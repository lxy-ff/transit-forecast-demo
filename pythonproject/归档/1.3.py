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
data = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3",con=conn)

data1 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line1' ",con=conn)
data2 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line2' ",con=conn)
data3 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line3' ",con=conn)
data4 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line4' ",con=conn)
data5 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line5' ",con=conn)
data10 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line10' ",con=conn)
data11 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line11' ",con=conn)
data12 = pd.read_sql("SELECT Station,Line,Dist,O,D,avr_O,avr_D from 1_3 where Line like 'Line12' ",con=conn)

Line_sum = []
Line1_sum = 0
Line2_sum = 0
Line3_sum = 0
Line4_sum = 0
Line5_sum = 0
Line10_sum = 0
Line11_sum = 0
Line12_sum = 0

# for i in range(len(data1.O)):
#     Line1_sum =Line1_sum + float(data1.avr_O[i])
# Line_sum.append(Line1_sum)
# for i in range(len(data2.O)):
#     Line2_sum =Line2_sum + float(data2.avr_O[i])
# Line_sum.append(Line2_sum)
# for i in range(len(data3.O)):
#     Line3_sum =Line3_sum + float(data3.avr_O[i])
# Line_sum.append(Line3_sum)
# for i in range(len(data4.O)):
#     Line4_sum =Line4_sum + float(data4.avr_O[i])
# Line_sum.append(Line4_sum)
# for i in range(len(data5.O)):
#     Line5_sum =Line5_sum + float(data5.avr_O[i])
# Line_sum.append(Line5_sum)
# for i in range(len(data10.O)):
#     Line10_sum =Line10_sum + float(data10.avr_O[i])
# Line_sum.append(Line10_sum)
# for i in range(len(data11.O)):
#     Line11_sum =Line11_sum + float(data11.avr_O[i])
# Line_sum.append(Line11_sum)
# for i in range(len(data12.O)):
#     Line12_sum =Line12_sum + float(data12.avr_O[i])
# Line_sum.append(Line12_sum)

for i in range(len(data1.O)):
    Line1_sum =Line1_sum + float(data1.avr_D[i])
Line_sum.append(Line1_sum)
for i in range(len(data2.O)):
    Line2_sum =Line2_sum + float(data2.avr_D[i])
Line_sum.append(Line2_sum)
for i in range(len(data3.O)):
    Line3_sum =Line3_sum + float(data3.avr_D[i])
Line_sum.append(Line3_sum)
for i in range(len(data4.O)):
    Line4_sum =Line4_sum + float(data4.avr_D[i])
Line_sum.append(Line4_sum)
for i in range(len(data5.O)):
    Line5_sum =Line5_sum + float(data5.avr_D[i])
Line_sum.append(Line5_sum)
for i in range(len(data10.O)):
    Line10_sum =Line10_sum + float(data10.avr_D[i])
Line_sum.append(Line10_sum)
for i in range(len(data11.O)):
    Line11_sum =Line11_sum + float(data11.avr_D[i])
Line_sum.append(Line11_sum)
for i in range(len(data12.O)):
    Line12_sum =Line12_sum + float(data12.avr_D[i])
Line_sum.append(Line12_sum)



print(Line_sum)




cursor.close()
#关闭数据库连接
conn.close()