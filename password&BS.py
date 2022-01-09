# **************************
# generate random 8 passcode
# **************************

import random
a1 = [chr(i) for i in range(65,91)] # capital A-Z
a2 = [chr(i) for i in range(97,123)] # a - z
a3 = [str(i) for i in range(0,10)] # 0-9
a4 = ["!","@","#","$","%","^","&","*"]
a = a1 + a2 + a3 + a4
random.shuffle(a)
b = random.sample(a,8)
c = ''.join(b)
print(c)

# **************************
# binary search
# **************************

def bSearch(arr, left, right, x):
  times = 0
  while left <= right:
    times += 1
    mid = (left + right) // 2
    if x < arr[mid]:
      right = mid -1
    elif x >arr [mid]:
      left = mid +1
    else: # x == a[mid]
      print('find it, the position is in {0},times={1}'.format(mid,times))
      break # end key
  # element doesn't exist ->end it
  else:
    print('the element is not exist.')

a = [1,2,3,4,5,8] 
bSearch(a, 0, len(a)-1, 4)#times: 8->3,3->1,4->3
