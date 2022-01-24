# **********************************************
# 1. Two Sum
# hash,dic comes into mind
# test cases:
# [2,7,11,15]->9;[3,2,4]->6;[3,3]->6
# **********************************************

def twoSum(nums: list[int], target: int) -> list[int]:
        for i_idx,i in enumerate(nums):
            for j_idx,j in enumerate(nums):
                if i == target - j and i_idx != j_idx:
                    return i_idx,j_idx
        return [None]

def twoSum1(nums: list[int], target: int) -> list[int]:
    result = {}
    for idx,i in enumerate(nums):
        if target - i in result:
            return [result[target - i],idx]
        result[i] = idx

nums = [2,7,11,15]; target = 18
print(twoSum1(nums,target))



# **********************************************
# **********************************************
