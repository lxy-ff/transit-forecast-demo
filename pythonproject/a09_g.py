import json
import csv, os

#"dist","age","num_p"   column1=[row[0] for row in reader]  column2=[row[1] for row in reader]


with open('down.csv', 'r') as f:
    reader = csv.reader(f)
    column3 = [row[0] for row in reader]
num = [int(i) for i in column3]


with open('up.csv', 'r') as f:
    reader = csv.reader(f)
    column2=[row[0] for row in reader]
num2 = [int(i) for i in column2]


with open('s_name.csv', 'r') as f:
    reader = csv.reader(f)
    column2=[row[0] for row in reader]
print(column2)



filename = "s_name5.json"
with open(filename, 'w') as file_obj:
  json.dump(column2, file_obj)
filename = "up5.json"
with open(filename, 'w') as file_obj:
  json.dump(num2, file_obj)
filename = "down5.json"
with open(filename, 'w') as file_obj:
  json.dump(num, file_obj)