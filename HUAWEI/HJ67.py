import itertools


def find(numbers:list, number:int):
    allpossible = itertools.permutations(numbers)
    operator = ["+","-","*","/"]
    s = True
    for numbers in list(allpossible):
        first = []
        for i in operator:
            first.append(eval(str(numbers[0]) + i + str(numbers[1])))
        second = []
        for i in first:
            for j in operator:
                second.append(eval(str(i)+j+str(numbers[2])))
        last = []
        for i in second:
            for j in operator:
                last.append(eval(str(i)+j+str(numbers[3])))
        if float(number) in map(float, last):
            s = True
            break
        else:
            s = False
    if s:
        return "true"
    else:
        return "false"
print(find([7,2,1,0],24))