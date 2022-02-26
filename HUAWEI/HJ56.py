def factors(number: str):
    number = int(number)
    if number == 1:
        return []
    factors_list = []
    for i in range(1, number):
        if number % i == 0:
            factors_list.append(i)
    return factors_list


while True:
    try:
        n = int(input())
        count = 0
        for j in range(2, n + 1):
            m = sum(factors(j))
            if m == j:
                count += 1
        print(count)
    except:
        break
