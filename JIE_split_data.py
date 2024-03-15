def split_list(l, n):
  # 將list分割 (l:list, n:每個matrix裡面有n個元素)
  for idx in range(0, len(l), n):
    yield l[idx:idx+n]

def save_chunks(chunks, base_filename):
    # 將chunks儲存到不同的文件中
    for i, chunk in enumerate(chunks):
        filename = f"{base_filename}_part{i}.txt"
        with open(filename, 'w') as f:
            f.write(chunk)
    print(f"Chunks saved to files with base name {base_filename}")

B = input('split WL path: ') 
base_filename = "output_chunk"
with open(B, 'r') as file:
   b = file.read()

chunks = split_list(b, 32768)

save_chunks(chunks, base_filename)