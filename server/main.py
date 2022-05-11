from sanic import Sanic
from sanic.response import json
from sanic.request import Request
import time
import asyncio

furry = Sanic("Hashfurry")

furry.ctx.online = {

}




def ret(code, message, data="empty", statuss=200):
    d = {
        "code": code,
        "message": message,
        "data": data,
        "time": time.time(),
    }
    return json(d, status=statuss)

async def online_check(): # 检查节点是否存活
    while True:
        await asyncio.sleep(5)
        m = furry.ctx.online.keys()
        for i in list(m):
            n = furry.ctx.online.get(i)
            t = n.get("last_alive")
            t = int(t)
            now = int(time.time())
            if now - t > 61:
                ids = furry.ctx.online.pop(i)
                print("ID: {} 超时".format(i))

furry.add_task(online_check())        

@furry.post("/reg")
async def reg(request: Request):
    try:
        data = request.json
        ids = data["id"]
        ver = data["version"]
        if ids in furry.ctx.online.keys():
            return ret(101, "Device ID already use")
        print("设备加入 ID:{} Ver:{}".format(ids, ver))
        furry.ctx.online[ids] = {
            "version": ver,
            "last_alive": data["time"]
        }
        return ret(200, "success")
    except Exception(e):
        return ret(999, "Unknown Error", e)


furry.run(host="0.0.0.0", port=80, fast=True, access_log=False)
