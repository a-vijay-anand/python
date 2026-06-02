isbn = input("Enter 10-digit ISBN: ")
total = 0
for i in range(10):
    total += (i + 1) * int(isbn[i])
if total % 11 == 0:
    print("Valid ISBN")
else:
    print("Invalid ISBN")