# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 闭包：
# 在一个函数 f 中又定义了函数 g，并且，内部函数 g 可以引用外部函数 f 的参数和局部变量
# 当外部函数 f 返回内部函数 g 时，相关参数和变量都保存在返回的函数中。
# 返回的函数并没有立刻执行，而是直到调用了f()才执行

def createCounter():
    n = 0
    def counter():
        nonlocal n
# 如果没有nonlocal声明(3.2版本后引入)，会发生异常 UnboundLocalError
# local variable 'n' referenced before assignment
        n = n + 1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')