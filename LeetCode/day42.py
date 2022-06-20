# 125. Valid Palindrome
def isAlNum(c):
    return (ord('a')<=ord(c)<=ord('z')) or         (ord('A')<=ord(c)<=ord('Z')) or         (ord('0')<=ord(c)<=ord('9'))
def isPalindrome(s: str) -> bool:
    l,r=0,len(s)-1
    while l<r:
        while l<r and not isAlNum(s[l]):
            l+=1
        while l<r and not isAlNum(s[r]):
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
        l+=1
        r-=1
    return True 

# 121. Best Time to Buy and Sell Stock
# keep track the min
def maxProfit(prices:list[int])->int:
    minV,res=prices[0],0
    # print(res)
    for i in range(1,len(prices)):
        if prices[i]<minV:
            minV=prices[i]
        if prices[i]-minV>res:
            res=prices[i]-minV
    return res
# two pointers&sliding window
def maxProfit(prices:list[int])->int:
    l,r=0,1
    maxP=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            # keep the maxP,
            maxP=max(maxP,profit)
        else:
            # l should be the min,but may not maxP,e.g.[3,7,2,4]=>max=7-3=4,though l=2
            l=r
        r+=1
    return maxP

# 20. Valid Parentheses
def isValid(s:str)->bool:
    stack=[]
    closeToOpen={")":"(","]":"[","}":"{"}
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1]==closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack

# 33. Search in Rotated Sorted Array
def search(nums:list[int],target:int)->int:
    # l,r=0,len(nums)-1
    minV=nums[0];minI=0
    # step1: find mid point
    for i in range(len(nums)):
        if nums[i]<minV:
            minI=i
            break
    # step2: decide direction
    l,r=0,len(nums)-1
    if target==nums[minI]:
        return minI
    # left part
    elif nums[minI]<target<=nums[len(nums)-1]:
        l=minI
    # right part
    else:
        r=minI
        
    # step3: bs,== only 1 elem
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
if __name__=="__main__":
    print('test')
    # 125
    # s = "A man, a plan, a canal: Panama"
    # print(isPalindrome(s))
    # 121
    # prices = [7,1,5,3,6,4]
    # print(maxProfit(prices))

    # 20
    # s = "{[]}"    
    # print(isValid(s))
    # 33
    # nums = [3,1]; target = 3
    # print(search(nums,target))