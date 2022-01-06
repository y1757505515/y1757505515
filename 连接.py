import pymysql
def select(sql,param="",mode="all",size=""):
    con=pymysql.connect(host="localhost",user="root",password="",database="bank")
    cur=con.cursor()
    if len(param) !=0:
        cur.execute(sql,param)
    else:
        cur.execute(sql)
    if mode =="one":
        return cur.fetchone()
    elif mode =="all":
        return cur.fetchall()
    elif mode =="many":
        return cur.fetchmany(size=size)
    cur.close()
    con.close()
def inster(sql,param):
    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cur = con.cursor()
    cur.execute(sql,param)
    con.commit()
    cur.close()
    con.close()