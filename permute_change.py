def permute_change(amount, denom):
    answer = 0
    if amount == 0:
        return 0
    if amount < 0:
        raise ValueError
    for index, coin in enumerate(reversed(denom)):
        if index != 0:
            denom.pop()
        denom_copy = denom[:]
        print amount, denom
        answer += permute_change_helper(amount,denom_copy)
    return answer

def permute_change_helper(a,d):
    ans = 0 
    if len(d) == 0:
        return 0
    while a - d[-1] < 0:
        print a, d
        d.pop()
    a = a - d[-1]
    if a == 0:
        return 1
    for i,c in enumerate(d): 
        if i != 0:
            d.pop()
        print a,d
        ans += permute_change_helper(a,d)
    return ans

assert(permute_change(4,[1,2]) == 3)
assert(permute_change(4,[1,2,3]) == 4)
assert(permute_change(5,[1,3,5]) == 3)

