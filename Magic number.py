num = int(input("Enter a number: "))

while num > 9:
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    num = s

if num == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")