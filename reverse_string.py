def reversed(s):
    if len(s) < 2:
        return s
    return s[1:] + s[0]

print reversed("abc")
