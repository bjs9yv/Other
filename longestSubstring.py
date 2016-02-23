def get_longest_string(the_string):
    if len(the_string) == 1:
        return s
    l = [] # stores the longest unique string the character in position i can make
    winning = ''
    for index,char in enumerate(the_string):
        if index == 0:
            l.append(char)
        elif index == 1:
            if char not in l[0]:
                l[0] += char
            l.append(char)
        else:
            for x in range(0,index):
                if l[x][-1] == '-':
                    continue
                elif char not in l[x]:
                    l[x] += char
                else:
                    l[x] += '-'
                if len(l[x].rstrip('-')) > len(winning):
                    winning = l[x].rstrip('-')
            l.append(char)
    winner = winning
    return winner

string1 = 'abcabcd'
string2 = 'abbccdeff'
assert(get_longest_string(string1) == 'abcd')
assert(get_longest_string(string2) == 'cdef')
