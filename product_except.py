def product_at_i_except_i(arr):
    ans_arr = []
    for index,value in enumerate(arr):
        product = 1
        for i,x in enumerate(arr):
            if i == index:
                continue
            ans_arr[index]
        ans_arr[index] = product
    return ans_arr

l = [1,7,3,4]
ans = [84,12,28,21]
assert(product_at_i_except_i(l) == ans)








