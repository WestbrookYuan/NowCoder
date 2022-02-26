def isIP(string:str):
    ip = string.strip().split(".")
    if len(ip) !=4:
        return "NO"
    for i in ip:
        if not i.isdigit():
            return "NO"
        if int(i) > 255:
            return "NO"
        if len(i) >= 4:
            return "NO"
        if i.startswith("0") and len(i) > 1:
            return "NO"
    return "YES"


print(isIP("10.138.15.1"))