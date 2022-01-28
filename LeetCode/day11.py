# **********************************************
# 151. Reverse Words in a String
# space is ''
# **********************************************

def reverseWords(s):
    s = s[::-1]
    s1 = s.split(' ')
    s2 = []
    for i in range(len(s1)):
        if s1[i] == '':
            continue
        s1[i] = s1[i][::-1]
        s2.append(s1[i])
    return ' '.join(s2)
s = '  he   wod'
print(reverseWords(s))

# **********************************************
# 217. Contains Duplicate
# **********************************************

# method1: dic, hash
def containsDuplicate(nums: list[int]) -> bool:
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = i
        else:
            return True
    return False

# method 2: set,hash
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

