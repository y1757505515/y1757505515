import random

bank_name = "中国工商银行"

print('*********************************')
print('*     中国工商银行               *')
print("*********************************")
print("|   1、开户                      |")
print("|   2、存钱                      |")
print("|   3、取钱                      |")
print("|   4、转账                      |")
print("|   5、查询                      |")
print("|   6、再见                      |")
print("*********************************")
# bank={}
# bank = {'1': {'account': 123, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门',
#               'money': 1000, 'bank_name': '中国工商银行'}}

bank={'1': {'account': 45234580, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'},'2': {'account': 45234580, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'},
'3': {'account': 66666666, 'password': 654321, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'}}

def adduser():
    account = random.randint(10000000, 99999999)
    username = input("请输入您用户名")
    password = int(input("请输入您的密码"))
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    a = addbank(account, username, password, country, province, street, door)
    if a == 1:
        print("开户成功,以下是您的详细信息")
        info = '''
                =========中国工商银行=======
                    1、用户名：%s
                    2、账号：%s
                    3、密码：%s
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % ( username,account, password, country, province, street, door, bank[username]["moeny"]))
    elif a == 2:
        print("重名")
    elif a == 3:
        print("已满")


def addbank(account, username, password, country, province, street, door):
    if len(bank) >= 100:
        return 3
    elif username in bank:
        return 2
    else:
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "moeny": 0,
            "bank_name": bank_name
        }
        return 1


def addmoeny():
    while True:
        username=input("请输入你的用户名:")
        if addmoeny1(username) is True:
            moeny=input("请输入您需要存款的金额:")
            moeny=int(moeny)
            bank[username]["moeny"]+=moeny
            print("您的账户余额:",bank[username]["moeny"])
            break
        else:
            print("用户名错误")


def addmoeny1(username):
    if username not in bank:
        return False
    else:
        return True


def popmoeny():
    while True:
        username=input("请输入您的用户名:")
        password=input("请输入您的密码:")
        password=int(password)
        money=input("请输入取款金额:")
        money=int(money)
        a=popmoeny1(username,password,money)
        if a==0:
            bank[username]["moeny"]-=money
            print("您的余额为:",bank[username]["moeny"])
            break
        elif a==1:
            print("您输入的用户名错误")
        elif a==2:
            print("你输入的密码错误")
        elif a==3:
            print("您的账户余额不足")


def popmoeny1(username,password,money):
    if username in bank:
        if password==bank[username]["password"]:
            if money>bank[username]["moeny"]:
                return 3
            else:
                return 0
        elif password!=bank[username]["password"]:
            return 2
    else:
        return 1


def remoeny():
    username_chu=input("请输入您的账户")
    username_jin=input("输入转账账户")
    password=input("输入您的密码")
    password=int(password)
    moeny=input("你需要转账的金额:")
    moeny=int(moeny)
    a=remoeny1(username_chu,username_jin,password,moeny)
    if a==0:
        bank[username_chu]["moeny"]-=moeny
        bank[username_jin]["moeny"]+=moeny
        print("您的余额为:",bank[username_chu]["moeny"],bank[username_jin]["moeny"])

    elif a==1:
        print("您输入的账号错误")
    elif a==2:
        print("你输入的密码错误")
    elif a==3:
        print("您的余额不足")


def remoeny1(username_chu,username_jin,password,moeny):
    if username_chu in bank:
        if username_jin in bank:
            if password==bank[username_chu]["password"]:
                if moeny<bank[username_chu]["moeny"]:
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 1


def search():
    username=input("请输入您的用户名:")
    while True:
        password=input("请输入您的密码:")
        password=int(password)
        if username in bank:
            if password==bank[username]["password"]:
                print("以下是您的详细信息",bank[username])
                break
            else:
                print("您输入的密码错误")
        else:
            print("该用户不存在")


o = input("请选择业务")
if o == "1":
    print("开户")
    adduser()
elif o == "2":
    print("存钱")
    addmoeny()
elif o == "3":
    print("取钱")
    popmoeny()
elif o == "4":
    print("转账")
    remoeny()
elif o == "5":
    print("查询")
    search()
elif o == "6":
    pass
