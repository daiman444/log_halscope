#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

input_log = input('Select file:')
output_log = input_log[::-1]
index = output_log.find("/")

if index != -1:
    output_log = output_log[index+1:]
else:
    print("File error")
    
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
headers = headers_line.split()
headers = headers[0::2]
headers_list = []

for i in headers:
    i_counter = 1
    if i not in headers_list:
        headers_list.append(i)
    else:
        i += '_' + str(i_counter)
        headers_list.append(i)

for i in range(lines_num):
    for header in headers:
        log_lines[i] = log_lines[i].replace(header, '')
        log_lines[i] = log_lines[i].replace('\n', '')
        log_lines[i] = log_lines[i].replace("+", '')
        log_lines[i] = log_lines[i].replace(",", '.')
    log_lines[i] = log_lines[i].split()  

with open(output_log, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(log_lines)

for i in headers:
    i = list(i)
    
headers_dict = {}
for i in headers_list:
    headers_dict[i] = [] 

with open(output_log, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(headers_dict)):
            dict_key = headers_list[i]
            headers_dict[dict_key].append(float(row[i]))
        
x_values = range(len(headers_dict[headers_list[0]]))

for i in range(len(headers_list)):
    dict_key = headers_list[i]    
    plt.plot(x_values, headers_dict[dict_key], label=str(headers_list[i]))

plt.xlabel("Thread step")
plt.ylabel("Scale(1:1)")
plt.title("Plot log from Halscope")
plt.grid(True)
plt.legend()
plt.show()

