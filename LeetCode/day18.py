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
s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))
# **********************************************
# Ex: break tip->terminate current SINGLE loop
# **********************************************
for i in range(5):
	for j in range(3):
		print(i,j)
		break
