num = int(input("Enter a number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
rev = int(str(num)[::-1])

if is_prime(num) and is_prime(rev) and num != rev:
    print("Emirp Number")
else:
    print("Not an Emirp Number")