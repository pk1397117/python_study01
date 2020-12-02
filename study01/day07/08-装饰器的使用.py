# 产品经理: 提需求 / 改需求
# 如果超过22点不让玩游戏，如果不告诉时间，默认不让玩
# 开闭原则
def can_play(fn):
    def inner(name, game, *args, **kwargs):
        # clock = kwargs["clock"]  # 拿不到会报错
        clock = kwargs.get("clock", 23)
        if clock > 22:
            print("太晚了")
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


play_game("张三", "王者荣耀", clock=21)
play_game("李四", "绝地求生", clock=23)
play_game("王五", "英雄联盟")
