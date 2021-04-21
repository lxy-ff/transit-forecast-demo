# # 导入pymysql模块
# import pymysql
# # 连接database
# conn = pymysql.connect(host="127.0.0.1",user="root",password="15987645691sf",database="test",charset="utf8")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()
# # 定义要执行的SQL语句
#
# sql = """
#
# INSERT INTO JAN(userID,s_in,s_in_t,s_out,s_out_t,price)
# SELECT userID,s_in,s_in_t,s_out,s_out_t,price
# from trips
# WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') BETWEEN '2020-01-01' AND '2020-01-31'
#
# """
#
#
#
# # 执行SQL语句
# cursor.execute(sql)
# # 关闭光标对象
# cursor.close()
# # 关闭数据库连接
# conn.close()

import matplotlib.pyplot as plt
import pandas as pd
import pymysql
from collections import Counter
import json



#建立数据库连接
conn = pymysql.connect(host="127.0.0.1",user="root",password="15987645691sf",database="test",charset="utf8")
print("连接成功")
cursor = conn.cursor()

# sql = """
#
#
#
# """
#
# cursor.execute(sql)

#读取数据库表数据
data_ = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN",con=conn)

# for i in range(31):
#     if i>=10:
#         data1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-i'",con=conn)
#         x1 = list(data1.s_in_t)  # 一月进站时间
#         print(len(x1))

data1_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-01'",con=conn)
data1_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-02'",con=conn)
data1_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-03'",con=conn)
data1_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-04'",con=conn)
data1_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-05'",con=conn)
data1_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-06'",con=conn)
data1_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-07'",con=conn)
data1_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-08'",con=conn)
data1_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-09'",con=conn)
data1_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-10'",con=conn)
data1_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-11'",con=conn)
data1_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-12'",con=conn)
data1_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-13'",con=conn)
data1_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-14'",con=conn)
data1_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-15'",con=conn)
data1_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-16'",con=conn)
data1_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-17'",con=conn)
data1_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-18'",con=conn)
data1_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-19'",con=conn)
data1_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-20'",con=conn)
data1_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-21'",con=conn)
data1_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-22'",con=conn)
data1_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-23'",con=conn)
data1_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-24'",con=conn)
data1_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-25'",con=conn)
data1_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-26'",con=conn)
data1_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-27'",con=conn)
data1_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-28'",con=conn)
data1_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-29'",con=conn)
data1_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-30'",con=conn)
data1_31 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from JAN WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-01-31'",con=conn)


data2_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-01'",con=conn)
data2_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-02'",con=conn)
data2_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-03'",con=conn)
data2_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-04'",con=conn)
data2_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-05'",con=conn)
data2_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-06'",con=conn)
data2_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-07'",con=conn)
data2_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-08'",con=conn)
data2_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-09'",con=conn)
data2_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-10'",con=conn)
data2_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-11'",con=conn)
data2_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-12'",con=conn)
data2_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-13'",con=conn)
data2_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-14'",con=conn)
data2_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-15'",con=conn)
data2_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-16'",con=conn)
data2_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-17'",con=conn)
data2_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-18'",con=conn)
data2_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-19'",con=conn)
data2_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-20'",con=conn)
data2_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-21'",con=conn)
data2_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-22'",con=conn)
data2_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-23'",con=conn)
data2_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-24'",con=conn)
data2_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-25'",con=conn)
data2_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-26'",con=conn)
data2_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-27'",con=conn)
data2_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-28'",con=conn)
data2_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Feb WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-02-29'",con=conn)

