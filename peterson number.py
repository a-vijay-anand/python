import math
num = int(input("Enter a number: "))
num_str = str(num)
total=0
for val in num_str:
    total +=math.factorial(int(val))
if(total==num):
    print("It is peterson number")
else:
    print("It is not a peterson number")