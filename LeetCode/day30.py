# ***********************************************
# 189. Rotate Array
# ***********************************************

# faster->nums[:] change original
def rotate(nums: list[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k %=len(nums)
	nums[:] = nums[-k:]+nums[:-k]

# pop original array->change,append into the tail	
def rotate(nums: list[int], k: int) -> None:
	n=len(nums)
	k %=n
	for i in range(len(nums)-k):
		x=nums.pop(0)
		nums.append(x)

if __name__=="__main__":
	print('tst')
	
	# remove the last k elems,prepend to the begin
	nums = [1,2,3,4,5,6]; k =11
	print(rotate(nums,k))
	print(nums)