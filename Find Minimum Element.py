n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
minimum = arr[0]
for i in range(1, n):
    if arr[i] < minimum:
        minimum = arr[i]
print(minimum)