# def 函数名(形参):
#   函数体

# 调用函数: 函数名(实参)


# 函数声明时，括号里的参数我们称之为形式参数，简称形参
# 形参的值是不确定的，只是用来占位的
def tell_story(place, person1, person2):
    print("从前有座山")
    print("山上有座" + place)
    print(place + "里有个" + person1)
    print(person1 + "在给" + person2 + "讲故事")
    print("故事的内容是:")


# 调用函数时传递数据
# 函数调用时传入的参数，才是真正参与运算的数据，我们称之为实参
tell_story("道观", "老道士", "小道士")  # 会把实参一一对应地传递，交给形参处理
tell_story("尼姑庵", "师太", "小尼姑")

# 直接给形参的变量赋值
tell_story(place="庙", person1="老和尚", person2="小和尚")

