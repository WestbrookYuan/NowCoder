import sys

for line in sys.stdin:
    a = line
a = a.strip().split(" ")

index = len(a) - 1
print(len(a[index]))