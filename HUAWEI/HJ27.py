line = input().strip().split()

number = line[0]

words = line[1:-2]

k = line[-1]
word = line[-2]
brothers = []
for i in words:
    if i != word:
        if sorted(i) == sorted(word):
            brothers.append(i)
    else:
        continue

print(len(brothers))
if int(k) > len(brothers):
    print()
else:
    print(sorted(brothers)[int(k) - 1])