import random

print("作战事件:")
print("特殊行动、对决")
print()
modech = input(str("请选择作战事件: "))
# PVE mode
if modech == "特殊行动":
    print("请选择角色:")
    ch = { 
        'ch1' : "夜曲",
        'ch2' : "护符",
        'ch3' : "水银"
        }
    print(ch['ch1'],ch['ch2'],ch['ch3'])
    chosench = input("请输入所选角色：")
    if chosench == "夜曲":
        player = "lullaby"
        print("已选择角色：",ch['ch1'])
    elif chosench == "护符":
        player = "talisman"
        print("已选择角色：",ch['ch2'])
    elif chosench == "":
        player = ""
        print("已选择角色：")
    else:
        print("character not found")
    print("------------------------------------------------------------------")
    print()
    print("[ 准备阶段 ]")
    #夜曲角色相关
    if player == "lullaby":
        php = 40
        s1 = "技能1: [无人机升空]"
        s1d = "     召唤[无人机]，最多召唤3架"
    # 消耗2枚白币，。获得1点充能
        s2 = "技能2: [空中打击]"
        s2d = "     造成5点物理伤害，每有1架[无人机]额外造成3点物理伤害"
    # 消耗3枚白币，。获得1点充能
        s3 = "技能3: [防御阵型]"
        s3d = "     每有1架[无人机]为[夜曲]附属1层[护甲]，最多叠加10层"
    # 消耗3枚黑币，。获得1点充能
        s4 = "技能4: [机身维护]" 
        s4d = "     为所有[无人机]恢复10点生命值"
    #消耗2枚黑币，



    if player == "talisman":
        php = 50
        s1 = "技能1: [刃]"
        s1d = "     造成5点物理伤害"
        s2 = "技能2: [锋]"
        s2d = "     造成3点物理伤害，怒气值+1"
        s3 = "技能3: [斩]"
        s3d = "     失去4点生命值，造成2点物理伤害，对方每已损失10点生命值，伤害额外+3"
        s4 = "技能4: [狂]"
        s4d = "     消耗所有怒气值，每1点怒气值，恢复3点生命值"














    print()
    print("[",chosench,"]生命值: ",php)
    print()
    print(s1)
    print(s1d)
    print()
    print(s2)
    print(s2d)
    print()
    print(s3)
    print(s3d)
    print()
    print(s4)
    print(s4d)
    print()
    # originize

    e1 = "[徘徊]"
    e1hp = 150
    dronenum = 0
    playerarmor = 0
    eatk = 2
    d1hp = 0
    d2hp = 0
    d3hp = 0
    roundnum = 0
    roundcon = roundnum % 2
    talismanrage = 0

    print()
    print("对方信息: ")
    print(e1)
    print("生命值: ",e1hp)
    print()
    print("------------------------------------------------------------------")

    if chosench == "夜曲":
        print()
        print("------------------------------------------------------------------")
        print()
        print("[ 开火已授权，作战开始 ]")
        print()
        print("对方信息: ")
        print(e1)
        print("生命值: ",e1hp)
        print()
        ready = input ("按下Enter以开始: ")
    elif chosench == "护符":
        print()
        print("------------------------------------------------------------------")
        print()
        print("[ 拔刀，作战开始 ]")
        print()
        print("对方信息: ")
        print(e1)
        print("生命值: ",e1hp)
        print()
        ready = input ("按下Enter以开始: ")
    # circulation start
    while e1hp > 0 and php > 0:
        if chosench == "夜曲":
            # player choose one skill to use
            # sun = skill used number
            if roundcon == 1:
                roundnum = roundnum + 1
                print("------------------------------------------------------------------")
                print()
                print("[ 回合开始：第",roundnum,"回合 ]")
                sun = input("输入技能对应数字并按下Enter：")
                print()
                if sun == "2" :
                    e1hp = e1hp - 5 - 3*dronenum
                    print("[ 我方行动 ]")
                    print("[夜曲]使用技能2[空中打击]")
                    print("[徘徊]受到",5+3*dronenum,"点物理伤害")
                    if e1hp < 0:
                        break
                    else:
                        print("[徘徊]剩余生命值: ",e1hp)
                if sun == "1" :
                    if dronenum < 3:
                        dronenum += 1
                        if dronenum == 1:
                            d1hp += 5
                        elif dronenum == 2:
                            d2hp += 5
                        elif dronenum == 3:
                            d3hp += 5
                        print("[ 我方行动 ]")
                        print("[夜曲]使用技能1[无人机升空]")
                        print("当前[无人机]数量: ",dronenum)
                        print()
                        print("[徘徊]未受到攻击，生命值: ",e1hp)
                        if dronenum > 3:
                            dronenum = 3
                if sun == "3":
                    playerarmor = playerarmor + dronenum * 1
                    if playerarmor > 10:
                        playerarmor = 10
                    print("[ 我方行动 ]")
                    print("[夜曲]使用技能3[防御阵型]")
                    print("当前护甲层数: ", playerarmor)
                if sun == "4":
                    healtarget = input("输入待修理无人机编号(01或02或03): ")
                    if healtarget == "01":
                        d1hp += 3
                        if d1hp > 5:
                            d1hp = 5
                    elif healtarget == "02":
                        d2hp += 3
                        if d2hp > 5:
                            d2hp = 5
                    elif healtarget == "03":
                        d3hp += 3
                        if d3hp > 5:
                            d3hp = 5
                    
                # drone condition
                # drones = {'drone01': 100, 'drone02': 80, 'drone03': 60}  
                # list(map(lambda drone: print(f'[{drone}]剩余生命值: {drones[drone]}'), drones))
                if dronenum == 1:
                    print("[无人机01]剩余生命值: ",d1hp)
                elif dronenum == 2:
                    print("[无人机01]剩余生命值: ",d1hp)
                    print("[无人机02]剩余生命值: ",d2hp)
                elif dronenum == 3:
                    print("[无人机01]剩余生命值: ",d1hp)
                    print("[无人机02]剩余生命值: ",d2hp)
                    print("[无人机03]剩余生命值: ",d3hp)

            if roundcon == 0:
                # enemy attack, random pick target
                print("[徘徊]发起攻击")
                if dronenum == 1:
                    etarget = random.randint(0,1)
                elif dronenum == 2:
                    etarget = random.randint(0,2)
                elif dronenum == 3:
                    etarget = random.randint(0,3)
                elif dronenum == 0:
                    etarget = 0

                # calculate damage caused by enemy
                if etarget == 0:
                    print("攻击：[徘徊]-->[夜曲]")
                if playerarmor == 0:
                    php -= 2
                print("[夜曲]受到2点物理伤害")
                if  playerarmor > 0 and playerarmor < eatk:
                    php = php - (eatk - playerarmor)
                    print("[夜曲]受到2点物理伤害，[护甲]挡下了",playerarmor,"点物理伤害")
                    playerarmor = 0
                if playerarmor >= eatk:
                    php = php
                    playerarmor = playerarmor - eatk
                    print("护甲挡下了",eatk,"点物理伤害，剩余",playerarmor,"层护甲")
                    print("[夜曲]未受到伤害")
                elif etarget == 1:
                    print("攻击：[徘徊]-->[无人机01]")
                    d1hp = d1hp - eatk
                    if d1hp <= 0:
                        d1hp = 0
                elif etarget == 2:
                    print("攻击：[徘徊]-->[无人机02]")
                    d2hp = d2hp - eatk
                    if d2hp <= 0:
                        d2hp = 0
                elif etarget == 3:
                    print("攻击：[徘徊]-->[无人机03]")
                    d3hp = d3hp - eatk
                    if d3hp <= 0:
                        d3hp = 0

            # round end ally hp result
            print()
            print("[ 回合结束：第",roundnum,"回合 ]")
            if dronenum == 0:
                print("[夜曲]剩余生命值: ",php)
            elif dronenum == 1:
                print("[夜曲]剩余生命值: ",php)
                if d1hp == 0:
                    print("[无人机01]已坠毁")
                else:
                    print("[无人机01]剩余生命值: ",d1hp)
            elif dronenum == 2:
                print("[夜曲]剩余生命值: ",php)
                if d1hp == 0:
                    print("[无人机01]已坠毁")
                else:
                    print("[无人机01]剩余生命值: ",d1hp)
                if d2hp == 0:
                    print("[无人机02]已坠毁")
                else:
                    print("[无人机02]剩余生命值: ",d2hp)
            elif dronenum == 3:
                print("[夜曲]剩余生命值: ",php)
                if d1hp == 0:
                    print("[无人机01]已坠毁")
                else:
                    print("[无人机01]剩余生命值: ",d1hp)
                if d2hp == 0:
                    print("[无人机02]已坠毁")
                else:
                    print("[无人机02]剩余生命值: ",d2hp)
                if d3hp == 0:
                    print("[无人机03]已坠毁")
                else:
                    print("[无人机03]剩余生命值: ",d3hp)
            print()
            print()

            # clean drone waste

            # 目前仅支持每回合最多失去一架无人机，出现AOE伤害后若一回合失去两架无人机将出现bug
            # Clean drone waste
            if d1hp == 0:
                if dronenum >= 1:
                    dronenum -= 1
                    d1hp = d2hp
                    d2hp = d3hp
                    d3hp = 0
            elif d2hp == 0:
                if dronenum >= 2:
                    dronenum -= 1
                    d2hp = d3hp
                    d3hp = 0
            elif d3hp == 0:
                if dronenum >= 3:
                    dronenum -= 1


        if chosench == "护符":
            # player choose one skill to use
            # sun = skill used number
            roundnum = roundnum + 1
            print("------------------------------------------------------------------")
            print()
            print()
            print("[ 开火已授权，作战开始 ]")
            print()
            print("对方信息: ")
            print(e1)
            print("生命值: ",e1hp)
            print()
            print("------------------------------------------------------------------")
            print()
            print("[ 回合开始：第",roundnum,"回合 ]")
            sun = input("输入技能对应数字并按下Enter：")
            print()
            if sun == "1" :
                e1hp = e1hp - 5
                print("[ 我方行动 ]")
                print("[护符]使用技能1[刃]")
                print("[徘徊]受到5点物理伤害")
                if e1hp < 0:
                    break
                else:
                    print("[徘徊]剩余生命值: ",e1hp)
            if sun == "2" :
                e1hp = e1hp - 3
                print("[ 我方行动 ]")
                print("[护符]使用技能2[锋]")
                print("[徘徊]受到3点物理伤害")
                if e1hp < 0:
                    break
                else:
                    talismanrage += 1
                    print("当前[怒气值]为: ",talismanrage)
                    print("[徘徊]剩余生命值: ",e1hp)
            if sun == "3":
                print("[护符]使用技能3[斩]")
                php -= 4
                enemyhploss = (150 - e1hp) // 10
                e1hp = e1hp - 2 - enemyhploss
                print("[徘徊]受到",2+3*enemyhploss,"点物理伤害")
                if e1hp < 0:
                    break
                else:
                    print("[护符]剩余生命值: ",php)
                    print("[徘徊]剩余生命值: ",e1hp)
            if sun == "4":
                php = php + 3 * talismanrage
                talismanrage = 0
                if php > 50:
                    php = 50
                print("[护符]剩余生命值: ",php)
                print("[徘徊]未受到攻击，生命值: ",e1hp)
                

            # enemy attack, random pick target
            print("[徘徊]发起攻击")
            # calculate damage caused by enemy: 
            print("攻击：[徘徊]-->[护符]")
            if playerarmor == 0:
                php -= 2
            print("[护符]受到2点物理伤害")

            # round end ally hp result
            print()
            print("[ 回合结束：第",roundnum,"回合 ]")

            print("[护符]剩余生命值: ",php)


            print()
            print()



    if php <= 0:
        print()
        print("[",chosench,"]被击败")

    if e1hp <= 0:
        print()
        print("[徘徊]被击败")
        print()








    '''
        if player == "talisman":
            s1 = "技能1: [刃]"
            s1d = "     消耗1枚白币，造成6点物理伤害。获得1点充能"
            s2 = "技能2: [锋]"
            s2d = "     消耗3枚白币，造成5点物理伤害，每有1架[无人机]额外造成3点物理伤害。获得1点充能"
            s3 = "技能3: [防御阵型]"
            s3d = "     消耗3枚黑币，每有1架[无人机]为[夜曲]附属3层[护甲]。获得1点充能"
            s4 = "技能4: [机身维护]"
            s4d = "     消耗2枚黑币，为所有[无人机]恢复10点生命值"
    '''

