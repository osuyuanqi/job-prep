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

if __name__=="__main__":
	print('tst')
	print(mySqrt(76))
