from pub_module import *

# **********************************************
# 234. Palindrome Linked List
# even and odd condition
# **********************************************

def isPalindrome(self, head: [ListNode]) -> bool:
    fast, slow = head, head
    # find the mid point, even: end when fast in the null condition,e.g.[1,2,2,1,null]; odd: end when fast.next none, e.g.[1,2,3,2,1],fast = 1(second), but fast.next node is None.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    #  fast not none-> odd, move to the next
    if fast:
        slow = slow.next
    
    prev = None
    while slow:
        # finish reverse        
        temp = slow.next
        slow.next = prev
        prev = slow
        
        # recursive step      
        slow = temp
    #   
    while prev:
        if prev.val != head.val:
            return False
        head = head.next
        prev = prev.next
    return True
# **********************************************
# Find the smallest missing positive integer
# [1,2,3]->4,[1,3,5,4,6]->2,[-1,-2]->1
# **********************************************

def solution(A):
    A_set = set()
    for i in A:
        A_set.add(i)
    A_length = len(A)
    # length+1->max value in the group, +2 -> smallest val outside of group
    for i in range(1,A_length+2):
        if i not in A_set:
            return i
# A = [-1,-2]
# print(solution(A))