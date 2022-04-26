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
	
if __name__=="__main__":
	print('tst')
	
	# 104. Maximum Depth of Binary Tree
	# root = [3,9,20,None,None,15,7],# 3
	# maxDepth(root)
	
	# 371. Sum of Two Integers
	# a,b=2,3	
	# print(getSum(a,b))

	# 169. Majority Element
	# nums = [3,2,1,2,4,2]
	# print(majorityElement(nums))