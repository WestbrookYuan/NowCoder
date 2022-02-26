def validPassword(password):
    if len(password) <= 8:
        return "NG"
    lower_check, number_check, upper_check, other_check = 0, 0, 0, 0
    for i in password:
        if ord("a") <= ord(i) <= ord("z"):
            lower_check = 1
        elif ord("0") <= ord(i) <= ord("9"):
            number_check = 1
        elif ord("A") <= ord(i) <= ord("Z"):
            upper_check = 1
        else:
            other_check = 1
    if lower_check + number_check + upper_check + other_check < 3:
        return "NG"

    for i in range(len(password) - 3):
        if len(password.split(password[i:i + 3])) >= 3:
            return "NG"

    return "OK"


while True:
    try:
        password = input()
        print(validPassword(password))
    except:
        break
