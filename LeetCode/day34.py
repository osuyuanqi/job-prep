# **********************************************
# 202. Happy Number
# **********************************************
def isHappy(n: int) -> bool:
	# note: [0,10), not [1,10)
	dic={str(i):i**2 for i in range(10)}
	# print(dic)
	s=set()
	while n!=1 and n not in s:
		s.add(n)
		# print(s)
		strN=str(n)
		n=0
		for i in range(len(strN)):
			n+=dic[strN[i]]
	return n==1
# **********************************************
# 118. Pascal's Triangle
# **********************************************
def generate(numRows: int) -> list[list[int]]:
	res=[]
	# from 0 is easier to generate 2d arr
	for i in range(numRows):
		b=[1]*(i+1)
		res.append(b)
		# print(res)
		for j in range(1,i):
			# print(i,j) ->tip
			res[i][j]=res[i-1][j]+res[i-1][j-1]
	return res

# **********************************************
# 70. Climbing Stairs
# **********************************************
# recursive thinking, plus the previous one
def climbStairs(n: int) -> int:
	# dic={1:1,2:2,3:3}
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
	return b
# follow rules to write code 
def climbStairs(n: int) -> int:
	memo={1:1,2:2}
	def climb(n):
		if n in memo:
			return memo[n]
		else:
			memo[n]=climb(n-1)+climb(n-2)
			return memo[n]
	return climb(n)
# **********************************************
# 53. Maximum Subarray
# **********************************************
# DP: Kadane’s Algorithm,local max>global max
def maxSubArray(nums: list[int]) -> int:
	res,temp=-math.inf,0
	for i in nums:
		temp= max(i,i+temp)
		if temp>res:
			res=temp
	return res
# same logic
def maxSubArray(nums: list[int]) -> int:
	curMax,res=nums[0],nums[0]
	for i in nums[1:]:
		curMax=max(curMax+i,i)
		res=max(res,curMax)
	return res
# dp: as long as the last elem>0-> effective add
def maxSubArray(nums: list[int]) -> int:
	for i in range(1, len(nums)):
		if nums[i-1] > 0:
			nums[i] += nums[i-1]
		# print(i,nums)
	return max(nums)

# **********************************************
# 509. Fibonacci Number
# **********************************************
# memo
def fib(n: int) -> int:
	memo={0:0,1:1}
	def f(n):
		if n<2:
			return n
		else:
			return f(n-1)+f(n-2)
	return f(n)
# iterative
def fib(n: int) -> int:
	if n <2:
		return n
	a,b=0,1
	for i in range(1,n):
		a,b=b,a+b
	return b
print(fib(2))
if __name__=="__main__":
	print('tst')
	# 202. Happy Number
	# print(isHappy(19))

	# 118. Pascal's Triangle
	# print(generate(5))

	# 70. Climbing Stairs
	# print(climbStairs(5))

	# 53. Maximum Subarray
	# nums = [-2,1,-3,4,-1,2,1,-5,4]
	# print(maxSubArray(nums))

