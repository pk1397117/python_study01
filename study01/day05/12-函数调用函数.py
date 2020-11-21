def test1():
    print("test1开始了")
    print("test1结束了")


def test2():
    print("test2开始了")
    test1()
    print("test2结束了")


test2()