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
# ***********************************************

def maxProfit(prices: list[int]) -> int:
    buy,profits=prices[0],0
    for i in range(1,len(prices)):
        if prices[i]<buy:
            buy = prices[i]
        if prices[i]- buy > profits:
            profits = prices[i]- buy
    return profits


if __name__=="__main__":
    print('tst')
    # 101. Symmetric Tree
    # nums = [3,2,4]; target = 7
    # print(twoSum(nums,target))

    # 121. Best Time to Buy and Sell Stock
    # prices =  [7,6,4,3,1]
    prices=[7,1,5,3,6,4]
    print(maxProfit(prices))