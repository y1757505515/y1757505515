import random
bank_name="中国工商银行"

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
bank={}
# bank={"Frank": {"account": "12345678", "password": 123456, "country": "中国", "province": "台湾", "street": "台湾的街道", "door": "台湾的门", "money": 2, "bank_name": "中国工商银行"},
#       "123": {"account": "12345678", "password": 123456, "country": "中国", "province": "台湾", "street": "台湾的街道", "door": "台湾的门", "money": 2, "bank_name": "中国工商银行"}}
def adduser():
    account=random.randint(10000000,99999999)
    username=input("请输入您用户名")
    password=int(input("请输入您的密码"))
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    a=addbank(account, username, password, country, province, street, door)
    if a==1:
        print("开户成功,以下是您的详细信息")
        info='''
                =========中国工商银行=======
                    1、用户名%s
                    2、******%s
                    3%s
                    4%s
                    5%s
                    6%s
                    7、账号%s
                    8%s
        '''
        print(info %(username, password, country, province, street, door,account,bank[username]["money"]))
    elif a==2:
        print("重名")
    elif a==3:
        print("已满")


def addbank(account,username,password,country,province,street,door):
    if len(bank)>=100:
        return 3
    elif username in bank:
        return 2
    else:
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

def cunqian():
    username=input("请输入您的用户名")
    zhanghao=int(input("请输入账号"))
    if zhanghao==bank[username]["account"]:
        a=int(input("请输入存款金额"))
        money=a+int(bank[username]["money"])
        bank[username]["money"]=money
        print("存款成功")
    else:
        print("账号不存在")




def quqian():
    username=input("请输入您的用户名")
    if username in bank.keys():
        mima=int(input("请输入您的密码"))
        if mima==bank[username]["password"]:
            jine=input("请输入取款金额")
            if int(jine)<int(bank[username]["money"]):
                money=int(bank[username]["money"])-int(jine)
                bank[username]["money"]=money
            else:
                print("余额不足")
                return 3
        else:
            print("密码错误")
            return 2
    else:
        print("用户名不存在")
        return 1

def zhuanzhang():
    username=input("请输入转入账号用户名")
    zhuanru=input("请输入转入账号")
    usernames=input("请输入转出账号用户名")
    zhuanchu = input("请输入转出账号")
    if zhuanru in bank[username]["account"] and zhuanchu in bank[usernames]["account"]:
        mima=int(input("请输入密码"))
        if mima==bank[usernames]["password"]:
            jine=int(input("请输入转账金额"))
            if jine<=bank[usernames]["money"]:
                bank[usernames]=bank[usernames]["money"]-jine
                bank[username]=bank[username]["money"]+jine
            else:
                return 3
        else:
            return 2
    else:
        return 1

def chaxun():
    username=input("请输入用户名")
    if username in bank.keys():
        mima=int(input("请输入密码"))
        if mima==bank[username]["password"]:
            print("当前账号",bank[username]["account"],  "密码:","*****",  "余额:",bank[username]["money"],
                  "用户住址",bank[username]["country"],bank[username]["province"],bank[username]["street"],bank[username]["door"],  "当前账户开户行:",bank[username]["bank_name"])
        else:
            print("密码错误")
    else:
        print("用户名不存在")








while True:
    o=input("请选择业务")
    if o =="1":
        print("1、开户")
        print(bank)
        adduser()
    elif o=="2":
        print("存钱")
        cunqian()
    elif o=="3":
        print("取钱")
        quqian()
    elif o=="4":
        print("转账")
        zhuanzhang()
    elif o=="5":
        print("账户查询")
        chaxun()