# PVP mode
if modech == "对决":
    print("请选择角色:")
    ch = { 
        'ch1' : "夜曲",
        'ch2' : "护符",
        'ch3' : "水银"
        }

    print(ch['ch1'],ch['ch2'],ch['ch3'])

    p1chosench = input("玩家1，请输入所选角色：")
    p2chosench = input("玩家2，请输入所选角色：")


    if p1chosench == "夜曲":
        p1 = "lullaby"
        print("玩家1已选择角色：",ch['ch1'])
    elif p1chosench == "护符":
        p1 = "talisman"
        print("玩家1已选择角色：",ch['ch2'])
    elif p1chosench == "水银":
        p1 = "mercury"
        print("玩家1已选择角色：",ch['ch3'])

    if p2chosench == "夜曲":
        p2 = "lullaby"
        print("玩家2已选择角色：",ch['ch1'])
    elif p2chosench == "护符":
        p2 = "talisman"
        print("玩家2已选择角色：",ch['ch2'])
    elif p2chosench == "水银":
        p2 = "mercury"
        print("玩家2已选择角色：",ch['ch3'])


    print("------------------------------------------------------------------")
    print()
    print("[ 准备阶段 ]")


    if p1chosench == "lullaby":
        p1hp = 40
        s1 = "技能1: [无人机升空]"
        s1d = "     召唤[无人机]，最多召唤3架"
        s2 = "技能2: [空中打击]"
        s2d = "     造成5点物理伤害，每有1架[无人机]额外造成3点物理伤害"
        s3 = "技能3: [防御阵型]"
        s3d = "     每有1架[无人机]为[夜曲]附属1层[护甲]，最多叠加10层"
        s4 = "技能4: [机身维护]" 
        s4d = "     为所有[无人机]恢复10点生命值"

    if p1chosench == "talisman":
        p1hp = 50
        s1 = "技能1: [刃]"
        s1d = "     造成6点物理伤害"
        s2 = "技能2: [锋]"
        s2d = "     造成5点物理伤害，怒气值+1"
        s3 = "技能3: [斩]"
        s3d = "     失去5点生命值，造成2点物理伤害，对方每已损失1点生命值，伤害额外+1"
        s4 = "技能4: [狂]"
        s4d = "     消耗所有怒气值，每1点怒气值，恢复2点生命值"
