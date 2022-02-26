result = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "EOF": 0, "PRIVATE": 0}


def check_mask(mask: str):
    mask = list(map(int, mask.split(".")))

    if len(mask) < 4 or '' in mask:
        result["EOF"] += 1
        return
    val = (mask[0] << 24) + (mask[1] << 16) + (mask[2] << 8) + mask[3]
    s = bin(val)[2:]
    start_0 = s.find("0")
    start_1 = s.rfind("1")
    if start_0 - start_1 == 1 and start_0 != -1 and start_1 != -1:
        return True
    else:
        result["EOF"] += 1
        return False


def check_ip_type(ip: str):
    ip = ip.split(".")
    if len(ip) < 4 or '' in ip:
        result["EOF"] += 1
        return
    ip = list(map(int, ip))

    if 1 <= ip[0] < 127:
        result["A"] += 1
    elif 128 <= ip[0] < 192:
        result["B"] += 1
    elif 192 <= ip[0] < 224:
        result["C"] += 1
    elif 224 <= ip[0] < 240:
        result["D"] += 1
    elif 240 <= ip[0] < 256:
        result["E"] += 1

    if ip[0] == 10 or (ip[0] == 172 and 16 <= ip[1] < 32) or (ip[0] == 192 and ip[1] == 168):
        result["PRIVATE"] += 1
    return


def judge(line):
    ip, mask = line.strip().split("~")
    if ip[0] == 0 or ip[0] == 127:
        return
    if check_mask(mask):
        check_ip_type(ip)


import sys

for line in sys.stdin:
    judge(line)

for i in result.values():
    print(i, end=' ')
