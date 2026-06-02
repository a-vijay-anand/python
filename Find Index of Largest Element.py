n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
max_index = 0
for i in range(1, n):
    if arr[i] > arr[max_index]:
        max_index = i
print(max_index)