data3_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-01'",con=conn)
data3_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-02'",con=conn)
data3_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-03'",con=conn)
data3_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-04'",con=conn)
data3_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-05'",con=conn)
data3_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-06'",con=conn)
data3_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-07'",con=conn)
data3_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-08'",con=conn)
data3_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-09'",con=conn)
data3_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-10'",con=conn)
data3_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-11'",con=conn)
data3_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-12'",con=conn)
data3_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-13'",con=conn)
data3_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-14'",con=conn)
data3_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-15'",con=conn)
data3_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-16'",con=conn)
data3_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-17'",con=conn)
data3_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-18'",con=conn)
data3_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-19'",con=conn)
data3_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-20'",con=conn)
data3_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-21'",con=conn)
data3_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-22'",con=conn)
data3_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-23'",con=conn)
data3_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-24'",con=conn)
data3_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-25'",con=conn)
data3_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-26'",con=conn)
data3_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-27'",con=conn)
data3_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-28'",con=conn)
data3_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-29'",con=conn)
data3_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-30'",con=conn)
data3_31 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Mar WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-03-31'",con=conn)

data4_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-01'",con=conn)
data4_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-02'",con=conn)
data4_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-03'",con=conn)
data4_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-04'",con=conn)
data4_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-05'",con=conn)
data4_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-06'",con=conn)
data4_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-07'",con=conn)
data4_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-08'",con=conn)
data4_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-09'",con=conn)
data4_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-10'",con=conn)
data4_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-11'",con=conn)
data4_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-12'",con=conn)
data4_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-13'",con=conn)
data4_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-14'",con=conn)
data4_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-15'",con=conn)
data4_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-16'",con=conn)
data4_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-17'",con=conn)
data4_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-18'",con=conn)
data4_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-19'",con=conn)
data4_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-20'",con=conn)
data4_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-21'",con=conn)
data4_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-22'",con=conn)
data4_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-23'",con=conn)
data4_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-24'",con=conn)
data4_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-25'",con=conn)
data4_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-26'",con=conn)
data4_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-27'",con=conn)
data4_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-28'",con=conn)
data4_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-29'",con=conn)
data4_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Apr WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-04-30'",con=conn)

data5_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-01'",con=conn)
data5_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-02'",con=conn)
data5_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-03'",con=conn)
data5_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-04'",con=conn)
data5_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-05'",con=conn)
data5_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-06'",con=conn)
data5_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-07'",con=conn)
data5_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-08'",con=conn)
data5_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-09'",con=conn)
data5_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-10'",con=conn)
data5_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-11'",con=conn)
data5_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-12'",con=conn)
data5_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-13'",con=conn)
data5_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-14'",con=conn)
data5_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-15'",con=conn)
data5_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-16'",con=conn)
data5_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-17'",con=conn)
data5_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-18'",con=conn)
data5_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-19'",con=conn)
data5_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-20'",con=conn)
data5_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-21'",con=conn)
data5_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-22'",con=conn)
data5_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-23'",con=conn)
data5_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-24'",con=conn)
data5_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-25'",con=conn)
data5_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-26'",con=conn)
data5_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-27'",con=conn)
data5_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-28'",con=conn)
data5_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-29'",con=conn)
data5_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-30'",con=conn)
data5_31 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from May WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-05-31'",con=conn)

data6_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-01'",con=conn)
data6_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-02'",con=conn)
data6_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-03'",con=conn)
data6_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-04'",con=conn)
data6_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-05'",con=conn)
data6_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-06'",con=conn)
data6_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-07'",con=conn)
data6_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-08'",con=conn)
data6_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-09'",con=conn)
data6_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-10'",con=conn)
data6_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-11'",con=conn)
data6_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-12'",con=conn)
data6_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-13'",con=conn)
data6_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-14'",con=conn)
data6_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-15'",con=conn)
data6_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-16'",con=conn)
data6_17 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-17'",con=conn)
data6_18 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-18'",con=conn)
data6_19 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-19'",con=conn)
data6_20 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-20'",con=conn)
data6_21 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-21'",con=conn)
data6_22 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-22'",con=conn)
data6_23 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-23'",con=conn)
data6_24 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-24'",con=conn)
data6_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-25'",con=conn)
data6_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-26'",con=conn)
data6_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-27'",con=conn)
data6_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-28'",con=conn)
data6_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-29'",con=conn)
data6_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jun WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-06-30'",con=conn)

