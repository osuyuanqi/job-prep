from pub_module import *
# **********************************************
# 104. Maximum Depth of Binary Tree
# **********************************************
# recursive
def maxDepth(root: [TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
# iterative
def maxDepth(root: [TreeNode]) -> int:
	if not root:
		return 0
	stack = [root]
	depth = 0
	while stack:
		new_stack = []
		for node in stack:
			print(node)
			RC, LC = node.right, node.left
			if RC: new_stack.append(RC)
			if LC: new_stack.append(LC)
		depth += 1
		stack = new_stack
		# explore the new_stack to the end, depth first
		print(new_stack)
	return depth

# **********************************************
# 283. Move Zeroes
# **********************************************
# slower
def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(0)
                nums.append(0)
# swap #0
def moveZeroes(nums: list[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	index = 0
	for i in range(len(nums)):
		# print(nums[i],nums[index],index,nums)

		if nums[i] != 0:
			# exchange the first index of 0
			nums[index], nums[i] = nums[i], nums[index]
			# move to the next index
			index += 1

# **********************************************
# 371. Sum of Two Integers
# **********************************************
def getSum(a: int, b: int) -> int:
	mask=0xFFFFFFFF
	
	# 000 also seen as 0, since compare decimal 
	while b!=0:
		# ^->XOR
		sum1=(a^b)&mask
		# since only 1&1=1
		carry=((a&b)<<1)&mask
		a=sum1
		b=carry
	return a if a< 0x7FFFFFFF else ~(a^mask)

# **********************************************
# 206. Reverse Linked List
# **********************************************
# iterative
def reverseList(head: [ListNode]) -> [ListNode]:
	prev,curr=None,head
	while curr:
		temp=curr.next
		curr.next=prev
		prev=curr
		curr=temp
	return prev
# recursive
def reverseList(head: [ListNode]) -> [ListNode]:
	if head==None or head.next==None: return head
	rev=self.reverseList(head.next)
	# head is a pointer->point to the first elem
	head.next.next=head
	head.next=None
	return rev

# **********************************************
# 169. Majority Element
# import condition: assume the majority elem appears
# more than n//2 times
# **********************************************
# way1: hash
def majorityElement(nums: list[int]) -> int:
	dic,count={},0
	for i in nums:
		if i not in dic:
			dic[i]=1
		else:
			dic[i]+=1
	# print(dic,maxV,i)
	maxV,maxI=0,0
	for i,j in dic.items():
		# print(i,j,maxV)
		if j>maxV:
			maxV=j
			maxI=i
	return maxI
# improve
def majorityElement(nums: list[int]) -> int:
	dic,maxK,maxV={},nums[0],0
	for i in range(len(nums)):
		if nums[i] not in dic:
			dic[nums[i]]=1
		else:
			dic[nums[i]]+=1
			if dic[nums[i]]>maxV:
				maxK=nums[i]
				maxV=dic[nums[i]]
	return maxK
# Boyer–Moore Majority Vote Algorithm
def majorityElement(nums: list[int]) -> int:
	ma,count=nums[0],1
	for i in range(len(nums)):
		if nums[i]==ma:
			count+=1
		else:
			count-=1
			print(i,nums[i],count)
			if count==0:
				ma=nums[i]
				count=1
	return ma
# **********************************************
# 237. Delete Node in a Linked List
# **********************************************
def deleteNode(node):
	"""
	:type node: ListNode
	:rtype: void Do not return anything, modify node in-place instead.
	"""
	node.val=node.next.val
	node.next= node.next.next

# **********************************************
# 13. Roman to Integer
# **********************************************
def romanToInt(s: str) -> int:
	dic ={"I":1,"V":5,"X":10,"L":50,"C":100
,"D":500,"M":1000}
	prev,res=s[0],dic[s[0]]
	for i in range(1,len(s)):
		# print(dic[prev],dic[s[i]],i)
		if dic[prev]>dic[s[i]] or dic[prev]==dic[s[i]]:
			res+=dic[s[i]]
		else:
			# before calculation, the smaller value has calculatd once and become the previous one's next
			res+=dic[s[i]]-2*dic[prev]
		prev=s[i]
	return res
# brilliant way: only concern about +/- current branch
def romanToInt(s: str) -> int:
	dic ={"I":1,"V":5,"X":10,"L":50,"C":100
,"D":500,"M":1000}
	res=0
	for i in range(len(s)-1):
		if dic[s[i+1]]>dic[s[i]]:
			res-=dic[s[i]]
		else:
			res+=dic[s[i]]
	return res+dic[s[len(s)-1]]
# **********************************************
# 122. Best Time to Buy and Sell Stock II
# **********************************************

# only concern current and next
def maxProfit(prices: list[int]) -> int:
	profit=0
	for i in range(len(prices)-1):
		if prices[i+1]-prices[i]>0:
			profit+=prices[i+1]-prices[i]
	return profit
# pass every elem
def maxProfit(prices: list[int]) -> int:
	buy,profit=prices[0],0
	for price in prices:
		if price>buy:
			profit+=price-buy
		# though jumped, also passed the latest price
		buy=price
	return profit
# **********************************************
# 242. Valid Anagram
# **********************************************
def isAnagram(s: str, t: str) -> bool:
	dic ={}
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]]=1
		else:
			dic[s[i]]+=1
	# print(dic)
	for i in range(len(t)):
		if t[i] not in dic:
			return False
		dic[t[i]]-=1
	for k,v in dic.items():
		if v!=0:
			return False
	return True

if __name__=="__main__":
	print('tst')
	
	# 104. Maximum Depth of Binary Tree
	# root = [3,9,20,None,None,15,7],# 3
	# maxDepth(root)

	# 283. Move Zeroes
	# nums=[1,0,0,3,12]
	# print(moveZeroes(nums))
	# print(nums)

	# 371. Sum of Two Integers
	# a,b=2,3	
	# print(getSum(a,b))

	# 169. Majority Element
	# nums = [3,2,1,2,4,2]
	# print(majorityElement(nums))

	# 13. Roman to Integer
	# s = "III"
	# print(romanToInt(s))	

	# 122. Best Time to Buy and Sell Stock II
	# prices = [7,1,5,3,6,4]
	# print(maxProfit(prices))

	# 242. Valid Anagram
	# s = "rat"; t = "car"
	# print(isAnagram(s,t))