from pub_module import *
# **********************************************
# 328.Odd Even Linked List
# append separately and connected by tail
# **********************************************
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def oddEvenList(self, head: [ListNode]) -> [ListNode]:
    oddDummy,evenDummy = odd, even = ListNode(0), ListNode(0)
    isOdd = True
    while head:
        if isOdd:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even = even.next
        isOdd = not isOdd
        head = head.next
    even.next = None
    odd.next = evenDummy.next
    return oddDummy.next
# **********************************************
# 203. Remove Linked List Elements
# **********************************************

def removeElements(head: [ListNode], val: int) -> [ListNode]:
    current = head
    pre = None
    while head and head.val == val:
        head = head.next
    while current:
        if current.val == val and pre:
            pre.next = pre.next.next
        else:
            pre = current
        current = current.next
    return head

# **********************************************
# 141. Linked List Cycle
# hash/two pointers
# **********************************************

# method1: hash table
def hasCycle(head: [ListNode]) -> bool:
    check = set()
    while head:
        if head in check:
            return True
        check.add(head)
        head = head.next
    return False

# method2: fast/slow ptr 
def hasCycle1(head: [ListNode]) -> bool:
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
