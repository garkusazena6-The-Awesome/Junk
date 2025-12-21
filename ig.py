"""
data = [10,20,30]
it = iter(data)
first = next(it)
print(first)
"""
"""
it = iter(range(5))
print(next(it))
print(next(it))
print(next(it))
"""
"""
def counter():
    i = 0
    while True:
        yield i
        i += 1
it = counter()
print(next(it))
print(next(it))
"""
"""
class MyRange:
    def __init__(self,n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        return self.i
r = MyRange(5)
for x in r:
    print(x)
"""
"""
def check_degrees(number):
    i = 0
    while True:
        result = number**i
        yield result
        if result > 100**20:
            return
        i += 1
rez = check_degrees(122345)
print(rez)
for _ in rez:
    print(_)
"""
def lock_main(x):
    def remember(y):
        return x+y
    return remember
par1 = lock_main(5)
par2 = lock_main(10)
print(par1(3))
print(par2(3))