def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def printprime(n):
    for i in range(2, n + 1):
        if isprime(i):
            print(i, end=" ")


if __name__ == "__main__":
    n = eval(input("Enter a number for n: "))
    printprime(n)
