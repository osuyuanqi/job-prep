print("========sort tips, python 3.10")
# ========sort # 
a = [5, 1, 2, 6, 4]
a.sort(key=lambda x: x,reverse=True)
print(a,sorted(a))
# ========sort dic
L = [('c', 2), ('d', 1), ('a', 4), ('b', 0), ('c', 0)]
print(sorted(L,key=lambda y:y)) # sort by first val,then second
print(sorted(L,key=lambda y:y[0])) #sort by the first value only, original order
print(sorted(L,key=lambda y:y[1]))#sort by the second value only, original order


print("========Fibonacci impro")
# default value: get rid of global variable
def fib(n,dic={0:1,1:1}):
    if n not in dic:
        # pass the updated dic
        dic[n]=fib(n-1,dic)+fib(n-2,dic)
    return dic[n]
print(fib(4))
# 2nd way:
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return b
print(fib(4))

print("========OOP")
class Point(object):
    # ~ everything in class is public
    # self, like the keyword "this" in js
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norm(self):
        return self.x**2+self.y**2
    def norm1(x,y):
        return x**2+y**2
    # no polymorphic function, earlier defs will be shadowed
    def poly(a):
        return 1
    def poly(b):
        return 2
# inheritance
class Point3D(Point):
    def __init__(self,x,y,z):
        Point.__init__(self,x,y)
        self.z=z
    def normal(self):
        return print(self.x,self.y,self.z)
p=Point(3,4)
print(p.norm(),p)
print(Point.norm1(3,4))
print("p.poly:",p.poly()) # 2
p3=Point3D(5,6,7)
p3.normal()