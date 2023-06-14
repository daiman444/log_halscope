#!/usr/bin/env python3

import csv
import matplotlib as plt



input_log = input('Указать файл лога:')
output_log = input_log[::-1]

index = output_log.find("/")

if index != -1:
    output_log = output_log[index+1:]
else:
    print("не удается определить путь для сохранения лога")
    
output_log = output_log[::-1] + '/output_log.csv'
backup_log = input_log + '.bak'

with open(input_log, 'r') as file:
    lines = file.readlines()

with open(backup_log, 'w') as file:
    file.writelines(lines)
    
with open(input_log, 'r') as file:
    lines = file.readlines()
    
log_lines = lines[2:]

log_lines_output = []

headers_line = log_lines[0]

lines_num =  len(log_lines)

print(lines_num)

headers = headers_line.split()
headers = headers[0::2]

print(headers)

for i in range(lines_num):
    for header in headers:
        log_lines[i] = log_lines[i].replace(header, '')
        log_lines[i] = log_lines[i].replace("+", '')
        log_lines[i] = log_lines[i].replace(",", '.')
        
#TODO разбить строки на элементы списка

with open(output_log, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([s] for s in log_lines)
    
y1_values = []
y2_values = []
y3_values = []
y4_values = []    
    
    
with open(output_log, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        y1_values.append(float(row[0]))
        y2_values.append(float(row[1]))
        y3_values.append(float(row[2]))
        y4_values.append(float(row[3]))
        
x_values = range(len(y1_values))

plt.plot(x_values, y1_values, label="Y1")
plt.plot(x_values, y2_values, label="Y2")
plt.plot(x_values, y3_values, label="Y3")
plt.plot(x_values, y4_values, label="Y4")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Графики из CSV")
plt.grid(True)
plt.legend()
plt.show()

