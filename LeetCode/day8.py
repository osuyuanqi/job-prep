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
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# class MaxStack:

#     def __init__(self):        
#         self.head = Node('head')
#         self.size = 0

#     def push(self, x: int) -> None:
#         node = Node(x)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1

#     def pop(self) -> int:
#         if self.isEmpty():
#             raise Exception('Pop from empty stack')
#         remove = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return remove.value

#     def top(self) -> int:
#         if self.isEmpty():
#             raise Exception('Pop from empty stack')
#         remove = self.head.next
#         self.head.next = self.head.next.next
#         # self.size -= 1
#         return remove.value

#     def peekMax(self) -> int:
#         if self.isEmpty():
#             raise Exception("Peeking from an empty stack")
#         return self.head.next.value.max()

#     def popMax(self) -> int:
#         node = head
#         maxV = node.value
#         while node:
#             if node.value > maxV:
#                 maxV = node.value
#             node.next = self.head.next

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# **********************************************
# 56. Merge Intervals
# append the largest tails only
# **********************************************
def merge(intervals: list[list[int]]) -> list[list[int]]:
    # sort the original list by the first elem
    intervals.sort(key = lambda x: x[0])
    
    # unpack the package intervals as 1,3
    result = []
    for x,y in intervals:
        if not result:
            result.append([x,y])
            # for the next loop 
            continue
        # comparison, result has had values,get the previous package value
        # print(result)
        x0,y0 = result[-1]
        # merge if prsent is smaller than the previous value y, which is y0
        
        if x > y0:
            # just append, since the previous x0,y0 has been added last time
            result.append([x,y])
        else:
        # we just sorted by the first elem in the first line of the func
            # the last element is useless
            # print(result)
            result.pop()
            result.append([x0, max(y,y0)])
    return result
# intervals = [[1,4],[4,5]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(merge(intervals))


# **********************************************
# 200. Number of Islands
# Depth Search Tree(DST), use # lable visited one
# **********************************************

def isIsland(i,j,grid):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
        return
    if grid[i][j]!='1':
        return
    # the visited point was labled by # 
    grid[i][j]='#'
    print(grid)
    # DST: vertical order
    isIsland(i-1, j, grid)
    isIsland(i+1, j, grid)
    isIsland(i,j-1, grid)
    isIsland(i, j+1, grid)
    # DST: horizontal order
    # isIsland(i, j+1, grid)
    # isIsland(i,j-1, grid)
    # isIsland(i+1, j, grid)
    # isIsland(i-1, j, grid)
def numIslands(grid: list[list[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(i,j)
            if grid[i][j] == '1':
                count += 1
                print(i,j,grid)
                isIsland(i,j,grid)
    return count
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# print(numIslands(grid))