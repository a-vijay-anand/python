num = int(input("Enter a number: "))

result = str(num) + str(num * 2) + str(num * 3)

if len(result) == 9 and sorted(result) == list("123456789"):
    print("Fascinating Number")
else:
    print("Not a Fascinating Number")