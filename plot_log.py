#!/usr/bin/env python3

import string

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

log_lines_output = []

headers_line = log_lines[0]

headers = headers_line.split()
headers = headers[0::2]

print(headers)

for line in log_lines:
    for header in headers:
        header = str(header)
        line = line.replace(header, '')
        log_lines_output.append(line)

"""for header in headers:
    for line in log_lines:
        header = str(header) + ' '
        line = line.replace(header, '')
        log_lines_output.append(line)"""
        
#print(log_lines_output)

with open(output_log, 'w') as file:
    file.writelines(log_lines_output)
    
    
    
