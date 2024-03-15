u32RandomIni = [
    0x0158001a, 0x441e9b63, 0xacc2f72e, 0x336386a5, 0xe36ca8e1, 0x851f8504, 0xa9dd54b8, 0x1b09a292,
    0x6be9836c, 0xe0071698, 0x09b13660, 0x00963742, 0x92605d74, 0x2019002e, 0x6a05d034, 0x3d57401f,
    0xb8cb5216, 0x00029840, 0x4a8801b9, 0x401f0052, 0xf8065020, 0x39179218, 0x00013001, 0xc8803121,
    0xca828f00, 0x7971001f, 0x004615c7, 0xd205694b, 0x1019006e, 0xb04a4f4c, 0x1d855bda, 0x00021290
]
def FT_get_seed(block, pg, ch, ce):
    # Calculate the initial seed value with bit manipulation and shifts
    seed = (block << 24) + (pg << 16) + (block << 8) + ((ce << 3) + ch)
    rIni = pg % 28 + (((ce << 3) + ch) + block) % 5
    shiftbit = pg % 32
    # Perform the rotation and bitwise OR with the selected random initialization value
    seed = (seed << shiftbit | seed >> (32 - shiftbit)) | u32RandomIni[rIni]
    return seed
def FT_scramble(seed, buffer):
    for i in range(len(buffer)):
        # Scramble the current element in the buffer with the seed
        buffer[i] = buffer[i] ^ seed
        # Update the seed for the next iteration
        seed += 0x35ACCA53
        seed = (seed << 1) | (seed >> 31) & 0xFFFFFFFF
def mem_write(data,output_path):
    data.split()
    with open(output_path,'a') as file:
        file.write('switch 2\n')
        file.write('log_level 5\n')
        file.write('allocDTAG\n')
        for i in range(0,len(data),4):  
            file.write(f"reg_mem_write 0 {i} 0x{data[i]} 0x{data[i+1]} 0x{data[i+2]} 0x{data[i+3]}\n")
            