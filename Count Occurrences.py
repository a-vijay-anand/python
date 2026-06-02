n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
target = int(input())
count = 0
for num in arr:
    if num == target:
        count += 1
print(count)