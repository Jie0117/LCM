# 映射關係
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

def text_to_hex_files(input_text, lsb_path, csb_path, msb_path):
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
        with open(file_path, 'w') as file:
            for i in range(0, len(binary_str), 32):  # 每32位处理一次
                # 获取下一个32位的二进制字符串，不足32位的在前面填充0
                chunk = binary_str[i:i+32].ljust(32, '0')
                # 将32位二进制转换成十六进制
                hex_number = '0x' + format(int(chunk, 2), '08X')
                file.write(hex_number + '\n')
    save_to_file(LSB, lsb_path)
    save_to_file(CSB, csb_path)
    save_to_file(MSB, msb_path)

# 示例使用
input_path = input('path: ')
with open(input_path,'r')as in_:
    input_text = in_.read()
    lsb_path = "LSB.txt"
    csb_path = "CSB.txt"
    msb_path = "MSB.txt"
    text_to_hex_files(input_text, lsb_path, csb_path, msb_path)




