n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
found = False
for num in arr:
    if num % 2 == 0:
        found = True
        break
if found:
    print("Even Number Found")
else:
    print("Even Number Not Found")