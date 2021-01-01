# 唐僧大战白骨精游戏

# 欢迎信息
print('-' * 50)
print('欢迎来到妖怪大战的世界！')

# 请输入用户名称
user_name = input('请输入您的昵称：')
print(f'{user_name}, 欢迎登录本游戏! 系统为您分配生命值30，攻击力30')
user_life = 30
user_attack = 30


# 白骨精妖怪类
class MasterBai:
    # 初始化妖怪数据
    bai_name = '白骨精'
    bai_life = 100
    bai_attack = 50


# 牛魔王妖怪类
class MasterNiu:
    # 初始化妖怪数据
    niu_name = '牛魔王'
    niu_life = 200
    niu_attack = 20


# 蜘蛛精妖怪类
class MasterZhi:
    # 初始化妖怪数据
    zhi_name = '蜘蛛精'
    zhi_life = 80
    zhi_attack = 80


# 是否攻击怪物方法
def attack_or_not(kinds):
    while True:
        print('-' * 50)
        attack_choice = input('您是否要攻击此怪物？ 1.攻击； 2.不攻击:')
        if attack_choice == '1':
            if kinds == 'bai':
                MasterBai.bai_life -= user_attack
                print(f'{MasterBai.bai_name}的生命值还剩余：', MasterBai.bai_life)
                if MasterBai.bai_life < 0:
                    print('恭喜你，此妖怪已被你消灭！游戏结束！')
                    break
            elif kinds == 'niu':
                niu = MasterNiu
                niu.niu_life -= user_attack
                print(f'{niu.niu_name}的生命值还剩余：', niu.niu_life)
                if niu.niu_life < 0:
                    print('恭喜你，此妖怪已被你消灭！游戏结束！')
                    break
            elif kinds == 'zhi':
                zhi = MasterZhi
                zhi.zhi_life -= user_attack
                print(f'{zhi.zhi_name}的生命值还剩余：', zhi.zhi_life)
                if zhi.zhi_life < 0:
                    print('恭喜你，此妖怪已被你消灭！游戏结束！')
                    break
            else:
                print('您输入的选择不合法，请重新选择！')
        elif attack_choice == '2':
            choice_master()
            break
        else:
            print('您输入的选择不合法，请重新选择！')


# 选择攻击的妖怪方法
def choice_master():
    while True:
        # 选择你要攻击的怪物
        print('-' * 50)
        print('黑暗森林里现在有以下妖怪：')
        print('\t1.白骨精')
        print('\t2.牛魔王')
        print('\t3.蜘蛛精')
        player_choice = input('请选择你要攻击的怪物：')

        # 对不同的怪物做不同的操作
        if player_choice == '1':
            print(f'您选择的妖怪是{MasterBai.bai_name}！生命值{MasterBai.bai_life}。攻击力{MasterBai.bai_attack}')
            attack_or_not('bai')
            break
        elif player_choice == '2':
            print(f'您选择的妖怪是{MasterNiu.niu_name}！生命值{MasterNiu.niu_life}。攻击力{MasterNiu.niu_attack}')
            attack_or_not('niu')
            break
        elif player_choice == '3':
            print(f'您选择的妖怪是{MasterZhi.zhi_name}！生命值{MasterZhi.zhi_life}。攻击力{MasterZhi.zhi_attack}')
            attack_or_not('zhi')
            break
        else:
            # 用户输入其他不合法选择
            print('您输入的选择不合法，请重新选择！')


choice_master()
