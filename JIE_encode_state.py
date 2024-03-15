import os

def read_file_to_array(filename):
    with open(filename, 'r') as file:
        # 讀取檔案並以空格分割，儲存成陣列
        array = file.read().split()
    return array
def hex_to_binary(hex_number):
    # 將十六進位數轉換成十進位整數
    return bin(int(hex_number, 16))[2:].zfill(32)

    

LSB = input('LSB path\n')
CSB = input('CSB path\n')
MSB = input('MSB path\n')
output_file_path =input('output file name\n')
if not os.path.splitext(output_file_path)[1] != '':
    output_file_path = output_file_path + '.txt'

# 讀取每個檔案
LSB_array = read_file_to_array(LSB)
CSB_array = read_file_to_array(CSB)
MSB_array = read_file_to_array(MSB)

counts = {'R': 0,'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
weights = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'R': 1}
weight_list = []
total_weight = 0

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

with open(output_file_path, 'w') as output_file:
    for i in range(len(LSB_array)):
        if (i + 1) % 1024 == 0:
            weight_list.append(total_weight)
            total_weight = 0

        a, b, c = map(hex_to_binary, (LSB_array[i], CSB_array[i], MSB_array[i]))
        for j, vals in enumerate(zip(a, b, c)):
            char = mapping.get(vals)
            if char:
                output_file.write(char)
                total_weight += weights[char]
                counts[char] += 1

    
    
   

            

