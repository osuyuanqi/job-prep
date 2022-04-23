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

if __name__=="__main__":
	# 344. Reverse String
	# s = ["h","e","l","l","o"]
	# print(reverseString(s))
	# print(s)
	
	# 412. fizzBuzz
	# n=15
	# print(fizzBuzz(n))
	