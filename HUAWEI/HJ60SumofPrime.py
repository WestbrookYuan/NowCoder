def isPrime(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def check(number: int):
    for i in range(1, number // 2 + 1):
        j = number - i
        if isPrime(i) and isPrime(j):
            x, y = i, j
    print(x)
    print(y)
    return


while True:
    try:
        number = int(input())
        check(number)
    except:
        break