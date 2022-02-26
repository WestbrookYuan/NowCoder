def record(string:str):
    numbers = list(map(int, string.split()))
    positive = 0
    positive_count = 0
    negative_count = 0
    for i in numbers:
        if i > 0:
            positive += i
            positive_count += 1
        elif i < 0:
            negative_count += 1
    if positive_count > 0:
        mean = positive/positive_count
        return str(negative_count) + " " + str(round(mean, 1))
    else:
        return str(negative_count) + " " + "0"

while True:
    try:
        n = int(input())
        print(record(input()))
    except:
        break