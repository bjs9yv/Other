# given a number as a string, 
# what are the maximum number of ways it can be decoded if a = 0,...,z = 25

def nums_alpha(string):
    if len(string) < 2:
        return 1
    s0 = string[0]
    s1 = string[1]
    if s0 == '2':
        if int(s1) <= 5:
            s0 += '-'
        else:
            s0 += '+'
    ways_to_make_num_digits = [0] * (len(string)+1)
    ways_to_make_num_digits[1] = 1
    ways_to_make_num_digits[2] = {'0':1,'1':2,'2-':2,'2+':1}.get(s0,0)
    for n in range(3,len(ways_to_make_num_digits)):
        ways_to_make_num_digits[n] = ways_to_make_num_digits[n-1] + ways_to_make_num_digits[n-2]  
    return ways_to_make_num_digits[-1]
    
print nums_alpha('151')

