# **********************************************
# 344. Reverse String
# **********************************************
# way1: s[:] from 0->len-1 is assigned with s[::-1]
def reverseString(s: list[str]) -> None:
	s[:]=s[::-1]
# way2: exchange from leftmost and rightmost->narrow down
def reverseString(s: list[str]) -> None:
	for i in range(len(s)//2):
		s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]

# **********************************************
# 412. fizzBuzz
# Method1: mod operation is slower
# **********************************************
def fizzBuzz(n:int)->list[str]:
	res = []
	for i in range(1,n+1):
		
		if i%3==0 and i%5==0:
			res.append("FizzBuzz")
		elif i%3==0:
			res.append("Fizz")
		elif i%5==0:
			res.append("Buzz")
		else:
			res.append(i)
	return res
# **********************************************
# 136. Single Number
# **********************************************
# way1: O(n^2)->array also need iterative search
def singleNumber(nums: list[int]) -> int:
	a=[]
	for i in range(len(nums)):
		if nums[i] not in a:
			a.append(nums[i])
		else:
			a.remove(nums[i])
	return a[0]

# way2: hash-> much faster
def singleNumber(nums: list[int]) -> int:
	dic ={}
	for i in nums:
		if i in dic:
			dic[i]-=1
		else:
			dic[i]=1
	for k,v in dic.items():
		if v==1:
			return k
# way3: ^ tip->similar faster as hash
def singleNumber(nums: list[int]) -> int:
	res=0
	# since every elem appears exactly twice except for one
	for i in nums:
		res^=i
	return res
# **********************************************
# 217. Contains Duplicate
# **********************************************
# way1: pythonic compares
def containsDuplicate(nums: list[int]) -> bool:
	return len(set(nums))!=len(nums)
# way2: dic
def containsDuplicate(nums: list[int]) -> bool:
	dic = {}
	for i in nums:
		if i in dic:
			return True
		else:
			dic[i]=None
	return False
# way3: hash
def containsDuplicate(nums: list[int]) -> bool:
	s=set()
	for i in nums:
		if i in s:
			return True
		s.add(i)
	return False

# **********************************************
# 168. Excel Sheet Column Title
# **********************************************
# way1: reverse from end, better to understand
def convertToTitle(n: int) -> str:
	table = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	res = ""
	while n > 0:
		digit=n%26
		if digit==0:
			digit=26
		# from last to first
		n=(n-digit)//26
		res+=table[digit]
	return res[::-1]

# way2: not understand n-1
def convertToTitle(columnNumber: int) -> str:
	dic = {}
	for i in range(26):
		dic[i]=chr(97+i).upper()
	res=""
	while columnNumber>0:
		print((columnNumber-1)%26)
		res+=dic[(columnNumber-1)%26]
		columnNumber=(columnNumber-1)//26
	return res[::-1]
	
# **********************************************
# 171. Excel Sheet Column Number
# **********************************************
def titleToNumber(columnTitle: str) -> int:
	dic={}
	for i in range(1,27):
		dic[chr(64+i)]=i
	res=0
	a=columnTitle[::-1]
	for i in range(len(a)):
		res+=dic[a[i]]*26**i
	return res

if __name__=="__main__":
	print("tst")
	# 344. Reverse String
	# s = ["h","e","l","l","o"]
	# print(reverseString(s))
	# print(s)
	
	# 412. fizzBuzz
	# n=15
	# print(fizzBuzz(n))
	
	# 136. Single Number
	# nums = [4,1,2,1,2]
	# print(singleNumber(nums))

	# 217. Contains Duplicate
	# nums = [1,1,1,3,3,4,3,2,4,2]
	# print(containsDuplicate(nums))

	#168. Excel Sheet Column Title

	# columnNumber = 701 #ZY
	# print(convertToTitle(columnNumber))
	# print(701%26)
	
	# 171. Excel Sheet Column Number
	# columnTitle = "ZY"
	# print(titleToNumber(columnTitle))