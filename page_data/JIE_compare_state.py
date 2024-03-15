

count = 0
ori_e=""
ret_e=""
original = input('original\n')
retention = input('after retention\n')
with open(original, 'r') as file1, open(retention, 'r') as file2:
        ori = file1.read()
        ret = file2.read()
for i in range(len(ori)):
    if ori[i] != ret[i]:
        count+=1
        ori_e += ori[i]
        ret_e += ret[i]
print('ori_error: ',ori_e)
print('ret_error: ',ret_e)
print(count)