data7_1 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-01'",con=conn)
data7_2 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-02'",con=conn)
data7_3 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-03'",con=conn)
data7_4 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-04'",con=conn)
data7_5 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-05'",con=conn)
data7_6 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-06'",con=conn)
data7_7 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-07'",con=conn)
data7_8 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-08'",con=conn)
data7_9 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-09'",con=conn)
data7_10 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-10'",con=conn)
data7_11 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-11'",con=conn)
data7_12 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-12'",con=conn)
data7_13 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-13'",con=conn)
data7_14 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-14'",con=conn)
data7_15 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-15'",con=conn)
data7_16 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Jul WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2020-07-16'",con=conn)

data12_25 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-25'",con=conn)
data12_26 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-26'",con=conn)
data12_27 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-27'",con=conn)
data12_28 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-28'",con=conn)
data12_29 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-29'",con=conn)
data12_30 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-30'",con=conn)
data12_31 = pd.read_sql("SELECT userID,s_in,s_in_t,s_out,s_out_t,price from Dec_ WHERE DATE_FORMAT(s_in_t,'%Y-%m-%d') LIKE '2019-12-31'",con=conn)


list1_1 = [data1_1,data1_2,data1_3,data1_4,data1_5,data1_6,data1_7,data1_8,data1_9,data1_10,data1_11,data1_12,data1_13,data1_14,data1_15,data1_16,data1_17,data1_18,data1_19,data1_20,data1_21,data1_22,data1_23,data1_24,data1_25,data1_26,data1_27,data1_28,data1_29,data1_30,data1_31]
list2_1 = [data2_1,data2_2,data2_3,data2_4,data2_5,data2_6,data2_7,data2_8,data2_9,data2_10,data2_11,data2_12,data2_13,data2_14,data2_15,data2_16,data2_17,data2_18,data2_19,data2_20,data2_21,data2_22,data2_23,data2_24,data2_25,data2_26,data2_27,data2_28,data2_29]
list3_1 = [data3_1,data3_2,data3_3,data3_4,data3_5,data3_6,data3_7,data3_8,data3_9,data3_10,data3_11,data3_12,data3_13,data3_14,data3_15,data3_16,data3_17,data3_18,data3_19,data3_20,data3_21,data3_22,data3_23,data3_24,data3_25,data3_26,data3_27,data3_28,data3_29,data3_30,data3_31]
list4_1 = [data4_1,data4_2,data4_3,data4_4,data4_5,data4_6,data4_7,data4_8,data4_9,data4_10,data4_11,data4_12,data4_13,data4_14,data4_15,data4_16,data4_17,data4_18,data4_19,data4_20,data4_21,data4_22,data4_23,data4_24,data4_25,data4_26,data4_27,data4_28,data4_29,data4_30]
list5_1 = [data5_1,data5_2,data5_3,data5_4,data5_5,data5_6,data5_7,data5_8,data5_9,data5_10,data5_11,data5_12,data5_13,data5_14,data5_15,data5_16,data5_17,data5_18,data5_19,data5_20,data5_21,data5_22,data5_23,data5_24,data5_25,data5_26,data5_27,data5_28,data5_29,data5_30,data5_31]
list6_1 = [data6_1,data6_2,data6_3,data6_4,data6_5,data6_6,data6_7,data6_8,data6_9,data6_10,data6_11,data6_12,data6_13,data6_14,data6_15,data6_16,data6_17,data6_18,data6_19,data6_20,data6_21,data6_22,data6_23,data6_24,data6_25,data6_26,data6_27,data6_28,data6_29,data6_30]
list7_1 = [data7_1,data7_2,data7_3,data7_4,data7_5,data7_6,data7_7,data7_8,data7_9,data7_10,data7_11,data7_12,data7_13,data7_14,data7_15,data7_16]
list12_1 = [data12_25,data12_26,data12_27,data12_28,data12_29,data12_30,data12_31]



