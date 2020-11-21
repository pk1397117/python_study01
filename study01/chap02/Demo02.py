from decimal import Decimal
name = '玛利亚'
name1 = '玛利亚'
print(name)
print(id(name))
print(id(name1))

print(type(name))
print(type(1))
print(type(1.1))
print(type(True))

p = int(1)
t = True
t = "123"
print("二进制", 0b101101110)
print("八进制", 0o10)
print("十六进制", 0xE32)

d = Decimal("1.1")+Decimal("2.2")
print(d)
