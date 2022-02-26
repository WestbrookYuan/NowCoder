import sys

lines = []
for line in sys.stdin:
    lines.append(line)

string = lines[0].strip()
char = lines[1].strip()
count = 0

for i in string.lower():
    if i == char.lower():
        count += 1
print(count)