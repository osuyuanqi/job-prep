from pub_module import *
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

# **********************************************
# 268. Missing Number
# **********************************************
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	a=0
	for i in range(len(nums)+1):
		a+=i
	return a-sum(nums)
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	for i in range(len(nums)):
		if i not in nums:
			return i
# math
def missingNumber(nums: list[int]) -> int:
	n = len(nums)
	return (n)*(n+1)//2-sum(nums)
# slower
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	for i in nums:
		nums.add(i)
	for i in range(len(nums)+1):
		if i not in nums:
			return i
# **********************************************
# 387. First Unique Character in a String
# **********************************************
def firstUniqChar(s: str) -> int:
	dic,arr={},{}
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]]=1
			arr[s[i]]=i
		else:
			dic[s[i]]+=1
	# print(dic,arr)
	for k,v in dic.items():
		# print(k,v)
		if v==1:
			return arr[k]
	return -1
# store a list in dic
def firstUniqChar(s: str) -> int:
	dic={}
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]]=[1,i]
		else:
			dic[s[i]]=2
	# print(dic,arr)
	for k,v in dic.items():
		if v!=2:
			return v[1]
	return -1
# **********************************************
# 108. Convert Sorted Array to Binary Search Tree
# **********************************************

def sortedArrayToBST(nums: list[int]) -> [TreeNode]:
    if len(nums)==0: return None
    mid = len(nums)//2
    root=TreeNode(nums[mid])
    # print(root)
    root.left=self.sortedArrayToBST(nums[:mid])
    root.right=self.sortedArrayToBST(nums[mid+1:])
        
    return root
# **********************************************
# 21. Merge Two Sorted Lists
# **********************************************
def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
		# same object, one pointer move, another pointer stay
        dummy=p=ListNode(-1)
        while list1 and list2:
            if list1.val>list2.val:
                dummy.next=list2
                list2=list2.next
            else:
                dummy.next=list1
                list1=list1.next
            dummy=dummy.next
        if list1:
            dummy.next=list1
        if list2:
            dummy.next=list2
        return p.next

# **********************************************
# 350. Intersection of Two Arrays II
# **********************************************
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
	dic,res={},[]
	for i in range(len(nums1)):
		if nums1[i] not in dic:
			dic[nums1[i]]=1
		else:
			dic[nums1[i]]+=1
	# print(dic)
	for i in range(len(nums2)):
		if nums2[i] in dic and dic[nums2[i]]!=0:
			res.append(nums2[i])
			dic[nums2[i]]-=1
	# print(dic)
	return res

# **********************************************
# 121. Best Time to Buy and Sell Stock
# note: wait for maxprof, sell once
# **********************************************
# get the min till now
# update res only when profits bigger
def maxProfit(prices: list[int]) -> int:
	res,buy=0,prices[0]
	for i in range(len(prices)):
		if prices[i]<buy:
			buy=prices[i]
		if prices[i]-buy>res:
			res=prices[i]-buy
	return res

if __name__=="__main__":
	print('tst')
	# 217. Contains Duplicate
	# nums = [1,2,3,1]
	# print(containsDuplicate(nums))

	# 268. Missing Number
	# nums=[9,6,4,2,3,5,7,0,1]
	# print(missingNumber(nums))

	# 387. First Unique Character in a String
	# s = "aabbc"
	# print(firstUniqChar(s))

	# 350. Intersection of Two Arrays II
	# nums1 = [4,9,5]; nums2 = [9,4,9,8,4]
	# print(intersect(nums1,nums2))

	# 121. Best Time to Buy and Sell Stock
	# prices = [7,1,5,3,6,4]
	# print(maxProfit(prices))