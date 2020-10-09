def additionWithoutCarrying(param1, param2):
    a = str(param1)
    b = str(param2)

    longer = ""
    shorter = ""
    if len(a) >= len(b):
        longer = a[::-1]
        shorter = b[::-1]
    else:
        longer = b[::-1]
        shorter = a[::-1]
    result = ""
    count = 0

    for char in longer:
        if count >= len(shorter):
            result += char
        else:
            num = int(char) + int(shorter[count])
            count += 1
            if num > 9:
                result += str(num - 10)
            else:
                result += str(num)
    return int(result[::-1])
