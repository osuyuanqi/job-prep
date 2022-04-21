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
	pass

if __name__=="__main__":
# 344. Reverse String
	s = ["h","e","l","l","o"]
	print(reverseString(s))
	print(s)
# 412. fizzBuzz
	# fizzBuzz()