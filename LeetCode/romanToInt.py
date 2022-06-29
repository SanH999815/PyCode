def romanToInt(s: str):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    b = False
    for i in range(len(s)):
        if b:
            b = False
            continue
        if s[i] == 'M':
            result += 1000
        elif s[i] == 'D':
            result += 500
        elif i != len(s) - 1 and s[i] == 'C' and s[i + 1] == 'D':
            result += 400
            b = True
        elif i != len(s) - 1 and s[i] == 'C' and s[i + 1] == 'M':
            result += 900
            b = True
        elif s[i] == 'C':
            result += 100
        elif s[i] == 'L':
            result += 50
        elif i != len(s) - 1 and s[i] == 'X' and s[i + 1] == 'C':
            result += 90
            b = True
        elif i != len(s) - 1 and s[i] == 'X' and s[i + 1] == 'L':
            result += 40
            b = True
        elif s[i] == 'X':
            result += 10
        elif s[i] == 'V':
            result += 5
        elif i != len(s) - 1 and s[i] == 'I' and s[i + 1] == 'X':
            result += 9
            b = True
        elif i != len(s) - 1 and s[i] == 'I' and s[i + 1] == 'V':
            result += 4
            b = True
        elif s[i] == 'I':
            result += 1
    return result


print('-' * 50)
