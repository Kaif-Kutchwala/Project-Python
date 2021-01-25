def twoSum(nums, target):
    complements = {}
    for i in range(len(nums)):
        if nums[i] in complements:
            return [i,complements[nums[i]]]
        else:
            complements[target - nums[i]] = i   


print(twoSum([2,11,15,3],14))
print(twoSum([4,10,7,21],25))
print(twoSum([3,2,7,4],9))
print(twoSum([20,10,11,2],30))

