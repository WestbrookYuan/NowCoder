balance = 0
value = {"A1": 2, "A2": 3, "A3": 4, "A4": 5, "A5": 8, "A6": 6}

def initialization(string: str):
    products = {"A1": 0, "A2": 0, "A3": 0, "A4": 0, "A5": 0, "A6": 0}
    money = {"1": 0, "2": 0, "5": 0, "10": 0}
    [r, product_init, money_init] = string.split(" ")
    product_init = product_init.split("-")
    money_init = money_init.split("-")
    keys = list(products.keys())
    for i in range(len(keys)):
        products[keys[i]] = int(product_init[i])
    keys = list(money.keys())
    for i in range(len(keys)):
        money[keys[i]] = int(money_init[i])
    print("S001:Initialization is successful")
    return products, money





def pay_money(string: str):
    global balance
    [p, coin] = string.split(" ")

    if coin not in ["1", "2", "5", "10"]:
        return "E002:Denomination error"
    elif money["1"] + 2 * money["2"] < int(coin) and coin in ["5", "10"]:
        return "E003:Change is not enough, pay fail"
    elif not any(products.values()):
        return "E005:All the goods sold out"
    else:
        balance = int(coin)
        return "S002:Pay success,balance=%d" % balance




def buy_products(string: str):
    global balance
    [b, item] = string.split(" ")
    if item not in products:
        return "E006:Goods does not exist"
    elif products[item] == 0:
        return "E007:The goods sold out"
    elif balance < products[item]:
        return "E008:Lack of balance"
    else:
        balance -= value[item]
        products[item] -= 1
        return "S003:Buy success,balance=%d" % balance




def return_coin():
    global balance
    tens, fives, twos, ones = 0, 0, 0, 0
    if balance == 0:
        return "E009:Work failure"
    print(balance)
    while balance > 0:
        if balance >= 10 and money["10"] > 0:
            balance -= 10
            money["10"] -= 1
            tens += 1
        elif balance >= 5 and money["5"] > 0:
            balance -= 5
            money["5"] -= 1
            fives += 1
        elif balance >= 2 and money["2"] > 0:
            balance -= 2
            money["2"] -= 1
            twos += 1
        elif balance >= 1 and money["1"] > 0:
            balance -= 2
            money["2"] -= 1
            ones += 1
        else:
            balance -= 1
    print('1 yuan coin number={}'.format(ones))
    print('2 yuan coin number={}'.format(twos))
    print('5 yuan coin number={}'.format(fives))
    print('10 yuan coin number={}'.format(tens))





def check(string: str):
    [q, type] = string.split(" ")
    if type == "0":
        for i in products:
            print("%s %d %d" % (i, value[i], products[i]))
    else:
        for i in money:
            print('%s yuan coin number=%d'%(i, money[i]))



inputs = "r 22-18-21-21-7-20 3-23-10-6;c;q 0;p 1;b A6;c;b A5;b A1;c;q 1;p 5;".split(";")

for i in inputs[:-1]:
    if i[0] == "r":
        products, money = initialization(i)
    elif i[0] == "p":
        pay_money(i)
    elif i[0] == "b":
        buy_products(i)
    elif i[0] == "c":
        return_coin()
    elif i[0] == "q":
        check(i)
