# 13. Roman to Integer
def romanToInt(s: str) -> int:
    dic={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res=dic[s[0]]
    for i in range(1,len(s)):
        if dic[s[i]]<=dic[s[i-1]]:
            res+=dic[s[i]]
        else:
            res+=dic[s[i]]-2*dic[s[i-1]]
    return res
# 169. Majority Element
def majorityElement(nums):
    dic={}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    maj,res=1,nums[0]
    print(dic)
    for k,v in dic.items():
        if v>maj:
            maj=v
            res=k
            # print(k,v)
    return res

# 217. Contains Duplicate
def containsDuplicate(nums)->bool:
    return len(set(nums))!=len(nums)
def containsDuplicate(nums)->bool:
    _set=set()
    for i in nums:
        if i in _set:
            return True
        _set.add(i)
    return False

# 242. Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    if len(s)!=len(t): return False
    dic={}
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    # print(dic)
    for j in t:
        # print(j)
        if j not in dic:
            return False
        else:
            dic[j]-=1
            if dic[j]<0:
                return False
    return True
def isAnagram(s: str, t: str) -> bool:
    return sorted(s)==sorted(t)
    
# 49. Group Anagrams
from collections import defaultdict 
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dic={}
    for word in strs:
        # sorted anagram should be consistent
        sortedWord=''.join(sorted(word))
        if sortedWord not in dic:
            dic[sortedWord] = [word]
        else:
            dic[sortedWord].append(word)
    # res = defaultdict(list)
    return dic.values()
if __name__=="__main__":
    print('success')

    # 13
    # s = "MCMXCIV"
    # print(romanToInt(s))

    # 169
    # nums = [2,2,1,1,1,2,2]
    # print(majorityElement(nums))
    
    # 217
    # nums = [1,2,3,1]
    # print(containsDuplicate(nums))

    # 242
    # s = "anagram"; t = "nagaram"
    # print(isAnagram(s,t))

    # 49
    # strs = ["eat","tea","tan","ate","nat","bat"]
    # print(groupAnagrams(strs))