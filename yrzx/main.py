# -*- coding: utf-8 -*-
'''
     @Time    : 2019/2/1 14:39
     @Author  : wsh_oo
     @File    : main.py
     @Software: PyCharm
'''
from urllib.request import urlretrieve, urljoin, build_opener, install_opener, Request, urlopen
from fake_useragent import UserAgent
import threading
import os
import ssl
import json


ssl._create_default_https_context = ssl._create_unverified_context # SSL Error
base_url = 'https://www.tohomh123.com/action/play/read?did=7155&sid={0}&iid={1}'
base_dir = r'./yrzx/yrzx'
os.makedirs(base_dir, exist_ok=True)
ua = UserAgent()
header = {'User-Agent': ua.random}

def my_opener():
    opener = build_opener()
    opener.addheaders = header
    install_opener(opener)
    return opener

def get_imgs(sid,lid):
    try:
        url = base_url.format(sid, lid)
        req = Request(url, headers=header)
        res = urlopen(req).read().decode('utf-8')
        img_url = json.loads(res)['Code']
        file_name = img_url.split('yirenzhixia/')[1].replace('/', '-')
        print(file_name)
        urlretrieve(img_url, urljoin(base_dir,file_name))
    except Exception as e:
        pass

class MyThread(threading.Thread):

    def __init__(self, sid=None, lid=None):
        super (MyThread, self).__init__()
        self.sid = sid
        self.lid = lid

    def run(self):
        get_imgs(self.sid,self.lid)


if __name__ == "__main__":
    thread_list = []
    for pageid in range(1,412):
        for imgid in range(1,20):
            t = MyThread(sid=pageid, lid=imgid)
            thread_list.append(t)

    for i in thread_list:
        i.start()
        i.join()









