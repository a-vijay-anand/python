n = int(input())
roll_numbers = []
for i in range(n):
    roll_numbers.append(int(input()))
search_roll = int(input())
found = False
for i in range(n):
    if roll_numbers[i] == search_roll:
        print("Roll Number Found at Index", i)
        found = True
        break
if not found:
    print("Roll Number Not Found")