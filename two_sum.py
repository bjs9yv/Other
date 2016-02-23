def twoSum(nums, target):
    ans = []
    for index0, n0 in enumerate(nums):
        if index0 == len(nums)-1:
            break
        for index1, n1 in enumerate(nums):
            if index1 <= index0:
                continue
            if n0+n1 == target:
                ans.append(index0+1)
                ans.append(index1+1)
                return ans
    return ans

print twoSum([2,3,5,7,9,15],9)
