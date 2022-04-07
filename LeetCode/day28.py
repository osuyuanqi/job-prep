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

if __name__=="__main__":
	print('tst')
	# 387. First Unique Character in a String
	# s = "leetcode"
	# print(firstUniqChar(s))

	