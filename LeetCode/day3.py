# **********************************************
# 171. Excel Sheet Column Number
# no need to convert list
# st = "ZYA"
# a = list(columnTitle)[::-1]
# print(st[::-1])
# for i in range(3, 0,-1):
#     print(i)
# **********************************************

def titleToNumber(columnTitle: str) -> int:
    rst = 0
    add = 1
    for i in range(len(columnTitle)-1, -1, -1):
        # print(i,columnTitle[i],add)
        rst += (ord(columnTitle[i]) - 64) * add
        add *= 26
    return rst
# print(titleToNumber('AB'))

# **********************************************
# 169. Majority Element
# find the majority element
# nums = [2,2,1,1,5] wrong result in Method1
# **********************************************

# Method1: Boyer–Moore Majority vote
def majorityElement(nums: list[int]) -> int:
    major, times = 0, 0 
    for i in nums:
        # print(major, i, times,"before")
        if times == 0:
            major = i
        # any other elements cutting down majority, to 0
        if i == major:
            times += 1
        else:
            times -=1
        # print(major, i, times,"after")
    return major 
# Method2: Hash
def majorityElement1(nums):
    dic = {}
    maxV = 0
    for i,j in enumerate(nums):
        # print(i,j)
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
    for k,v in dic.items():
        # print(k,v)
        if v > maxV:
            maxV = v
            major= k
    return major
# [2,2,1,1,1,2,2], [3,3,4], [6,5,5]
# print(majorityElement(nums))

# **********************************************
# 13. Roman to Integer
# add first, then the double subtract logic
# **********************************************

def romanToInt(s: str) -> int:
    rela = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev, total = 0, 0
    for i in range(len(s)):
        curr = rela[s[i]]
        if curr > prev:
            # print(i,curr,prev,rela[s[i]])
            # prev should be substracted twice
            total += curr - 2 * prev
        else:
            # sum directly [first]
            total += curr
        # [first] is given to prev,but it has be added
        prev = curr
    return total
# s = "LX";s = "XL";s = "MCMXCIV"
# print(romanToInt(s))