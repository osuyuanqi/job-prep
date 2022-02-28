# **********************************************
# 167. Two Sum II - Input Array Is Sorted
# **********************************************

def twoSum(numbers: list[int], target: int) -> list[int]:
    dic={}
    for i in range(len(numbers)):
        if target - numbers[i] in dic:
            return [dic[target - numbers[i]]+1,i+1]
        dic[numbers[i]] = i
    return []
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))

# **********************************************
# 15. 3Sum
# **********************************************
