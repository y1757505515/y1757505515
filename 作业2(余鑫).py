
list_name = [
    ["可乐", 5],
    ["雪碧", 5],
    ["奶茶", 5],
    ["矿泉水", 100],
    ["龙井", 50],
]
moeny = 500  # 钱
mycar = []  # 购物车
a=0
while True:  # 循环
    for i in enumerate(list_name):
        print(i)
    shop = input("请输入商品编号")
    if shop.isdigit():
        shop = int(shop)
        if 0 <= shop <= 4:
            if moeny >= list_name[shop][1]:
                mycar.append(list_name[shop])
                # moeny = moeny - list_name[shop][1]
                # moeny=moeny-(list_name[shop][1]*0.8)
                a=a+list_name[shop][1]
                print("购买成功已经加入购物车，总计为", a)
        else:
          print("no")
    elif shop == "q" or shop == "Q":
        print("欢迎下次光临以下是您购买的详细内容：")
        for i in enumerate(mycar):
            print(i)
        import random
        o=random.randint(1,2)
        if o==1:
            a=a*0.8
        else:
            a=a*0.85
        if a >= 200:
            moeny = moeny - (a - 20)
            print("剩余金额为：", moeny)
        else:
            moeny=moeny-a
            print("剩余金额为",moeny)
        break
    else:
        print("no")