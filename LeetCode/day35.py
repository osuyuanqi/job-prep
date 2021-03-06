from pub_module import ListNode
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
# **********************************************
# 172. Factorial Trailing Zeroes
# **********************************************
def trailingZeroes(self, n: int) -> int:
	ct=0
	while n//5!=0:
		n//=5
		# not 1,e.g.10!=(5*2)*9*..*5*..*1,leading 2 is what we want
		ct+=n
	return ct

# **********************************************
# 141. Linked List Cycle
# **********************************************
# way1: double pointer
def hasCycle(head: [ListNode]) -> bool:
    fast,slow=head,head
    # AND, since fast.next must have value, then fast.next.next maybe none
    while fast and fast.next:
        # fast.next.next may be none after loop
        fast=fast.next.next
        slow=slow.next
        # judgement when done, since they're exactly same at the begining
        if fast==slow:
            return True
    return False

# way2: hash
def hasCycle(head: [ListNode]) -> bool:
	s=set()
	while True:
	    if head not in s:
	        s.add(head)
	    else:
	        return True
	    if head:
	        head=head.next
	    else:
	        return False

# **********************************************
# 66. Plus One
# **********************************************
def plusOne(digits: list[int]) -> list[int]:
	s=''.join(map(str,digits))
	it=str(int(s)+1)
	res=list(map(int,it))
	return res
	
# **********************************************
# 88. Merge Sorted Array
# requirement: change original nums1,return nothing
# **********************************************
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	nums1[:m+n]=nums1[:m]+nums2
	# nums1[:].sort()-> not works
	nums1.sort() #works
# one line 
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
	nums1[:]=sorted(nums1[:m]+nums2)

if __name__=="__main__":
	print('tst')
	
	# 26. Remove Duplicates from Sorted Array
	# nums=[0,0,1,1,1,2,2,3,3,4]
	# print(removeDuplicates(nums))

	# 1. Two Sum
	# nums=[2,7,11,15];target=9
	# print(twoSum(nums,target))

	# 66. Plus One
	# digits = [1,2,9]
	# print(plusOne(digits))

	# 88. Merge Sorted Array
	# nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
	# print(merge(nums1,3,nums2,3))
	# print(nums1)
