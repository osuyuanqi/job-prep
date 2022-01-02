# **********************************************
# 344 Reverse String
# **********************************************

def reverseString(s: list[str]) -> None:
    a = len(s)
    for i in range(a//2):
        if s[i] != s[a-i-1]:
             s[i], s[a-i-1] = s[a-i-1], s[i]

s = ["h","e","l","l","o"]
# reverseString(s)
# print(s)

# **********************************************
# 412: fizzBuzz
# Method1: mod operation is slower
# **********************************************

def fizzBuzz1(n:int)->list[str]:
    rst = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            rst.append("FizzBuzz")
        elif i % 3 == 0:
            rst.append("Fizz")
        elif i % 5 == 0:
            rst.append("Buzz")
        else:
            rst.append(str(i))
    return rst
# **********************************************
# Method2: replace operation is faster
# **********************************************

def fizzBuzz2(n:int)->list[str]:
    f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
    arr = [str(i) for i in range(1, n + 1)]
    for i in range(2, n, 3):
        arr[i] = f
    for i in range(4, n, 5):
        arr[i] = b
    for i in range(14, n, 15):
        arr[i] =fb
    return arr

# print(fizzBuzz1(15))
# print(fizzBuzz2(15))

# **********************************************
# 136. Single Number:
# every element appears twice except for one. 
# Find that single one.
# **********************************************

def singleNumber1(nums: list[int]) -> int:
    dupl={}
    for i in nums:
        if i not in dupl:
            dupl[i] = i
        else:
            dupl.pop(i)
    return [i for i in dupl.keys()][0]
def singleNumber2(nums: list[int]) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res
# nums = [4,1,2,1,2]