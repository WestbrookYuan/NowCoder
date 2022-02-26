import sys


def sorted_process(l, r):
    count = 0
    dic = {}
    for i in r:
        for j in l:
            if i in j:
                if i not in dic:
                    dic[i] = [j]
                else:
                    dic[i].append(j)
    output = []
    for i in r:
        if i in dic:
            output.append(i)
            output.append(str(len(dic[i])))
            count += 2
            temp = []
            for j in dic[i]:
                id1 = [str(x) for x, y in enumerate(l) if y == j]
                if len(id1) > 1:
                    for iss in id1:
                        if iss not in temp:
                            temp.append(iss)
                            temp.append(j)
                            break
                else:
                    temp.append(str(l.index(j)))
                    temp.append(j)
            count += len(temp)
            temp = ' '.join(temp)
            output.append(temp)
            print(temp)
    output = str(count) +" " + " ".join(output)
    print(output)


# for line in sys.stdin:
#     L = input().strip().split(" ")[1:]
#     R = set(input().strip().split(" ")[1:])
#     R = sorted(R)

print(sorted_process(l="15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123".strip().split(" ")[1:],
                     r=sorted(set("5 6 3 6 3 0".strip().split(" ")[1:]))))
