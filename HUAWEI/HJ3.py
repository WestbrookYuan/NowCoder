while True:
    try:
        n = input()
        numbers = []
        for i in range(int(n)):
            numbers.append(int(input()))
        uniq = set(numbers)
        numbers= list(uniq)
        numbers.sort()
        for i in numbers:
            print(i)
    except:
        break
