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
    prices=[1,2,3,4,5]
    print(maxProfit(prices))