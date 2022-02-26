def find(string: str):
    number = int(string)
    if str(number ** 2)[-len(string):] == str(number):
        return True
    else:
        return False


while True:
    try:
        n = int(input())
        numbers = [i for i in range(n + 1)]
        vaild = 0
        for i in numbers:
            if find(str(i)):
                vaild += 1
            else:
                continue
        print(vaild)
    except:
        break
