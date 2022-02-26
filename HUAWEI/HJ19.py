errors = {}
output = []
while True:
    try:
        line = input()
        line = line.strip().split('\\')
        recorded = line[-1]
        recorded = recorded.split(' ')
        line_number = recorded[1]
        if len(recorded[0]) > 16:
            address = recorded[0][-16:]
        else:
            address = recorded[0]
        key = address + ' ' + line_number
        if key in errors:
            errors[key] += 1
        else:
            errors[key] = 1



    except:
        break

for i, j in errors.items():
    output.append("%s %d" % (i, j))
for i in output[-8:]:
    print(i)