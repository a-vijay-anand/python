import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num + 1))
if root * root == num + 1:
    print("Sunny Number")
else:
    print("Not a Sunny Number")