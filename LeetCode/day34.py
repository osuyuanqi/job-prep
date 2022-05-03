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

if __name__=="__main__":
	print('tst')
	# 202. Happy Number
	# print(isHappy(19))