number_to_alpha = {"1": "1", "abc": "2", "def": "3", "ghi": "4", "jkl": "5", "mno": "6", "pqrs": "7", "tuv": "8",
                   "wxyz": "9"}

Upp_to_low = {}

for i in range(65, 65 + 26):
    if chr(i) == "Z":
        Upp_to_low[chr(i)] = "a"
    else:
        Upp_to_low[chr(i)] = chr(i + 33)


def converter(password: str):
    s = ""
    for i in password:
        if i.isupper():
            s += Upp_to_low[i]
        elif i.isdigit():
            s += i
        else:
            for key in number_to_alpha.keys():
                if i in key:
                    s += number_to_alpha[key]
    return s


while True:
    try:
        print(converter(input().strip()))

    except:
        break
