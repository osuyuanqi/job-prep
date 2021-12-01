# ****************************
# decorator usage: 
# pass a whole function object
# ****************************

def decorator(func):
  # *args stands for varible parameter without keywords
  # **kwargs stands for varible parameters with keywords
  def partial_func(*args,**kwargs):    
    print('func={0}:args={1},kwargs={2}'.format(func.__name__,args,kwargs))
    func(*args,**kwargs)
  return partial_func

@decorator
def some_func():
  return print('someeee')

@decorator
def any_func(*args,**kwargs):
  return print("anyyyy")

# return the execute result
# case1: no para
# func=some_func:args=(),kwargs={}
# someeee
some_func()
# equivalent
decorator(some_func())

# case 2: has paras. 
# func=any_func:args=('aaa', 'bbb'),kwargs={'key1': 'ccc', 'key2': 'ddd'}
# anyyyy
any_func('aaa','bbb',key1='ccc',key2='ddd')

# 'function' itself is a type
print('=====')
print(type(any_func)) # class 'function'
print('~~~~~~')
print(decorator(any_func())) # return the execute result + a 'function'

# ****************************
# fib: recursive+dic
# ****************************

# ordinary method: recursive, lowest
def fib(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

# memorize the previous result by dict->linear, fastest
def fibm(n):
  memo = {0:0, 1:1}
  if n not in memo:
    memo[n] = fibm(n - 1) + fibm(n - 2)
  return memo[n]

# keep the latest only ->linear search, faster
def fibi(n):
  if n == 0:
    return 0
  old, new = 0, 1
  for i in range(n-1):
    old, new = new, old + new
  return new

print([fibi(i) for i in range(10)]) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib(9),fibm(9),fibi(9)) # 34 34 34