#数据转化为列表

list1_2 = []
list2_2 = []
list3_2 = []
list4_2 = []
list5_2 = []
list6_2 = []
list7_2 = []
list12_2 = []


for i in range(len(list1_1)):
    list1_2.append(list1_1[i].s_in_t)
    list3_2.append(list3_1[i].s_in_t)
    list5_2.append(list5_1[i].s_in_t)
for i in range(len(list4_1)):
    list4_2.append(list4_1[i].s_in_t)
    list6_2.append(list6_1[i].s_in_t)
for i in range(len(list2_1)):
    list2_2.append(list2_1[i].s_in_t)
for i in range(len(list7_1)):
    list7_2.append(list7_1[i].s_in_t)
for i in range(len(list12_1)):
    list12_2.append(list12_1[i].s_in_t)



# l = 31
# list1_3 = [0]*l
# list2_3 = [0]*l
# list3_3 = [0]*l
# list4_3 = [0]*l
# list5_3 = [0]*l
# list6_3 = [0]*l
# list7_3 = [0]*l
# list12_3 = [0]*7

list1_3 = [0]*31
list2_3 = [0]*29
list3_3 = [0]*31
list4_3 = [0]*30
list5_3 = [0]*31
list6_3 = [0]*30
list7_3 = [0]*16
list12_3 = [0]*7

for i in range(len(list1_2)):
    list1_3[i] = len(list1_2[i])
    list3_3[i] = len(list3_2[i])
    list5_3[i] = len(list5_2[i])
for i in range(len(list4_2)):
    list4_3[i] = len(list4_2[i])
    list6_3[i] = len(list6_2[i])
for i in range(len(list2_2)):
    list2_3[i] = len(list2_2[i])
for i in range(len(list7_2)):
    list7_3[i] = len(list7_2[i])
for i in range(len(list12_2)):
    list12_3[i] = len(list12_2[i])





y2 = []
yy2 = [list12_3,list1_3,list2_3,list3_3,list4_3,list5_3,list6_3,list7_3]

# yy1 = ["Date","Ridership","Month","numID"]
# y = [yy1]
# y1 = [list1_3,list2_3,list3_3,list4_3,list5_3,list6_3,list7_3]
# a = ["2020.01","2020.02","2020.03","2020.04","2020.05","2020.06","2020.07"]
# c = ["1号","2号","3号","4号","5号","6号","7号","8号","9号","10号","11号","12号","13号","14号","15号","16号","17号","18号","19号","20号","21号","22号","23号","24号","25号","26号","27号","28号","29号","30号","31号"]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]



for j in range(len(list12_3)):
     y2.append(list12_3[j])
for j in range(len(list1_3)):
     y2.append(list1_3[j])
for j in range(len(list2_3)):
     y2.append(list2_3[j])
for j in range(len(list3_3)):
     y2.append(list3_3[j])
for j in range(len(list4_3)):
     y2.append(list4_3[j])
for j in range(len(list5_3)):
     y2.append(list5_3[j])
for j in range(len(list6_3)):
     y2.append(list6_3[j])
for j in range(len(list7_3)):
     y2.append(list7_3[j])



# for i in range(l):
#     for j in range(len(y1)):
#         yy = []
#         yy.append(c[i])
#         yy.append(y1[j][i])
#         yy.append(a[j])
#         yy.append(b[i])
#         y.append(yy)


print(y2)


# filename = "x.json"
# with open(filename, 'w') as file_obj:
#   json.dump(x, file_obj)
filename = "1.1.json"
with open(filename, 'w') as file_obj:
  json.dump(y2, file_obj)






cursor.close()
#关闭数据库连接
conn.close()