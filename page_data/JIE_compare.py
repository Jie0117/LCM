def hex_to_binary(hex_number):
    # 將十六進位數轉換成十進位整數
    return bin(int(hex_number, 16))[2:].zfill(32)
def read_file_to_array(filename):
    with open(filename, 'r') as file:
        # 讀取檔案並以空格分割，儲存成陣列
        array = file.read().split()
    return array



count = 0

original = input('original\n')
retention = input('after retention\n')
ori_page = read_file_to_array(original)
ret_page = read_file_to_array(retention)
for i in range(len(ori_page)):
    tmp_o = hex_to_binary(ori_page[i])
    tmp_r = hex_to_binary(ret_page[i])
    for j in range(len(tmp_o)):
        if tmp_o[j] != tmp_r[j]:
            count += 1
print(count)