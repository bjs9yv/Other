def pre_compute(target):
    n1_max = int(target/2)
    pairs = []
    for x in range(1,n1_max+1):
        pairs.append((x,target-x))
    return pairs

def binary_search(nums,target):
    high = len(nums)
    low = 0
    old_guess = -1
    while True:
        middle = int((high+low)/2)
        guess = nums[middle]
        if guess == old_guess:
            return -1
        old_guess = guess
        if guess == target:
            return middle
        if guess < target:
            low = middle
        if guess > target:
            high = middle
        
def two_sum(nums,target):
    answer_pairs = pre_compute(target)
    i0 = -1
    i1 = -1
    for pair in answer_pairs:
        i0 = binary_search(nums,pair[0])
        if i0 != -1:
            i1 = binary_search(nums,pair[1])
        else:
            continue
        if i1 != -1:
            return [(i0+1,i1+1)]

l1 = [2,3,7,8,9,11]
print two_sum(l1,12)
