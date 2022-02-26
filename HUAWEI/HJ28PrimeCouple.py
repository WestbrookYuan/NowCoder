def is_prime(number):
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return 0

    return 1


def match(i):
    for j in range(n):
        if array[i][j] == 1 and not visited[j]:
            visited[j] = True
            if matched[j] == -1 or match(matched[j]):
                matched[j] = i
                return True
    return False


while True:
    try:
        n = int(input())
        numbers = list(map(int, input().strip().split()))
    except:
        break

    else:
        evens, odds = [], []
        for i in numbers:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        m = len(odds)
        n = len(evens)
        array = [[-1 for j in range(n)] for i in range(m)]

        for i, x in enumerate(odds):
            for j, y in enumerate(evens):
                array[i][j] = is_prime(x + y)
        matched = [-1 for i in range(n)]
        counter = 0

        for i in range(m):
            visited = [False for k in range(n)]
            if match(i):
                counter += 1
        print(counter)
