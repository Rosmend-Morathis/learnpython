# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

L = list(filter((lambda x : x % 2 == 1 ), range(1, 20)))

print(L)