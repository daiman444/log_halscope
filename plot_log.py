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
    
with open(input_log, 'r') as file:
    lines = file.readlines()
    
log_lines = lines[2:]

log_lines_output = []

headers_line = log_lines[0]

lines_num =  len(log_lines)
lines_counter = 0

print(lines_num)

headers = headers_line.split()
headers = headers[0::2]

print(headers)

while lines_counter <= lines_num:
    



for line in log_lines:
    for header in headers:
        header = str(header)
        new_line = line.replace(header, "")
    #log_lines_output.append(new_line)

with open(output_log, 'w') as file:
    file.writelines(log_lines)
    
    
    
