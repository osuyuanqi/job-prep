# **********************************************
# 167. Two Sum II - Input Array Is Sorted
# sorted tips
# **********************************************

# way1: hash
def twoSum(numbers: list[int], target: int) -> list[int]:
    dic={}
    for i in range(len(numbers)):
        if target - numbers[i] in dic:
            return [dic[target - numbers[i]]+1,i+1]
        dic[numbers[i]] = i
    return []

# way2: double pointer,since it's sorted array
def twoSum(numbers: list[int], target: int) -> list[int]:
    l,h = 0, len(numbers) - 1
    while numbers[l] + numbers[h]!= target and l < h:
        # print(numbers[l],numbers[h],l,h)
        if target - numbers[l] > numbers[h]:
            l+=1
        else:
            h-=1
    else:
        # print(l,h)
        return [l+1, h+1] if l!= h else []
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))
# **********************************************
# 15. 3Sum
# **********************************************
