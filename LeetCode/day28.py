# ***********************************************
# 387. First Unique Character in a String
# ***********************************************
def firstUniqChar(s: str) -> int:
	dic = {}
	# just access, didn't change
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]] = [1,i]
		else:
			dic[s[i]]=2
	for i in dic.items():
		k,v=i
		# means v==[1,i]->2nd val
		if v!=2:
			return v[1]
	return -1

# ***********************************************
# 172. Factorial Trailing Zeroes
# ***********************************************
# way1: string<->int
def trailingZeroes(n: int) -> int:
	if n <5:
		return 0
	res=1
	while n >1:
		res= res*n
		n-=1
	a=str(res)[::-1]
	for i in range(len(a)):
		if a[i]!='0':
			break
		i+=1
	return i
# way2: calculate the times of 5
# since follow by (5*4*3*2*1) and combined to 10
def trailingZeroes(n: int) -> int:
	ct=0
	while n>=5:
		print(n)
		n=n//5
		ct+=n
	return 
# ***********************************************
# 20. Valid Parentheses
# ***********************************************
def isValid(s: str) -> bool:	
	while "()" in s or "[]" in s or "{}" in s:
		s = s.replace("()","").replace("[]","").replace("{}","")
	return s ==""

# way2: hash,last elem match
def isValid(s: str) -> bool:
	if len(s)%2!=0:
		return False
	dic = {"[":"]","{":"}","(":")"}
	stack = []
	for i in s:
		if i in "[{(":
			stack.append(i)
		# stack just has [{(,match the last elm
		# can't be empty since needs pop
		elif not stack or i!=dic[stack.pop()]:
			return False
	# has elem
	return not stack

# ***********************************************
# 14. Longest Common Prefix
# ***********************************************
# horizontal scanning
def longestCommonPrefix(strs: list[str]) -> str:
	res= ""
	for i in zip(*strs):
		# any elem is the same
		if len(set(i))==1:
			# get the first one
			res+=i[0]
		else:
			# e.g.["cir","car"]
			return res
		# print(i)
	# cover strs=[""]
	return res
# vertical scanning
def longestCommonPrefix(strs: list[str]) -> str:
	prefix=strs[0]
	for ele in strs[1:]:
		# until they're the same
		while prefix!=ele[0:len(prefix)]:
			# print(prefix,ele)
			prefix=prefix[0:len(prefix)-1]
	return prefix

if __name__=="__main__":
	print('tst')
	# 387. First Unique Character in a String
	# s = "leetcode"
	# print(firstUniqChar(s))
	
	# 172. Factorial Trailing Zeroes
	# n = 10
	# print(trailingZeroes(n))
	
	# 20. Valid Parentheses
	s="([)]{}" #[()]
	# print(s)
	print(isValid(s))

	# 14. Longest Common Prefix
	# strs = ["cir","car"]
	strs= ["flower","flow","flight"]
	strs = ["dog","racecar","car"]
	strs=[""]
	print(longestCommonPrefix(strs))