import random
from math import sqrt

"""
print('hello', 'world', sep=',', end='!')
a = 321
b = 123
# 幂运算
print(a ** b)
# 整数除
print(a // b)
pi = 3.14
print(type(a))
print(type(pi))

# str类型不能进行运算
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
"""

# f = float(input('请输入华氏温度： '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# username = input('请输入用户名： ')
# password = input('请输入密码: ')
# if username == 'admin' and password == '123456':
#     print("身份验证成功")
# else:
#     print("身份验证失败")

"""
分段函数求值
"""
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x -5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

# num = 0
# for x in range(100):
#     print(x)
#     num += x
# print(num)

"""
弱智游戏
"""
# answer = random.randint(1, 100)
# times = 0
# while True:
#     times += 1
#     number = int(input('请输入： '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你答对了')
#         break
# print("你总共猜了%d次" % times)
# if times > 7:
#     print('你的智商余额明显不足')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# print(end)

"""
寻找水仙花数
"""
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# 获取用户输入数据
nterms = int(input("你需要几项？"))
# 第一和第二项
n1 = 0
n2 = 1
count = 2
# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1

