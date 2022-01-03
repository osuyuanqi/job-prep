# **********************************************
# 104. Maximum Depth of Binary Tree
# should take the input format as tree.
# e.g.[3,9,20,null,null,15,7],shouldn't be list
# **********************************************

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

sl= Solution()
root = TreeNode(3) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(7) 

# print (sl.maxDepth(root))

# **********************************************
# 371. Sum of Two Integers
# return the sum of the two integers without using the operators + and -.
# note: use sample to analyse the logic
# **********************************************
def getSum(a: int, b: int) -> int:
    c = 0
    while b != 0:
        c = a & b
        a = a ^ b
        b = c << 1
        print(bin(c),bin(a),bin(b),)
    return a
# print(getSum(2,3))

# **********************************************
# 206. Reverse Linked List
# construct link list needs to improve
# **********************************************

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class LinkedList:
#     def __init__(self):
        self.head = None
    def insert(self, val):
        newNode = LinkedList(val)
        if(self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def printLL(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
def reverseList(head: LinkedList) -> LinkedList:
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(30)
ll.insert(4)
ll.insert(5)
ll.insert(6)
# ll.reverse()
# ll.printLL()
# reverseList(ll)