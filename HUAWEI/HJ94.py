def summary(members: str, counts: str):
    members = members.split()
    members_counter = {}
    for i in members:
        members_counter[i] = 0
    counts = counts.split()
    invaild = 0
    for i in counts:
        if i in members_counter:
            members_counter[i] += 1
        else:
            invaild += 1
    for i in members_counter:
        print(i + " : " + str(members_counter[i]))

    print("Invalid :", invaild)


summary("A B C D", "A D E CF A GG A B")
