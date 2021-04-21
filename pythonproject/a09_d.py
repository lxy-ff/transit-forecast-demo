import csv, os

from matplotlib import pyplot as plt
import json

#"dist","age","num_p"   column1=[row[0] for row in reader]  column2=[row[1] for row in reader]


with open('age_dist_in.csv', 'r') as f:
    reader = csv.reader(f)
    column3 = [row[2] for row in reader]
num = [int(i) for i in column3]

with open('age_dist_in.csv', 'r') as f:
    reader = csv.reader(f)
    column2=[row[1] for row in reader]
age = [int(i) for i in column2]

with open('age_dist_in.csv', 'r') as f:
    reader = csv.reader(f)
    dist=[row[0] for row in reader]
dist= [str(i) for i in dist]


stri="Dist10"
age_=[]
k=0
start=dist.index(stri)
distre=dist
distre=distre.reverse()
length=len(dist)
end=length-dist.index(stri)

age_=age[start:end]
num_=num[start:end]

print(num_)

age_x = ['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99']  # 画图用的x轴，坐标是年龄范围


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(age_x, num_)

for i in range(10):
    plt.text(i, num_[i] + 0.1, "%s" % num_[i], ha='center',va='bottom')
plt.title("年龄结构分析")
plt.show()


filename = "x.json"
with open(filename, 'w') as file_obj:
  json.dump(age_x, file_obj)
filename = "y.json"
with open(filename, 'w') as file_obj:
  json.dump(num_, file_obj)


