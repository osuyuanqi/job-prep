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
	return ct

if __name__=="__main__":
	print('tst')
	# 387. First Unique Character in a String
	# s = "leetcode"
	# print(firstUniqChar(s))
	
	# 172. Factorial Trailing Zeroes
	# n = 10
	# print(trailingZeroes(n))