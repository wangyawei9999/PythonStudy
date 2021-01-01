# python字符串
name = 'wangdawei'

# 字符串 拼接
print('欢迎 ' + name + ' 光临！')

# 多个参数
print('欢迎', name, '光临！')

# 占位符
print('欢迎 %s 光临！' % name)

# 字符串格式化
print(f'欢迎 { name } 光临！')

# 布尔值Ture相当于1，False相当于0

# None 空值

# type() 用来检查值的类型
print(type(1))
print(type(1.5))
print(type(True))
print(type('wang'))
print(type(None))

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


