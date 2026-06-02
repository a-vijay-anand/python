num = int(input("Enter a number: "))
num_str = str(num)

total = 0

for i in range(len(num_str)):
    total += int(num_str[i]) ** (i + 1)

if total == num:
    print("Disarium Number")
else:
    print("Not a Disarium Number")