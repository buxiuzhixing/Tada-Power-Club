import time as t
print("欢迎来到蝌粉俱乐部！\n请输入用户名与密码,账号不存在将自动创建")
y=input("用户名：")
p=input("密码：")
g=float(input("您的年龄？"))
yzm=float(input("验证码：114514："))
if yzm==114514:
    print("蝌粉,欢迎登录\n================\n您现在在大厅\n================\na=进入_蝌蚪SeaDream_的放映厅\nb=注销\nc=留在大厅")
    menu=input("您现在想做什么？")
    if menu=="a":
        print("========\n放映厅正在播放_蝌蚪SeaDream_的《论史蒂夫的重量》快去看看吧！https://b23.tv/gZLM6es\na=返回大厅\nb=注销\nc=点赞\nd=投币\ne=收藏\nf=打赏")
        while True:
            menu=input("您现在想做什么？")
            if menu=="c":
                print("点赞成功！")
            if menu=="d":
                bi=1
                print("投币成功！余额：",bi-1)
            if menu=="e":
                print("收藏成功！")
            if menu=="f" and g>=18:
                yuan=100
                print("打赏成功！余额：",yuan-10)
            if menu=="f" and g<18:
                print("未成年人不允许打赏哦！")
            if menu=="b":
                print("您已注销！")
                break
            if menu=="a":
                print("你已返回大厅！")
                t.sleep(3)
                print("警报！病毒入侵！")
                t.sleep(3)
                print("怪怪鼠鼠：泥🔒嘢I嘚，4泥滴森佛")
                t.sleep(3)
                print("admin：糟了！病毒被释放了！")
                t.sleep(3)
                print(y,"：你是？")
                t.sleep(3)
                print("admin：我是蝌粉俱乐部的管理员，被我关进小黑屋的病毒出来了！快帮我打败它！")
                t.sleep(3)
                print(y,"：好！")
                t.sleep(1)
                print("a=点赞攻击\nb=用硬币砸死它")
                attack=input("发起攻击：")
                if attack=="a":
                    print("你居然给鼠鼠点赞\n你死了！")
                    break
                if attack=="b":
                    print("你的硬币余额不足！怪怪鼠鼠的HP还有50%")
                    t.sleep(1)
                    print("不好，它向你发起攻击！")
                    t.sleep(1)
                    print("admin：你▓什么时候▓啊！")
                    t.sleep(1)
                    print("怪怪鼠鼠消失了")
                    t.sleep(3)
                    print(y,"：终于……")
                    for i in range(3):
                        print("警报！系统错误，检测到非法行为，强制注销！")
                    t.sleep(1)
                    print(y,"：发生什么了？")
                    t.sleep(1)
                    print("admin：病毒已经攻击到内部了！")
                    t.sleep(3)
                    print("服务器即将关闭：3")
                    t.sleep(1)
                    print("服务器即将关闭：2")
                    t.sleep(1)
                    print("服务器即将关闭：1")
                    t.sleep(1)
                    print("您已强制注销！\n感谢游玩！")
                    shell=input("~$ ")
                    if shell=="login":
                        mi=input("密码：")
                        if mi==p:
                            print("admin：你又回来了！")
                            t.sleep(1)
                            print("admin：帮我找一找哪个程序不对，怪怪鼠鼠就藏在那。")
                            print("A.😀\nB.😀\nC.😅")
                            answer=input("回答：")
                            if answer=="C":
                                print("admin：感谢你帮我找到病毒，我现在就消灭病毒！稍等10秒就行。")
                                t.sleep(10)
                                print("服务器重启，3")
                                t.sleep(1)
                                print("服务器重启，2")
                                t.sleep(1)
                                print("服务器重启，1")
                                t.sleep(1)
                                print("admin：服务器重启成功！感谢你拯救蝌粉俱乐部！\n感谢游玩KF Club！")
                                break
                            else:
                                print("admin：病毒不在这！")
                                print("蝌粉俱乐部又被吞噬了！")
                                break
                    else:
                        break
    if menu=="b":
        print("您已注销！")
    if menu=="c":
        print("你遇到了一位老人！")
        t.sleep(3)
        print("老人：骚年，我是豆科•二八克，很荣幸你成为了我的财产继承人，你已得到GiliGili永久超级大会员！并获得无限硬币，快去试试吧!")
        t.sleep(1)
        huiche=input("回车立即前往GiliGili")
        print("========\n放映厅正在播放_蝌蚪SeaDream_的《论史蒂夫的重量》快去看看吧！https://b23.tv/gZLM6es\na=返回大厅\nb=注销\nc=点赞\nd=投币\ne=收藏\nf=打赏")
        while True:
            menu=input("您现在想做什么？")
            if menu=="a":
                print("你已返回大厅！")
                t.sleep(3)
                print("警报！病毒入侵！")
                t.sleep(3)
                print("怪怪鼠鼠：泥🔒嘢I嘚，4泥滴森佛")
                t.sleep(3)
                print("admin：糟了！病毒被释放了！")
                t.sleep(3)
                print(y,"：你是？")
                t.sleep(3)
                print("admin：我是蝌粉俱乐部的管理员，被我关进小黑屋的病毒出来了！快帮我打败它！")
                t.sleep(3)
                print(y,"：好！")
                t.sleep(1)
                print("a=点赞攻击\nb=用硬币砸死它")
                attack=input("发起攻击：")
                if attack=="a":
                    print("你居然给鼠鼠点赞\n你死了！")
                    break
                if attack=="b":
                    print("你使用硬币攻击！鼠鼠HP还剩1%")
                    t.sleep(1)
                    print("不好它准备向你发起攻击!")
                    t.sleep(3)
                    print("admin：你▓什么时候▓啊！")
                    t.sleep(1)
                    print("成功击败！")
                    t.sleep(1)
                    print("admin：感谢你解救了蝌粉俱乐部！\n感谢游玩！")
                    break
            if menu=="b":
                print("您已注销！")
                break
            if menu=="c":
                print("点赞成功！")
            if menu=="d":
                print("投币成功！余额：∞")
            if menu=="e":
                print("已收藏！")
            if menu=="f" and g>=18:
                print("打赏成功！余额：∞")
            if menu=="f" and g<18:
                print("未成年人不允许打赏哦！")
