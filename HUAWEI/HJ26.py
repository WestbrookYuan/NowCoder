def sort(string: str):
    unsorted_alphas = ""
    for i in string:
        if i.isalpha():
            unsorted_alphas += i
    sorted_alphas = sorted(unsorted_alphas, key=str.upper)
    print(sorted_alphas)
    sorted_string = ""
    index = 0
    for i in string:
        if i.isalpha():
            sorted_string += sorted_alphas[index]
            index += 1
        else:
            sorted_string += i
    return sorted_string


while True:
    try:
        string = input()
        print(sort(string))
    except:
        break
