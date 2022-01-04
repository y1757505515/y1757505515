import xlrd
import xlwt
open_book=xlrd.open_workbook(filename="百度合作单位-人员管理-二期.xls",encoding_override=True)
sheet=open_book.sheet_by_index(0)
col=sheet.ncols
row=sheet.nrows
print("总人数为：",int(len(sheet.col_values(0))-1))


#男女人数
x={"男":0,"女":0}
list_pohon1=sheet.col_values(8)[1:]
for i in range(int(len(sheet.col_values(8))-1)):
    if list_pohon1[i]=="男":
        x["男"]=x["男"]+1
    if list_pohon1[i]=="女":
        x["女"]=x["女"]+1
print("男女数量分别是:",x)


#运营商数量
# a={"移动":0,"联通":0,"电信":0}
# for i in range(int(len(sheet.col(5)))-1):
#     list_pohon2 = list(sheet.col_values(5)[1:])[i]
#     if list_pohon2[0:2]=="13":
#         a["移动"]=a["移动"]+1
#     elif list_pohon2[0:2]=="14" or list_pohon2[0:2]=="17":
#         a["电信"]=a["电信"]+1
#     elif list_pohon2[0:2]=="15":
#         a["联通"]=a["联通"]+1
# print("运营商分别为:",a)

a={"移动":0,"联通":0,"电信":0}
list_pohon13=sheet.col_values(5)
for i in list_pohon13:
    i=str(i)
    if i.startswith("14") or i.startswith("17"):
        a["电信"]=a["电信"]+1
    elif i.startswith("13"):
        a["移动"]=a["移动"]+1
    elif i.startswith("15"):
        a["联通"]=a["联通"]+1
print("运营商分别为:",a)




# 超过45岁的人数
c={"老员工":0}
list_popon3=sheet.col_values(7)[1:]
for i in range(int(len(sheet.col_values(7))-1)):
    if list_popon3[i]>45:
        c["老员工"]=c["老员工"]+1
print("超过45岁的人员有:",c)


# 薪资统计
b={"高薪人员":0,"低薪人员":0}
list_popon4=sheet.col_values(11)[1:]
for i in range(int(len(sheet.col_values(11))-1)):
    if list_popon4[i]>8000:
        b["高薪人员"]=b["高薪人员"]+1
    elif list_popon4[i]<3000:
        b["低薪人员"]=b["低薪人员"]+1
print("高低薪酬非别为:",b)


#在传媒公司人数统计
list_popon5=sheet.col_values(13)
sum=0
for i in range(int(len(sheet.col_values(13))-1)):
    list_gs=list_popon5[i]
    if "传媒" in list_gs:
        sum=sum+1
print("传媒公司人数：",sum)


# 疫情区域统计
# d={"黑龙江":0,"北京":0,"福建":0,"四川":0}
# for i in range(int(len(sheet.col(9)))-1):
#     list_pohon6 = list(sheet.col_values(9)[1:])[i]
#     if list_pohon6[0:3]=="黑龙江":
#         d["黑龙江"]=d["黑龙江"]+1
#     elif list_pohon6[0:3]=="福建省":
#         d["福建"]=d["福建"]+1
#     elif list_pohon6[0:3]=="北京市":
#         d["北京"]=d["北京"]+1
#     elif list_pohon6[0:3]=="四川省":
#         d["四川"]=d["四川"]+1
# print("在疫情区域人数统计:",d)

d={"黑龙江":0,"北京":0,"福建":0,"四川":0}
list_pohon6=sheet.col_values(9)
for i in list_pohon6:
    i=str(i)
    if i.startswith("黑龙江"):
        d["黑龙江"]=d["黑龙江"]+1
    elif i.startswith("北京市"):
        d["北京"]=d["北京"]+1
    elif i.startswith("福建省"):
        d["福建"]=d["福建"]+1
    elif i.startswith("四川省"):
        d["四川"]=d["四川"]+1
print("在疫情区域人数统计:",d)

