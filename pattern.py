def pattern_boolean(pattern,string):
    words = string.split()
    d = {}
    for i,p in enumerate(pattern):
        d[p] = words[i]
pattern_boolean('abba','dog cat cat dog')  
