# 1304. Find N Unique Integers Sum up to Zero
# 
# [1, 2, 0, -1, -2]
# [1, 2, 3, -1, -2, -3]
def sumZero( n: int) -> list[int]:
    a = [i for i in range(1, n // 2 + 1)]
    b = [-i for i in range(1, n // 2 + 1)]
    if n % 2 != 0:
        a.append(0)
    return a + b
print(sumZero(5))
print(sumZero(6))