def finder(string: str, i: int, j: int):
    while (i >= 0 and j < len(string) and string[i] == string[j]):
        i -= 1
        j += 1
    return string[i + 1:j]


def middlefind(string: str):
    password = ""
    for i in range(len(string)):
        temp = finder(string, i, i)
        if len(temp) > len(password):
            password = temp
        temp = finder(string, i, i + 1)
        if len(temp) > len(password):
            password = temp
    print(len(password))


while True:
    try:
        string = input()
        middlefind(string)
    except:
        break