from flask import Blueprint  #引入蓝图

route_imooc = Blueprint("imooc_page",__name__) #创建蓝图对象

@route_imooc.route("/")
def index():
    return "immoc index page"