# ***********************************************
# 1. Two Sum
# ***********************************************
def twoSum( nums: list[int], target: int) -> list[int]:
    memo = {}
    for i in range(len(nums)):
        if target - nums[i] in memo:
            return [memo[target - nums[i]],i]
        else:
            memo[nums[i]] = i

# ***********************************************
# 121. Best Time to Buy and Sell Stock
# one transaction
# ***********************************************
def maxProfit(prices: list[int]) -> int:
    buy,profits=prices[0],0
    for i in range(1,len(prices)):
        if prices[i]<buy:
            buy = prices[i]
        if prices[i]- buy > profits:
            profits = prices[i]- buy
    return profits

# ***********************************************
# 122. Best Time to Buy and Sell Stock II
# multiple transaction
# ***********************************************
def maxProfit(prices: list[int]) -> int:
    profits = 0
    for i in range(0,len(prices)-1):
        if prices[i]<prices[i+1]:
            profits+=prices[i+1]-prices[i]
    return profits
# ***********************************************
# 118. Pascal's Triangle
# ***********************************************
def generate(numRows: int) -> list[list[int]]:
    res = [[1]*i for i in range(1,numRows+1)]
    print(res)
    # e.g.5,i:0,1,2,3,4
    for i in range(numRows):
        # j:0,1,2,3
        for j in range(1,i):
            res[i][j] = res[i-1][j-1]+res[i-1][j]
    return res

# ***********************************************
# 7. Reverse Integer
# ***********************************************
# way1: string<->int
def reverse(x: int) -> int:
    sign= -1 if x<0 else 1
    res= sign * int(str(sign*x)[::-1])
    return 0 if  res > 2 ** 31 - 1 or res < - 2 ** 31 else res
# way2:%
def reverse(x: int) -> int:
    sign = 1 if x>0 else -1
    res= 0
    x *= sign
    while x!=0:
        res = res*10+x % 10
        x//=10
    return sign*res if res>-2**31 and res<2**31 - 1 else 0

if __name__=="__main__":
    print('tst')
    # 101. Symmetric Tree
    # nums = [3,2,4]; target = 7
    # print(twoSum(nums,target))

    # 121. Best Time to Buy and Sell Stock
    # prices =  [7,6,4,3,1]
    # prices=[7,1,5,3,6,4]
    # print(maxProfit(prices))

    # 122. Best Time to Buy and Sell Stock II
    # prices = [7,1,5,3,6,4]
    # prices=[1,2,3,4,5]
    # print(maxProfit(prices))

    # 118. Pascal's Triangle
    # numRows = 5
    # print(generate(numRows))
    
    # 7. Reverse Integer,[-2147483648,-321,321]
    # print(reverse(321))
