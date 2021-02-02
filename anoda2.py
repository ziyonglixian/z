import random
import threading

import requests

url = "http://txt1.qiyehuangyewang.com:2974/?fromuid=1090393"
cookie = "yj0M_7b23_saltkey=fqKkgh1c; yj0M_7b23_lastvisit=1612270558; yj0M_7b23_seccode=112057.c24612e444279b2cfb; yj0M_7b23_ulastactivity=1612274294%7C0; yj0M_7b23_auth=3076dZ8AwyyJxrIv%2FmIayz5QuzArcZoODJut4COaW0YXtO7kZK0eVWelEussEzPRpyXuBeWt1dBm2AdyExJHKOY4xwKU; yj0M_7b23_nofavfid=1; yj0M_7b23_taskdoing_1090393=1; yj0M_7b23_sendmail=1; yj0M_7b23_noticeTitle=1; yj0M_7b23_lastact=1612275307%09home.php%09spacecp; yj0M_7b23_checkpm=1"
headers1 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "cookie": cookie,
}
url1 = "http://txt2.qiyehuangyewang.com:2974/home.php?mod=task&do=apply&id=2"


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "X-forwarded-for": str(ip),
        "x-client-ip": str(ip),
        "Client_ip": str(ip),
    }

    headers3 = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "cookie": cookie,
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "DNT": "1",
        "Proxy-Connection": "keep-alive",
        "Referer":
        "http://txt1.qiyehuangyewang.com:2974/home.php?mod=task&item=doing",
        "Upgrade-Insecure-Requests": "1"
    }
    url3 = "http://txt2.qiyehuangyewang.com:2974/home.php?mod=task&do=draw&id=2"
    res3 = requests.get(url=url3, headers=headers3)
    print(res3)


for i in range(200):
    t = threading.Thread(target=q)
    t.start()
