n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
maximum = arr[0]
for i in range(1, n):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)