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

# ***********************************************
# Molecular lab intv: 
# count the pair of stocks
# ***********************************************
        
def count(n,ar):
    dic = {}
    for i in range(len(ar)):
        if ar[i] in dic:
            dic[ar[i]]+=1
        else:
            dic[ar[i]]=1
    # print(dic)
    res=0
    for i in dic:
        # print(res,dic[i])
        res+=dic[i]//2
    return res

if __name__=="__main__":
    print('tst')
    
    # 187. Repeated DNA Sequences
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(findRepeatedDnaSequences(s))
    # count pair
    n=9; ar=[10,20,20,10,50,10,10,20,30]
    print(count(n,ar))