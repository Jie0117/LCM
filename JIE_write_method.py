import os
import sys
from itertools import permutations
def page2array(page):
    array = page.split()
    return array
def read_file_to_array(filename):
    with open(filename, 'r') as file:
        content = file.read().split('\n')
    return content
def hex_to_binary(hex_number):
    # 將十六進位數轉換成十進位整數
    return bin(int(hex_number, 16))[2:].zfill(32)
def split_list(l, n):
  # 將list分割 (l:list, n:每個matrix裡面有n個元素)
  for idx in range(0, len(l), n):
    yield l[idx:idx+n]
def min_sum(p_wl,c_wl):
   total = 0
   for i in range(len(p_wl)):
      total += abs(weights.get(p_wl[i], 0) - weights.get(c_wl[i], 0))
   return total
def text_to_hex_files(input_text, file_path):
    # 初始化三个累积字符串
    LSB, CSB, MSB = '', '', ''
    
    # 遍历输入文本中的每个字符，根据映射关系填充三个累积字符串
    for char in input_text:
        if char in char_to_binary:
            lsb, csb, msb = char_to_binary[char]
            LSB += lsb
            CSB += csb
            MSB += msb

    # 将累积的二进制字符串保存到文件
    def save_to_file(binary_str, file_path):
        with open(file_path, 'a') as file:
            for i in range(0, len(binary_str), 32):  # 每32位处理一次
                # 获取下一个32位的二进制字符串，不足32位的在前面填充0
                chunk = binary_str[i:i+32].ljust(32, '0')
                # 将32位二进制转换成十六进制
                hex_number = '0x' + format(int(chunk, 2), '08X')
                file.write(hex_number + ' ')
            file.write('\n')
    save_to_file(LSB, file_path)
    save_to_file(CSB, file_path)
    save_to_file(MSB, file_path)
            

part = 32684
a_split = []
b_split = []
b_split_index = [0,1,2,3]

b_split_index = list(permutations(b_split_index))
counts = {'R': 0,'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
weights = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'R': 1}

current_WL = ""
last_WL = ""
char_to_binary = {
    'R': ('1', '1', '1'),
    'A': ('0', '1', '1'),
    'B': ('0', '0', '1'),
    'C': ('0', '0', '0'),
    'D': ('0', '1', '0'),
    'E': ('1', '1', '0'),
    'F': ('1', '0', '0'),
    'G': ('1', '0', '1'),
}
mapping = {
    ('1', '1', '1'): 'R',
    ('0', '1', '1'): 'A',
    ('0', '0', '1'): 'B',
    ('0', '0', '0'): 'C',
    ('0', '1', '0'): 'D',
    ('1', '1', '0'): 'E',
    ('1', '0', '0'): 'F',
    ('1', '0', '1'): 'G',
    
}
in_file_path = input('input file_path\n')
output_file_path =input('output file name\n')
if not os.path.splitext(output_file_path)[1] != '':
    output_file_path = output_file_path + '.txt'
lines = read_file_to_array(in_file_path)
for i in range(0,len(lines)):
    print(i)
    if i%3==0:
        LSB = lines[i]
        LSB_array = page2array(LSB)
    if i%3==1:
        CSB = lines[i]
        CSB_array = page2array(CSB)
    if i%3==2:
        MSB = lines[i]
        MSB_array = page2array(MSB)
    if i % 3 == 2:
        current_WL = ''
        for k in range(0,len(LSB_array)):
            a, b, c = map(hex_to_binary, (LSB_array[k], CSB_array[k], MSB_array[k]))
            for j, vals in enumerate(zip(a, b, c)):
                char = mapping.get(vals)
                current_WL += char
        if last_WL == '':
            last_WL=current_WL
            with open(output_file_path,'a') as f:
                f.write(LSB)
                f.write('\n')
                f.write(CSB)
                f.write('\n')
                f.write(MSB)
                f.write('\n')
        else:
            out_min=''
            min = min = sys.maxsize
            for l in range(0,len(b_split_index)): 
                total = 0
                tmp = ''
                a_split = list(split_list(last_WL, part)) 
                b_split = list(split_list(current_WL, part)) 
                #print(len(a_split))
                for m in range(0,len(b_split_index[l])):
                    total += min_sum(a_split[m],b_split[b_split_index[l][m]])
                    tmp += b_split[b_split_index[l][m]]
                if l == 0:
                    ori = total
                if total < min:
                    out_min = tmp
                    min = total
            last_WL = current_WL
            print(f"ans= {ori-min}")
            
            text_to_hex_files(out_min,output_file_path)

                    
        


        

    
    
   

            

