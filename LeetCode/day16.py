# **********************************************
# 724. Find Pivot Index
# **********************************************

# method1: math tip
def pivotIndex(self, nums: list[int]) -> int:
    total = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        rsum = total - lsum - nums[i]
        if lsum == rsum:
            return i
        lsum += nums[i]
    return -1

# method2: use function
def pivotIndex(self, nums: list[int]) -> int:
    #Error case 
    if nums == None: return -1
    #base case 
    if len(nums) == 0: return -1 
    if len(nums) == 1: return 0
    if len(nums) == 2: return -1
    #iterations 
    for i in range(len(nums)):
        left_sum = sum(nums[0:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1

if __name__ == "__main__":
	print('test')