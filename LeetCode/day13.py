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
    # not while since the rest linkedlist no need append node one by one
    if list1:
        p.next = list1
    if list2:
        p.next = list2
    # also works
    # while list2:
    #     p.next = list2
    #     list2 = list2.next
    #     p = p.next
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

# **********************************************
# badge pass validation
# **********************************************
'''
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"] 
]

Expected output: ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]

Other test cases:

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

Expected output: ["Paul"], ["Paul"]

n: length of the badge records array
'''

badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"] 
]

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

badge_records_4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

def inproperty_action(badge_records):
    #     collection of inproper action
    in_exit,in_enter = [],[]
    
    #unpackage the input: badge_records
    my_dict = {}
    for i in badge_records:
        name, action = i
        if name not in my_dict:
            if action == "exit":
                in_exit.append(name)
            my_dict[name] = action
        else:
            if action != my_dict[name]:
                if action == "enter" and my_dict[name] == "exit":
                    in_enter.append(name)
                my_dict[name] = action
    return set(in_exit),set(in_enter)
print(inproperty_action(badge_records_4))