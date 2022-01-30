# **********************************************
# #234. Palindrome Linked List
# even and odd condition
# **********************************************

def isPalindrome(self, head: Optional[ListNode]) -> bool:
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