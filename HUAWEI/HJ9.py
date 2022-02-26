x = input()

x = x[::-1]
xs = []
for i in x:
    if i not in xs:
        xs.append(i)

x = int("".join(xs))

print(x)