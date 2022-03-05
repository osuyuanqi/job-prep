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
# numbers = [2,7,11,15]
# target = 9
# print(twoSum(numbers,target))
# **********************************************
# 15. 3Sum
# **********************************************

# **********************************************
# 7. Reverse Integer
# **********************************************
def reverse(x:int)->int:
    sign = 1 if x > 0 else -1
    rst = sign * int(str(abs(x))[::-1])
    return 0 if rst > 2 ** 31 - 1 or rst < -2**31 else rst
def reverse1(x:int)->int:
    res,sign = 0, 0
    if x > 0:
        sign = 1
    else:
        sign = -1
        x = -x
    while x:
        res = res * 10 + x % 10
        x = x // 10
        # print(x,res)
    return 0 if res > pow(2,31) else sign*res
# a = -123
# print(reverse1(a))

# **********************************************
# 125. Valid Palindrome
# **********************************************

# way1:short version
def isPalindrome(s: str) -> bool:
    s= [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]
s = "A man, a plan, a canal: Panama" 

# way2:shrink
def isPalindrome(s: str) -> bool:
    s = [i for i in s.lower() if i.isalnum()]
    l,h = 0, len(s)-1
    while l<h:
        if s[l]!= s[h]:
            return False
        l+=1
        h-=1
    return True   
print(isPalindrome(s))

# **********************************************
# 88. Merge Sorted Array
# **********************************************

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        nums1[m + i] = nums2[i]
    # NOT nums1=nums1.sort(),since the left nums1 doesn't influence the right nums1 in memory address
    nums1.sort()

if __name__ == '__main__':
    print('tst')