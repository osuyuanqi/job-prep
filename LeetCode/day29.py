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

if __name__=="__main__":
	print('tst')
	
	# 69. Sqrt(x)
	# print(mySqrt(76))
	
	# 160. Intersection of Two Linked Lists
