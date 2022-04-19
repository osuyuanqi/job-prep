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

if __name__=="__main__":
	print('tst')
	
	# 189. Rotate Array
	# nums = [1,2,3,4,5,6]; k =11
	# print(rotate(nums,k))
	# print(nums)

	# 204. Count Primes
	# n = 10
	# print(countPrimes(n))