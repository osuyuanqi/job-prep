# ***********************************************
# 69. Sqrt(x)
# ***********************************************
# just compare
def mySqrt( x: int) -> int:
	i=1
	while i*i<x:
		i+=1
	if i*i==x:
		return i
	else:
		return i-1

# awsome->two sides
def mySqrt(x: int) -> int:
	start = 0
	end = x
	p = 0
	while start <= end:
		mid = (start+end)//2
		if mid*mid == x:
			return mid
		elif mid*mid < x:
			p = mid
			start = mid+1
		else:
			end = mid-1
	return p

# **********************************************
# 160. Intersection of Two Linked Lists
# hash/arithmetic method
# **********************************************
# hash set
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = set()
        while headA:
            dic.add(headA)
            headA=headA.next
        while headB:
            if headB in dic:
                return headB
            headB=headB.next
        return None
#  arithmetic: a+c+(b+same)=b+c+(a+same)
#  terminate when it's the same
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1,p2=headA,headB
        while p1!=p2:
            p1=headB if p1==None else p1.next
            p2=headA if p2==None else p2.next
        return p1

# ***********************************************
# 28. Implement strStr()
# ***********************************************
# check left
def strStr(haystack: str, needle: str) -> int:
	if needle==None or haystack==None:
		return 0

	for i in range(len(haystack)):
		for j in range(i,len(haystack)):
			# print(i,j,needle,haystack[i:j])
			if haystack[i:j+1]==needle:
				return i
	return -1

# track the rest length deduct needle
def strStr(haystack: str, needle: str) -> int:
	if needle==None or haystack==None:
		return 0
	lneed=len(needle)
	l=len(haystack)-lneed+1

	for i in range(l):
		# print(i,needle,haystack[i:lneed+i])
		if haystack[i:lneed+i]==needle:
			return i
	return -1
	
# ***********************************************
# 125. Valid Palindrome
# ***********************************************
# pythonic check
def isPalindrome(s: str) -> bool:
	a=''.join([i for i in s if i.isalnum()]).lower()
	return a==a[::-1]
# two side check
def isPalindrome(s: str) -> bool:
	s = [i for i in s.lower() if i.isalnum()]
	l,h = 0, len(s)-1
	while l<h:
		if s[l]!= s[h]:
			return False
		l+=1
		h-=1
	return True
# ***********************************************
# 7. Reverse Integer
# ***********************************************
def reverse(x: int) -> int:
	sign=1 if x>0 else -1
	a=int(str(sign*x)[::-1])
	return  sign*a if sign*a > -2**31 and sign*a < 2**31-1 else 0
def reverse(x: int) -> int:
	sign=1 if x>0 else -1
	res =0
	a=sign*x
	while a>0:
		rem = a%10
		res = 10*res+rem
		a//=10
	return sign*res if sign*res > -2**31 and sign*res < 2**31-1 else 0

	
if __name__=="__main__":
	print('tst')
	
	# 69. Sqrt(x)
	# print(mySqrt(76))
	
	# 160. Intersection of Two Linked Lists

	# 28. Implement strStr()
	# haystack = "aa"; needle = "aa"
	# print(strStr(haystack,needle))

	# 125. Valid Palindrome
	# s = "A man, a plan, a canal: Panama"
	# print(isPalindrome(s))

	# 7. Reverse Integer
	# x = 123
	# print(reverse(x))
