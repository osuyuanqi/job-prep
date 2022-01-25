# **********************************************
# 160. Intersection of Two Linked Lists
# hash/arithmetic method
# **********************************************

# single list definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method 1: hash table,O(m + n)
def getIntersectionNode1(headA: ListNode, headB: ListNode) -> [ListNode]:
    a_node = set()
    while headA is not None:
        a_node.add(headA)
        headA = headA.next
    while headB is not None:
        if headB in a_node:
            return headB
        headB = headB.next
    return None

# method 2: arithmetic method, a+c+b = b+c+a, O(m + n)
def getIntersectionNode1(headA: ListNode, headB: ListNode) -> [ListNode]:
    p1,p2 = headA,headB
    while p1 != p2:
        p1 = headB if p1 == None else p1.next
        p2 = headA if p2 == None else p2.next
    return p1
