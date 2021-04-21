import pandas as pd
import pymysql
import numpy as np
from collections import Counter
import json



#建立数据库连接
conn = pymysql.connect(host="127.0.0.1",user="root",password="15987645691sf",database="test",charset="utf8")
print("连接成功")
cursor = conn.cursor()
#读取数据库表数据
data1_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data1_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data1_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data1_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data1_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data1_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data1_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data1_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data1_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data1_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data1_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data1_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data2_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data2_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data2_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data2_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data2_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data2_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data2_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data2_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data2_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data2_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data2_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data2_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data3_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data3_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data3_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data3_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data3_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data3_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data3_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data3_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data3_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data3_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data3_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data3_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data4_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data4_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data4_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data4_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data4_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data4_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data4_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data4_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data4_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data4_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data4_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data4_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data5_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data5_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data5_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data5_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data5_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data5_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data5_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data5_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data5_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data5_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data5_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data5_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data6_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data6_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data6_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data6_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data6_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data6_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data6_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data6_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data6_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data6_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data6_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data6_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)

data7_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '00:00:00' AND '01:59:59'",con=conn)
data7_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '02:00:00' AND '03:59:59'",con=conn)
data7_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '04:00:00' AND '05:59:59'",con=conn)
data7_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '06:00:00' AND '07:59:59'",con=conn)
data7_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '08:00:00' AND '09:59:59'",con=conn)
data7_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '10:00:00' AND '11:59:59'",con=conn)
data7_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '12:00:00' AND '13:59:59'",con=conn)
data7_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '14:00:00' AND '15:59:59'",con=conn)
data7_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '16:00:00' AND '17:59:59'",con=conn)
data7_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '18:00:00' AND '19:59:59'",con=conn)
data7_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '20:00:00' AND '21:59:59'",con=conn)
data7_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%H:%i:%s') BETWEEN '22:00:00' AND '23:59:59'",con=conn)


list1_1 = [data1_1,data1_2,data1_3,data1_4,data1_5,data1_6,data1_7,data1_8,data1_9,data1_10,data1_11,data1_12]
list2_1 = [data2_1,data2_2,data2_3,data2_4,data2_5,data2_6,data2_7,data2_8,data2_9,data2_10,data2_11,data2_12]
list3_1 = [data3_1,data3_2,data3_3,data3_4,data3_5,data3_6,data3_7,data3_8,data3_9,data3_10,data3_11,data3_12]
list4_1 = [data4_1,data4_2,data4_3,data4_4,data4_5,data4_6,data4_7,data4_8,data4_9,data4_10,data4_11,data4_12]
list5_1 = [data5_1,data5_2,data5_3,data5_4,data5_5,data5_6,data5_7,data5_8,data5_9,data5_10,data5_11,data5_12]
list6_1 = [data6_1,data6_2,data6_3,data6_4,data6_5,data6_6,data6_7,data6_8,data6_9,data6_10,data6_11,data6_12]
list7_1 = [data7_1,data7_2,data7_3,data7_4,data7_5,data7_6,data7_7,data7_8,data7_9,data7_10,data7_11,data7_12]


list1_2 = []
list2_2 = []
list3_2 = []
list4_2 = []
list5_2 = []
list6_2 = []
list7_2 = []


for i in range(len(list1_1)):
    list1_2.append(list1_1[i].s_in_t)
    list3_2.append(list3_1[i].s_in_t)
    list5_2.append(list5_1[i].s_in_t)
    list4_2.append(list4_1[i].s_in_t)
    list6_2.append(list6_1[i].s_in_t)
    list2_2.append(list2_1[i].s_in_t)
    list7_2.append(list7_1[i].s_in_t)

list1_3 = []
list2_3 = []
list3_3 = []
list4_3 = []
list5_3 = []
list6_3 = []
list7_3 = []

for i in range(len(list1_2)):
    list1_3.append(len(list1_2[i])/31)
    list1_3_3f = [float('{:.3f}'.format(i)) for i in list1_3]
for i in range(len(list3_2)):
    list3_3.append(len(list3_2[i])/31)
    list3_3_3f = [float('{:.3f}'.format(i)) for i in list3_3]
for i in range(len(list5_2)):
    list5_3.append(len(list5_2[i])/31)
    list5_3_3f = [float('{:.3f}'.format(i)) for i in list5_3]
for i in range(len(list4_2)):
    list4_3.append(len(list4_2[i])/30)
    list4_3_3f = [float('{:.3f}'.format(i)) for i in list4_3]
for i in range(len(list6_2)):
    list6_3.append(len(list6_2[i])/30)
    list6_3_3f = [float('{:.3f}'.format(i)) for i in list6_3]
for i in range(len(list2_2)):
    list2_3.append(len(list2_2[i])/29)
    list2_3_3f = [float('{:.3f}'.format(i)) for i in list2_3]
for i in range(len(list7_2)):
    list7_3.append(len(list7_2[i])/16)
    list7_3_3f = [float('{:.3f}'.format(i)) for i in list7_3]


# print(list1_3_3f)


yy1 = ["Timeframe","Ridership","Month","numID"]
y = [yy1]
y1 = [list1_3_3f,list2_3_3f,list3_3_3f,list4_3_3f,list5_3_3f,list6_3_3f,list7_3_3f]
a = ["2020.01","2020.02","2020.03","2020.04","2020.05","2020.06","2020.07"]
c = ["0:00-2:00","2:00-4:00","4:00-6:00","6:00-8:00","8:00-10:00","10:00-12:00","12:00-14:00","14:00-16:00","16:00-18:00","18:00-20:00","20:00-22:00","22:00-24:00"]
b = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(12):
    for j in range(len(y1)):
        yy = []
        yy.append(c[i])
        yy.append(y1[j][i])
        yy.append(a[j])
        yy.append(b[i])
        y.append(yy)

# print(y)

filename = "1.1.1.json"
with open(filename, 'w') as file_obj:
  json.dump(y, file_obj)


cursor.close()
#关闭数据库连接
conn.close()