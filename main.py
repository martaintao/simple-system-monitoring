# encoding=utf8
from flask import Flask, request, jsonify, session, render_template
from flask_pymongo import PyMongo
from gevent import pywsgi
from flask_cors import CORS
import random
import time

app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)
app.config["MONGO_URI"] = "mongodb://localhost:27017/visual"
mongo = PyMongo(app)


@app.route('/')
def index():
    """
    页面入口
    """
    return render_template("index.html")


@app.route('/getCpuStatus')
def get_cup_status():
    """
    模拟获取系统CPU状态
    """
    cpu_total = 100
    cpu_use = round(random.uniform(0, cpu_total), 2)
    cpu_unit = "%"
    now = int(round(time.time()*1000))
    res = {
        "total": cpu_total,
        "use": cpu_use,
        "unit": cpu_unit,
        "time": now
    }
    result = success_with_data(res)
    mongo.db.cpu_record.insert_one(res)
    return result


@app.route("/getCpuHistoryStatus")
def get_cpu_history_status():
    """
    获取cpu的历史数据
    """
    records = mongo.db.cpu_record.find().limit(100)
    data = []
    for record in records:
        item = {
            "total": record["total"],
            "use": record["use"],
            "unit": record["unit"],
            "time": record["time"]
        }
        data.append(item)
    return success_with_data(data=data)


@app.route('/getMemoryStatus')
def get_memory_status():
    """
    模拟获取系统内存状态
    """
    memory_total = 16
    memory_use = round(random.uniform(0.5*memory_total, memory_total), 2)
    memory_unit = "GB"
    now = int(round(time.time()*1000))
    res = {
        "total": memory_total,
        "use": memory_use,
        "unit": memory_unit,
        "time": now
    }
    result = success_with_data(res)
    mongo.db.memory_record.insert_one(res)
    return result


@app.route("/getMemoryHistoryStatus")
def get_memory_history_status():
    """
    获取内存的历史数据
    """
    records = mongo.db.memory_record.find().limit(100)
    data = []
    for record in records:
        item = {
            "total": record["total"],
            "use": record["use"],
            "unit": record["unit"],
            "time": record["time"]
        }
        data.append(item)
    return success_with_data(data=data)

###################### 封装的返回Response ######################


def success():
    return response(0, "success")


def success_with_data(data):
    return response(0, "success", data)


def fail(msg):
    return response(-1, msg)


def response(code, msg, data=''):
    return jsonify({'code': code, 'msg': msg, 'data': data})

# 封装的返回Response ###################### End


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 8090), app)
    server.serve_forever()
