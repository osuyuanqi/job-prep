# **********************************************
# 139. Word Break
# dynamic programming, break is the key
# **********************************************

# bruce force + hash check
def wordBreak(s: str, wordDict: list[str]) -> bool:
	wordDict = set(wordDict)
	start = [0]
	for i in range(len(s)):
		for j in start:
			if s[j:i+1] in wordDict:
				start.append(i+1)
				# finish loop the current loop
				break

# way2: dynamic programmin
def wordBreak(s: str, wordDict: list[str]) -> bool:
	wordSet= set(wordDict)
	dp = [0]*(len(s)+1)
	dp[0] = 1
	# tricky read
	# e.g.i read the 1->9 here
	for i in range(1,len(s)+1):
		# e.g.read the 0->8
		for j in range(i):
			print(i,j,dp)
			# s[j:i] read the 0->7,since range(8) doesn't contain 8
			if dp[j] == 1 and s[j:i] in wordSet:
				dp[i] = 1
				break
	# print(dp)
	return dp[-1] == 1
# s = "leetcode"
# wordDict = ["leet","code"]
# print(wordBreak(s,wordDict))

# **********************************************
# Ex: break tip->terminate current SINGLE loop
# **********************************************
# for i in range(5):
# 	for j in range(3):
# 		print(i,j)
# 		break

# **********************************************
# 171. Excel Sheet Column Number
# **********************************************

# way1
def titleToNumber(columnTitle: str) -> int:
	num = 0
	dic = {}
	for i in range(1,27):
		dic[chr(64+i)] = i
	a = columnTitle[::-1]
	for i in range(len(a)):
		num+= dic[a[i]]*26**i
	return num

# way2
def titleToNumber(columnTitle: str) -> int:
	a = list(columnTitle)[::-1]
	rst = 0
	for i in range(len(a)):
	    rst += (ord(a[i]) - 64) * (26**i)
	return rst

# print(titleToNumber("ZY"))

# **********************************************
# 371. Sum of Two Integers
# binary operations: positive+negative cases
# **********************************************

# mask->set bound,since python is no length limitation
def getSum(a: int, b: int) -> int:
	mask = 0xFFFFFFFF
	while b!=0:
	    sum1 = (a^b)&mask
	    carry = ((a&b)<<1)&mask
	    # print(bin(sum1),bin(carry))
	    a =sum1
	    b=carry
	max_int = 0x7FFFFFFF
	return a if a<max_int else ~(a^mask)
def getSum(a: int, b: int) -> int:
	mask=0xffffffff
	while b & mask:
	    a, b = (a ^ b), (a & b) << 1
	# print(a,b)  
	if b > 0:
	    return a & mask
	else:
	    return a

# test cases:
# {a = 5;b=1},{a=8;b=-12},{a=-8;b=12}
a=-8;b=-12
print(getSum(a,b))

if __name__ == '__main__':
    print('tst')		