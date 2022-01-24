# **********************************************
# 1. Two Sum
# hash,dic comes into mind
# test cases:
# [2,7,11,15]->9;[3,2,4]->6;[3,3]->6
# **********************************************

def twoSum(nums: list[int], target: int) -> list[int]:
        for i_idx,i in enumerate(nums):
            for j_idx,j in enumerate(nums):
                if i == target - j and i_idx != j_idx:
                    return i_idx,j_idx
        return [None]

def twoSum1(nums: list[int], target: int) -> list[int]:
    result = {}
    for idx,i in enumerate(nums):
        if target - i in result:
            return [result[target - i],idx]
        result[i] = idx

nums = [2,7,11,15]; target = 18
# print(twoSum1(nums,target))

# **********************************************
# 716. Max Stack
# not solved
# **********************************************
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class MaxStack:

    def __init__(self):        
        self.head = Node('head')
        self.size = 0

    def push(self, x: int) -> None:
        node = Node(x)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            raise Exception('Pop from empty stack')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def top(self) -> int:
        if self.isEmpty():
            raise Exception('Pop from empty stack')
        remove = self.head.next
        self.head.next = self.head.next.next
        # self.size -= 1
        return remove.value

    def peekMax(self) -> int:
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value.max()

    def popMax(self) -> int:
        node = head
        maxV = node.value
        while node:
            if node.value > maxV:
                maxV = node.value
            node.next = self.head.next




# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# **********************************************
# 56. Merge Intervals
# **********************************************
