def solve(s):
    result = ''
    for i in range(0, len(s)):
        if i == 0:
            result = result + s[i].upper()
        elif s[i] != ' ' and s[i-1] == ' ':
            c = s[i].upper()
            result = result + c
        else:
            result = result + s[i]
    return result