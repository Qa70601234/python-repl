# -*- coding: utf-8 -*-
# @Time    : 2023-4-21
# @Author  : mogui    flask可视化模板
# @Email   : 
# @File    : app.py

from random import randrange
from flask import Flask, render_template
from flask.json import jsonify
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
import pymysql,os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv('.env'))
env_dist = os.environ



#app = Flask(__name__, static_folder="templates")
app = Flask(__name__)

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


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "耐克", "阿迪达斯", "裤子", "高跟鞋", "袜子"])
        #.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        #.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家A", [33,44,22,55,23,my_echart()[1]])
        .add_yaxis("商家B", [33,41,12,15,23,my_echart()[0]])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

idx = 9

@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


@app.route("/templates")
def line():
    return render_template("line_on.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=5000)