
import pymysql
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv('.env'))
env_dist = os.environ

def my_echart():
    conn = pymysql.connect(host='host.408200.cf', user='ubuntu', password='q7060123', db='date')#建立数据库连接
    cur = conn.cursor()
    sqlmale = ' SELECT * FROM  people_flow'
    cur.execute(sqlmale)#执行单条sql语句
    maleresult = cur.fetchall()#接收全部的返回结果行
    man_num = maleresult[0][1]
    woman_num = maleresult[1][1]
    cur.close()#关闭指针对象
    conn.close()#关闭连接对象
    print(man_num,woman_num)#测试


def env():
    
    #env_dist = os.environ
    #print(env_dist.get('host'))
    #print(env_dist.get('user'))
    #print(env_dist.get('db'))
    port = env_dist.get('port')
    print(port)
def my_echart():
    
    host = env_dist.get('host')
    user = env_dist.get('user')
    password = env_dist.get('password')
    db = env_dist.get('db')
    
    conn = pymysql.connect(host=host, user=user, password=password, db=db)#建立数据库连接
    cur = conn.cursor()
    sqlmale = ' SELECT * FROM  people_flow'
    cur.execute(sqlmale)#执行单条sql语句
    maleresult = cur.fetchall()#接收全部的返回结果行
    man_num = maleresult[0][1]
    woman_num = maleresult[1][1]
    cur.close()#关闭指针对象
    conn.close()#关闭连接对象
    return man_num,woman_num
if __name__ == '__main__' :
    #my_echart()
    #port = int(os.environ.get('PORT', 6000))
    #env()
    #print(port)
    print(my_echart())