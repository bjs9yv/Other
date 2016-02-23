def move_zeros(nums):
    count = 0
    indexs = []
    for n in nums:
        if n == 0:
            count+=1
    for x in range(0,count):
        nums.remove(0)
        nums.append(0)
    return nums

print move_zeros([0,1,2,1,1,2,0,5])
print move_zeros([0,0,1])
