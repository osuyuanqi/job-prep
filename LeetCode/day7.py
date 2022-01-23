# **********************************************
# 9. Palindrome Number
# **********************************************

def isPalindrome(x: int) -> bool:
	if x < 0:
		return False
	s = str(x)
	if len(s) == 1:
		return True
	lmost,rmost = 0, len(s) - 1
	while lmost < rmost:
		if s[lmost] != s[rmost]:
			return False
		lmost += 1
		rmost -= 1
	return True
x = 10301; #1->true,1001->true,-1->false
print(isPalindrome(x))
