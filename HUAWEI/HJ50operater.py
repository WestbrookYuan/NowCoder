def group(string: str):
    num, res = "", []
    for i, c in enumerate(string):
        if c.isdigit():
            num += c
        else:
            if num:
                res.append(num)
                num = ""
            if c == "-":
                if i == 0 or (string[i - 1] in "+-*/{[("):
                    num += c
                    continue
            res.append(c)

    if num:
        res.append(num)
    return res


def scan(string: str):
    lst = group(string)
    stack_numbers = []
    stack_operators = []

    for i in lst:
        if i not in "+-*/[]{}()":
            stack_numbers.append(i)
        elif i in "*/[{(":
            stack_operators.append(i)
        elif i in "+-":
            if len(stack_operators) == 0 or stack_operators[-1] in "([{":
                stack_operators.append(i)
            else:
                while stack_operators:
                    if stack_operators[-1] in "([{":
                        break

                    op = stack_operators.pop()
                    n2, n1 = stack_numbers.pop(), stack_numbers.pop()
                    stack_numbers.append(str(int(eval(n1 + op + n2))))
                stack_operators.append(i)
        elif i in ")]}":
            while stack_operators[-1] not in "([{":
                op = stack_operators.pop()
                n2, n1 = stack_numbers.pop(), stack_numbers.pop()
                stack_numbers.append(str(int(eval(n1 + op + n2))))
            stack_operators.pop()
    while stack_operators:
        op = stack_operators.pop()
        n2, n1 = stack_numbers.pop(), stack_numbers.pop()
        stack_numbers.append(str(int(eval(n1 + op + n2))))
    print(stack_numbers.pop())


while True:
    try:
        s = input()
        scan(s)
    except:
        break
