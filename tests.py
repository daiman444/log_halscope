headers = ['ahc.arc-ok', 'joint.3.motor-pos-cmd', 'ahc.arc-ok', 'ahc.torch-up']
headers_list = []

for i in headers:
    i_counter = 1
    if i not in headers_list:
        headers_list.append(i)
    else:
        i = i + '_' + str(i_counter)
        headers_list.append(i)
        
print(headers_list)

headers_dict = {}

for i in headers_list:
    headers_dict[i] = []
    
print(headers_dict)

for i in headers:
    print(headers_dict[i])

#headers = [[ahc.arc-o],[joint.3.motor-pos-cmd], [ahc.arc-ok', 'ahc.torch-up]]

#print(headers)