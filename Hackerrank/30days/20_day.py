import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total = 0
for _ in range(n):
    numSwaps = 0

    for i in range(n-1):
        if a[i] > a[i + 1]:
            aux = 0
            aux = a[i]
            a[i] = a[i + 1]
            a[i + 1] = aux
            numSwaps += 1
            total += 1
    
    if numSwaps == 0:
        break

print(f'Array is sorted in {total} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')