from pub_module import *
# **********************************************
# 21. Merge Two Sorted Lists
# similar to the merge part of mergesort
# **********************************************

def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    p = dummy = ListNode(-1)
    while list1 and list2:
        if list1.val < list2.val:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
    if list1:
        p.next = list1
    if list2:
        p.next = list2
    return dummy.next
# **********************************************
# 2. Add Two Numbers
# carry usage for new digit
# **********************************************

def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    p1, p2 = l1, l2
    p = dummy = ListNode(-1)
    carry = 0
    while p1 or p2 or carry > 0 :
        val = carry
        if p1:
            val += p1.val
            p1 = p1.next
        if p2:
            val += p2.val
            p2 = p2.next
        carry = val // 10
        val = val % 10
        p.next = ListNode(val)
        p = p.next
    return dummy.next

# **********************************************
# 144. Binary Tree Preorder Traversal
# **********************************************

# recursive way
def preorderTraversal(self, root: [TreeNode]) -> list[int]:
    output = []
    def recurs(root):
        if root:
            output.append(root.val)
            recurs(root.left)
            recurs(root.right)
    recurs(root)
    return output

# iterative way,stack->First in, First out
def preorderTraversal(self, root: [TreeNode]) -> list[int]:
	if root == None:
	    return []
	stack, output = [root], []
	while stack:
	    root = stack.pop()          
	    if root:
	        output.append(root.val)
	        if root.right:
	            stack.append(root.right)
	        if root.left:
	            stack.append(root.left)     
	return output