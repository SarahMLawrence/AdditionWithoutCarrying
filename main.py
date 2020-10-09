def additionWithoutCarrying(param1, param2):
    a = str(param1)
    b = str(param2)

    longNum = ""
    shortNum = ""
    if len(a) >= len(b):
        longNum = a[::-1]
        shortNum = b[::-1]
    else:
        longNum = b[::-1]
        shortNum = a[::-1]
    result = ""
    count = 0

    for char in longNum:
        if count >= len(shortNum):
            result += char
        else:
            num = int(char) + int(shortNum[count])
            count += 1
            if num > 9:
                result += str(num - 10)
            else:
                result += str(num)
    return int(result[::-1])
