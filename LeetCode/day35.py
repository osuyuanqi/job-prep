# **********************************************
# 62. Unique Paths
# **********************************************
# **********************************************
# 26. Remove Duplicates from Sorted Array
# **********************************************
def removeDuplicates(nums: list[int]) -> int:
	if len(nums)==0: return 0
	j=0
	for i in range(len(nums)):
		if nums[i]!=nums[j]:
			nums[j+1]=nums[i]
			j+=1
	return j+1
# **********************************************
# 1. Two Sum
# **********************************************
def twoSum(nums: list[int], target: int) -> list[int]:
	memo={}
	for i in range(len(nums)):
		if target-nums[i] in memo:
			return [memo[target-nums[i]],i]
		else:
			memo[nums[i]]=i

if __name__=="__main__":
	print('tst')
	
	# 26. Remove Duplicates from Sorted Array
	# nums=[0,0,1,1,1,2,2,3,3,4]
	# print(removeDuplicates(nums))

	# 1. Two Sum
	# nums=[2,7,11,15];target=9
	# print(twoSum(nums,target))