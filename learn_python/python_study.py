# python字符串
# name = 'wangdawei'
# 字符串 拼接
# print('欢迎 ' + name + ' 光临！')
# 多个参数
# print('欢迎', name, '光临！')
# 占位符
# print('欢迎 %s 光临！' % name)
# 字符串格式化
# print(f'欢迎 { name } 光临！')

# 布尔值Ture相当于1，False相当于0

# None 空值

# type() 用来检查值的类型
# print(type(1))
# print(type(1.5))
# print(type(True))
# print(type('wang'))
# print(type(None))

# 对象即一块内存，有id(),type(),value()

# 类型转化 int(), float(), st(), bool()
# int()规则：
#   布尔型：True -> 1; False -> 0
#   浮点型：直接取整
#   字符型：如果是合法的整数，则转换成对应的整数；如果是其他的字符，就报错。
# bool()规则：0, None, ''会转换成False，其他的都会转换成True。

# 逻辑运算符 优先级参考官方文档
# 逻辑非 not
#   a = not 1 一元运算符，先将1转化为布尔值，再取反
# 逻辑与 and
# 逻辑或 or

# a = input()
# print('用户输入的内容是：', a)
#
# b = input('请输入内容：')
# print('用户输入的内容是：', a)
#
# username = input('请输入用户名：')
# admin = 'admin'
# if username == admin:
#     print('欢迎登陆，', admin)

# # 狗的年龄相当于人的多少岁
# dog_age = int(input('请输入狗的年龄：'))
# dog_for_human_age = 10.5
# if dog_age == 1:
#     print(dog_age, '岁的狗相当于人的年龄为：', dog_for_human_age, '岁')
# elif dog_age == 2:
#     print(dog_age, '岁的狗相当于人的年龄为：', dog_for_human_age * 2, '岁')
# else:
#     dog_for_human_age = (dog_age - 2) * 4 + 21
#     print(dog_age, '岁的狗相当于人的年龄为：', dog_for_human_age, '岁')

# dog_age = float(input('请输入狗的年龄：'))
# like_person_age = 0
# if dog_age <= 2:
#     like_person_age = dog_age * 10.5
# else:
#     like_person_age = (dog_age - 2) * 4 + 21
#
# print(dog_age, '岁的狗相当于人的年龄为：', like_person_age, '岁')

# while 循环
# i = 0
# while i < 10:
#     i += 1
#     print(i, ', hello')
# else:
#     print('else 结束！')

# 计算100以内所有奇数之和
# i = 0
# result = 0
# while i < 100:
#     i += 1
#     if i % 2 != 0:
#         result = result + i
#
# print('100以内所有奇数之和为：', result)

# 求100以内7的倍数之和及个数
# i = 0
# num = 0
# result = 0
# while i < 100:
#     if i % 7 == 0:
#         num += 1
#         result += i
#     i += 1
# print('100以内7的倍数之和为：', result)
# print('100以内7的倍数的个数为：', num)

# 求1000以内的所有水仙花数
# i = 100
# while i < 999:
#     bai = i // 100
#     shi = i % 100 // 10
#     ge = i % 100 % 10
#     result = bai ** 3 + shi ** 3 + ge ** 3
#     if result == i:
#         print(i)
#     i += 1

# 获取用户输入的任意数，判断它是否为质数
# num = int(input('请输入任意整数：'))
# if num > 0:
#     if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
#         print(num, '是质数！')
#     else:
#         print(num, '不是质数！')

# 打印99乘法表
# i = 0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print(f'{j}*{i}={i*j} ', end='')
#     print()

# break会立即退出循环，包括else
# continue是跳过当次循环
# pass是在循环或判断中占位的

# time() 获取当前时间，返回单位是秒

# 列表 有序
# list = [1,2,3,4,5]
# list[0] 获取第一个元素
# len(list)获取list长度

# 切片 从现有列表中获取子列表 返回一个新列表
# list[-1]获取列表倒数第一个元素
# list[0:2]获取列表前两个元素
# 切片可以不写开始或结束，list[:3]; list[2:]; 或开始和结束都省略，相当于复制一遍
# list[开始：结束：步长] list[0:5:2],默认为1，不可以是0，可以是负数（倒着写）

# 列表的通用操作
# + 可以将两个列表拼接成一个列表 my_list = [1,2,3] + [4,5,6]
# * 重复列表N次 my_list = [1,2,3] * 5
# in; not in:检查指定元素是否存在于列表中，返回布尔值
# len() 获取列表长度
# min() 获取列表中的最小值
# max() 获取列表中的最大值
# index() 获取列表中元素的索引
# count() 统计元素在列表中出现的次数




