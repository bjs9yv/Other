# Given an unsorted integer array, find the first missing positive integer.
def missing_int(l):
    expecting = []
    missing = len(l) + 1
    for x in range(0,len(l)):
        expecting.append(False)
    for y in l:
        try:
            expecting[y] = True
        except IndexError:
            missing = min(missing,y-1)
    for i,z in enumerate(expecting):
        if not z:
            return i
    return len(l)
    
if __name__ == "__main__":
    print missing_int([0])
    print 'missing: ', missing_int([0,1,5,7])
    print 'missing: ', missing_int([0,1,2])
    print 'missing: ', missing_int([0,1,2,7])
