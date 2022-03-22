# ***********************************************
# 187. Repeated DNA Sequences
# ***********************************************
        
def findRepeatedDnaSequences(s: str) -> list[str]:
    l = set();dic = []
    for i in range(len(s)-9):
        a = s[i:i+10]
        if a not in l:
            l.add(a)
        else:
            dic.append(a)
    # print(dic,l)
    return set(dic)

if __name__=="__main__":
    print('tst')
    
    # 187. Repeated DNA Sequences
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(findRepeatedDnaSequences(s))