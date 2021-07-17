#高级函数 map() & reduce()

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

#练习1
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    if (isinstance(name, str)):
        name = str.lower(name)
        name = str.capitalize(name) 
    return name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#练习2
#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    # def p(x, y):
    #     return x * y
    # return reduce(p, L)
    return reduce((lambda x, y : x * y), L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#练习2
#利用map和reduce编写一个str2float函数，
#把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    DIGITS = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
    def char2num(s):
        return DIGITS[s]
    L1, L2 = str.split(s,'.')   
    return reduce((lambda x, y : x * 10 + y), list(map(char2num, L1))) + reduce((lambda x, y : x * 10 + y), list(map(char2num, L2))) / 10**len(L2)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')