from flask import Flask
from imooc import route_imooc

app = Flask(__name__)
app.register_blueprint(route_imooc,url_prefix="/imooc")


@app.route("/")
def hello_world():
    return "hello word"

if __name__ == '__main__':
    app.run(debug=True)