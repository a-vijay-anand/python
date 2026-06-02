n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
target = int(input())
last = -1
for i in range(n):
    if arr[i] == target:
        last = i
print(last)