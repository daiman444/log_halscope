#!/usr/bin/env python3

input_log = input('Указать файл лога:')
output_log = input_log[::-1]

index = output_log.find("/")

if index != -1:
    output_log = output_log[index+1:]
else:
    print("не удается определить путь для сохранения лога")
    
output_log = output_log[::-1] + '/output.log'
backup_log = input_log + '.bak'

with open(input_log, 'r') as file:
    lines = file.readlines()

with open(backup_log, 'w') as file:
    file.writelines(lines)
    
log_lines = lines[2:]

headers_line = log_lines[0]

headers = headers_line.split()
headers = headers[0::2]

for header in headers:
    for i in lines:
        i.



print(headers)

with open(output_log, 'w') as file:
    file.writelines(log_lines)
    
    
    
