from itertools import permutations
import sys
def split_list(l, n):
  # 將list分割 (l:list, n:每個matrix裡面有n個元素)
  for idx in range(0, len(l), n):
    yield l[idx:idx+n]

def min_sum(p_wl,c_wl):
   total = 0
   for i in range(len(p_wl)):
      total += abs(weights.get(p_wl[i], 0) - weights.get(c_wl[i], 0))
   return total

A = input('first path\n')
B = input('second path\n')
part = 32684
max = 0
out_min=[]
out_max=[]
weights = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'R': 1}
min = sys.maxsize

with open(A, 'r') as file:
   a = file.read()
with open(B, 'r') as file:
   b = file.read()
a_split = []
b_split = []
b_split_index = [0,1,2,3]
a_split = list(split_list(a, part)) 
b_split = list(split_list(b, part)) 
b_split_index = list(permutations(b_split_index))


for i in range(0,len(b_split_index)): 
   
   total = 0
   tmp = ""
   for j in range(0,len(b_split_index[i])):
      total += min_sum(a_split[j],b_split[b_split_index[i][j]])
      
      tmp += b_split[b_split_index[i][j]]
      
   if i == 0:
      print('original is :',total)
   if total < min:
      out_min = tmp
      min = total
   if total > max:
      out_max = tmp
      max = total
print("min is :", min)
print("max is :", max)

with open('min.txt', 'w') as file:
   file.write(out_min)
with open('max.txt', 'w') as file:
   file.write(out_max)