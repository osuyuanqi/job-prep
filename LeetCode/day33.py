# **********************************************
# 217. Contains Duplicate
# **********************************************
def containsDuplicate(nums: list[int]) -> bool:
	s=set()
	for i in nums:
		if i in s:
			return True
		s.add(i)
	return False
def containsDuplicate(nums: list[int]) -> bool:
	return len(set(nums))!=len(nums)

if __name__=="__main__":
	print('tst')
	# 217. Contains Duplicate
	# nums = [1,2,3,1]
	# print(containsDuplicate(nums))