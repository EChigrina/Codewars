def my_parse_int(string):
    return int(string) if len([x for x in string.strip() if not x.isdigit()]) is 0 else "NaN"
