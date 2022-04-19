# ***********************************************
# 189. Rotate Array
# remove the last k elems,prepend to the begin
# ***********************************************

# faster->nums[:] change original
def rotate(nums: list[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k %=len(nums)
	nums[:] = nums[-k:]+nums[:-k]

# pop original array->change,append into the tail	
def rotate(nums: list[int], k: int) -> None:
	n=len(nums)
	k %=n
	for i in range(len(nums)-k):
		x=nums.pop(0)
		nums.append(x)

# ***********************************************
# 204. Count Primes
# ***********************************************

# timeout
def countPrimes(n: int) -> int:
	def check_prime(n:int)->bool:
		for i in range(2,n):
			if n%i==0:
				return False
		return True
	res=0
	for i in range(0,round(n**0.5)+1):
		if check_prime(i):
		# 	# print(i)
			res+=1
	return res
# math calculate the minimest i*i value 
def countPrimes(n: int) -> int:
	if n < 2:
		return 0
	# assume all is prime
	s = [1] * n
	s[0] = s[1] = 0
	# exclude the not prime value
	for i in range(2, int(n ** 0.5) + 1):
	# target the i*i+(i steps) also not prime->0
		if s[i] == 1:
			s[i * i::i] = [0] * len(s[i * i::i])
		# print(s,i,len(s[i * i:n:i]))
	# print(s)

	return sum(s)
# ***********************************************
# 190. Reverse Bits
# ***********************************************

def reverseBits(n: int) -> int:
	a='{:032b}'.format(n)
	# int(x,2)->x must be string
	return int(a[::-1],2)

def reverseBits(n: int) -> int:
	res=0
	for i in range(32):
	    # pop to the right_most
		a=n>>i
		# only last 1 left, since &1 is &000..001
		bit=(a)&1
		# push the pop val to the left_most, then add together
		# 31->0
		res= res|(bit<<(31-i))
		# print('{:032b}'.format(a),i,bit,'{:032b}'.format(bit<<(31-i)),'{:032b}'.format(res))
	return res

# ***********************************************
# 155. Min Stack
# ***********************************************
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_elem=[]

    # min_elem: always push the min
    def push(self, val: int) -> None:
        self.stack.append(val)
        min_elem=self.min_elem
        # append val when not min_elem==True, means it's None
        # e.g.a=None; print(1 if not a else 2)->1
        min_elem.append(val if not min_elem else min(val,min_elem[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_elem.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elem[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__=="__main__":
	print('tst')
	
	# 189. Rotate Array
	# nums = [1,2,3,4,5,6]; k =11
	# print(rotate(nums,k))
	# print(nums)

	# 204. Count Primes
	# n = 10
	# print(countPrimes(n))

	# 190. Reverse Bits
	# n='00000010100101000001111010011100'
	# print(reverseBits(int(n,2)))