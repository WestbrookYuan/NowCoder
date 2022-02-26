def findcontinousnumbers(string:str):
    numbers =[]
    temp = []
    for i in string:
        if i.isdigit():
            temp.append(i)
        else:
            if temp:
                numbers.append(temp)
                temp = []
    if temp:
        numbers.append(temp)
    maxlength = 0
    for i in numbers:
        if len(i) >= maxlength:
            maxlength = len(i)
    for i in numbers:
        if len(i) == maxlength:
            print("".join(i), end="")
    print("," + str(maxlength))

findcontinousnumbers("a8a72a6a5yy98y65ee1r2")