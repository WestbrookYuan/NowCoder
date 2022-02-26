def shownumbers(string: str):
    shows = []
    i = 0
    while i < len(string):
        if string[i].isdigit():
            shows.append("*")
            for j in range(i, len(string)):
                if string[j].isdigit():
                    shows.append(string[j])
                else:
                    shows.append("*")
                    shows.append(string[j])
                    i = j
                    break
                if j == (len(string) - 1):
                    shows.append("*")
                    return "".join(shows)
        else:
            shows.append(string[i])
        i += 1
    return "".join(shows)

print(shownumbers("1**3"))
print(shownumbers("Y1^*6**26*"))
