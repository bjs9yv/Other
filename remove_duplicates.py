def remove_dups(s):
    d = {}
    for c in s:
        if c in d.keys():
            s = s.replace(c,'',1)
        d[c] = 'seen this character now'
    return s

assert remove_dups('a55bcc') == 'a5bc'
assert remove_dups('abc') == 'abc'
