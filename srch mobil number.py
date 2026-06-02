n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
search_num = int(input())
for i in range(n):
    if numbers[i] == search_num:
        print("Number Found at Index", i)
        break
else:
    print("Number Not Found")