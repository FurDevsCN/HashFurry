import requests as rq
import random
import time

'''
    配置
'''
class Setting():
    @staticmethod
    class versions():
        client = 1 # 客户端版本

    @staticmethod
    class urls():
        root = "http://127.0.0.1/" # 网站根目录
        connect = "reg" # 连接模块

'''
    错误输出
'''
class Error():
    @staticmethod
    def NetworkError():
        print("网络连接错误，请等待重试")
        time.sleep(3)

'''
    控制器
'''
class Controller():
    def __init__(self, _id=None):
        if _id is None:
            _id = random.randint(10**9+1, 10**10)
        self.id = _id

    @staticmethod
    def help():
        print(Setting.urls.root)
        pass


    def connect(self):
        url = Setting.urls.root + Setting.urls.connect
        data = {
            "id": self.id,
            "time": time.time(),
            "version": Setting.versions.client
        }
        try:
            ret = rq.post(url, json=data).json()
            print(ret)
        except:
            Error.NetworkError()
            self.connect()



Furry = Controller(111111)
Furry.connect()

