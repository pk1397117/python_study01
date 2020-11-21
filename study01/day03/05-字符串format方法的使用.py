# {} 也可以进行站位
# {} 什么都不写，会读取format里的参数值，一一对应
x = "大家好，我是{},我今年{}岁了".format("张三", 18)
print(x)

# {数字} ,按照format参数列表的索引进行匹配
y = "大家好，我是{1},我今年{0}岁了".format(20, "Jerry")
print(y)

# {变量名}
z = "大家好，我是{name}，我今年{age}岁了,来自{address}".format(age=18, name="Jack", address="北京")
print(z)

# 混合使用 {数字} {变量}
a = "大家好，我是{name}，我今年{0}岁了,来自{address}".format(17, name="Daisy", address="上海")
print(a)

# {}什么都不写 {数字} 不能混合使用

d = ["张三", 18, "上海", 180]
b = "大家好，我叫{0},今年{1}岁，来自{2},身高{3}".format(d[0], d[1], d[2], d[3])
b = "大家好，我叫{0},今年{1}岁，来自{2},身高{3}".format(*d)  # *d 对列表进行拆包
print(b)

info = {"name": "Chris", "age": 23, "addr": "北京", "height": 190}
c = "大家好，我叫{0},今年{1}岁，来自{2},身高{3}".format(*info.values())
c = "大家好，我叫{name},今年{age}岁，来自{addr},身高{height}".format(**info)  # **info 对字典进行二次拆包
print(c)

print(*info)