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

if __name__=="__main__":
	print('tst')
	# 202. Happy Number
	# print(isHappy(19))

	# 118. Pascal's Triangle
	# print(generate(5))

	# 70. Climbing Stairs
	# print(climbStairs(5))
