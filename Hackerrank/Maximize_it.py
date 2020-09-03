"""
inputs 
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

output
206
"""

from itertools import product

def func(x):
    return pow(x,2)

k, m = input("").split()
lists = []
temp_list = []
max_value = 0

for _ in range(int(k)):
    temp_list = list(map(int, input("").split()))
    temp_list.pop(0)
    lists.append(temp_list)

all_lists = list(product(*lists))

for i in range(len(all_lists)):
    total = 0
    for j in all_lists[i]:
        total += func(j)
    
    result = int(m) % total
    if result > max_value:
        max_value = result
    
print(max_value)