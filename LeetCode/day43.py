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

if __name__=="__main__":
    print('test')
    # 13
    # s = "MCMXCIV"
    # print(romanToInt(s))