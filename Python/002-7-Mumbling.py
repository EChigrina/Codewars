def accum(s):
    string = ""
    for num in range(len(s)):
        string += s[num].upper() + s[num].lower()*(num) + '-'
    return string[:-1]
