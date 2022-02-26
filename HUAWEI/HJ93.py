def add(fives, threes, temp):
    if len(temp) == 0:
        if fives == threes:
            return True
        else:
            return False
    else:
        return add(fives + temp[0], threes, temp[1:]) or add(fives, threes + temp[0], temp[1:])


def splitnumbers():
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    fives = []
    threes = []
    rests = []
    for i in numbers:
        if i % 5 == 0:
            fives.append(i)
        elif i % 3 == 0:
            threes.append(i)
        else:
            rests.append(i)
    a = add(sum(fives), sum(threes), rests)
    print("true" if a else "false")
