import requests as rq
import random
import time
import schedule 

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
        alive = "alive" # 保活模块

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

    def keep_alive(self):
        url = Setting.urls.root + Setting.urls.alive
        data = {
            "id": self.id,
            "time": time.time()
        }
        try:
            ret = rq.post(url, json=data).json()
            print(ret)
        except:
            Error.NetworkError()
        
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
            schedule.every(10).seconds.do(self.keep_alive)
        except:
            Error.NetworkError()
            return False
        return True

    def start(self): # 开始循环
        while not self.connect():
            time.sleep(4.9)
        # 循环队列
        while True:
            schedule.run_pending()
            time.sleep(0.2)



Furry = Controller()
Furry.start()
