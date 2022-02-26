def compare():
    dic = {
        '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
        '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12,
        '2': 13, 'joker': 14, 'JOKER': 15
    }
    s1, s2 = input().split('-')
    lst1, lst2 = s1.split(), s2.split()
    L1, L2 = len(lst1), len(lst2)
    if L1 == L2:
        if dic[lst1[0]] > dic[lst2[0]]:
            print(s1)
        else:
            print(s2)
    else:
        if "joker JOKER" == s1 or "joker JOKER" == s2:
            print("joker JOKER")
        elif lst1.count(lst1[0]) == 4:
            print(s1)
        elif lst2.count(lst2[0]) == 4:
            print(s2)
        elif lst1.count(lst1[0]) == 4 and lst1.count(lst2[0]) == 4:
            if lst1[0] > lst2[0]:
                print(s1)
            else:
                print(s2)
        else:
            print("ERROR")