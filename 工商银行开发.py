import random
import time
from 连接 import select,inster
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
bank={}
# bank = {'1': {'account': 123, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门',
#               'money': 1000, 'bank_name': '中国工商银行'}}

#bank={'1': {'account': 45234580, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'},'2': {'account': 45234580, 'password': 123456, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'},
#'3': {'account': 66666666, 'password': 654321, 'country': '中国', 'province': '台湾', 'street': '台湾的街道', 'door': '台湾的门', 'moeny': 1000, 'bank_name': '中国工商银行'}}

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
                    1、用户名%s
                    2、密码******
                    3、国家%s
                    4、省份%s
                    5、街道%s
                    6、门派%s
                    7、账户%s
                    8、钱%s
        '''
        sql="select money from user where username=%s"
        param=username
        date=int(select(sql,param,mode="one")[0])
        print(info %(username,  country, province, street, door,account,date))
    elif a == 2:
        print("重名")
    elif a == 3:
        print("已满")

def repeater(name):
    sql="select username from user where username=%s"
    param=[name]
    data=len(select(sql,param))
    return data
def max():
    sql="select username from user where money>=0"
    data=len(select(sql))
    return data

def addbank(account, username, password, country, province, street, door):
    if max() >= 100000000:
        return 3
    elif repeater(username) !=0:
        return 2
    else:
        sql="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param=[account,username,password,country,province,street,door,0,time.strftime("%Y-%m-%d %H:%M:%S"),bank_name]
        inster(sql,param)
    return 1
    # else:
    #     bank[username] = {
    #         "account": account,
    #         "password": password,
    #         "country": country,
    #         "province": province,
    #         "street": street,
    #         "door": door,
    #         "moeny": 0,
    #         "bank_name": bank_name
    #     }
    #     return 1

def account(username):
    sql="select username from user where username=%s"
    param=[username]
    if len(select(sql,param))!=0:
        data=select(sql,param)[0][0]
        return data
    else:
        return 2


def cunqian():
    username=input("请输入您的用户名")
    a=account(username)
    if username==a:
        c=int(input("请输入存款金额"))
        param=[c,username]
        sql="update user set money=money+%s where username=%s"
        inster(sql,param)
        print("存款成功")
    elif a==2:
        print("账号不存在")

def passs(password):
    sql="select password from user where username=%s"
    param=[password]
    data=int(select(sql,param,mode="one")[0])
    return data
def balance(username):
    sql="select money from user where username=%s"
    param=[username]
    date=int(select(sql, param,mode="one")[0])
    return date
def quqian():
    username=input("请输入您的用户名")
    a=account(username)
    if username==a:
        password=int(input("请输入您的密码"))
        a=passs(password)

        if password==a:
            money=input("请输入取款金额")
            residue=balance(username)
            if int(money)<residue:
                sql="update user set money=money-%s where username=%s"
                param=[money,username]
                inster(sql,param)
                print("取款成功")
            else:
                print("余额不足")
                return 3
        else:
            print("密码错误")
            return 2
    else:
        print("用户名不存在")
        return 1


def name(username):
    sql="select username from user where username=%s"
    param=[username]
    if len(select(sql,param)) !=0:
        data=select(sql,param)[0][0]
        return data
    else:
        return 2
def name2(username):
    sql="select username from user where username=%s"
    param=[username]
    if len(select(sql,param))!=0:
        data=select(sql,param)[0][0]
        return data
    else:
        return 2


def p(username):
     sql="select password from user where username=%s"
     param=[username]
     data=int(select(sql,param,mode="one")[0])
     return data


def zhuanzhang():
    username=input("请输入您的用户名")
    a=name(username)
    if username==a:
        username2=input("请输入收款方用户名")
        b=name2(username2)
        if username2==b:
            password=int(input("请输入密码"))
            c=p(username)
            if password==c:
                money=int(input("请输入转账金额"))
                yue=balance(username)
                if money<=yue:
                    sql="update user set money=money-%s where username=%s"
                    param=[money,username]
                    inster(sql,param)
                    sql2="update user set money=money+%s where username=%s"
                    param2=[money,username2]
                    inster(sql2,param2)
                    print("转账成功")
                else:
                    print("您的余额不足")
            else:
                print("密码输入错误")
        elif b==2:
            print("收款方用户名错误")
    elif a==2:
        print("无此用户名")


def chaxun():
    username=input("请输入您的用户名:")
    a=account(username)
    if username==a:
        password=int(input("请输入您的密码:"))
        b=passs(password)
        if password==b:
            sql="select * from user where username=%s"
            param=[username]
            print(select(sql,param))
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
    cunqian()
elif o == "3":
    print("取钱")
    quqian()
elif o == "4":
    print("转账")
    zhuanzhang()
elif o == "5":
    print("账户查询")
    chaxun()
elif o == "6":
    print("退出系统")
