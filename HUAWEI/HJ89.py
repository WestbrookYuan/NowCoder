import itertools


def find24(string: str):
    compute = ["+", "//", "*", "-"]
    dict = {"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 1, "2": 2}
    convert = string.strip().split()
    if "joker" in convert or "JOKER" in convert:
        return "ERROR"
    for i in range(len(convert)):
        convert[i] = dict[convert[i]]
    orders = itertools.permutations(convert, 4)
    results = []
    for time in orders:
        first = {}
        for i in compute:
            first[str(time[0]) + i + str(time[1])] = eval(str(time[0]) + i + str(time[1]))
        second = {}
        for i in first:
            for j in compute:
                second[str(i) + j + str(time[2])] = eval(str(first[i]) + j + str(time[2]))

        result = {}
        for i in second:
            for j in compute:
                result[str(i) + j + str(time[3])] = eval(str(second[i]) + j + str(time[3]))
        results.append(result)
    for i in results:
        for oper in i:
            if i[oper] == 24:
                return oper.replace("//", "/").replace("13","K").replace("1","A").replace("11","J").replace("12","L")
    return None


print(find24("4 2 K A"))
