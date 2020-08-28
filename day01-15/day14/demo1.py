# -*- coding-8 -*-
import os
import re
from threading import Thread, Lock
from time import time
import requests
from bs4 import BeautifulSoup


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url
        self._lock = Lock()

    def run(self):
        self._lock.acquire()
        filename = self._url[self._url.rfind('/') + 1:]
        try:
            resp = requests.get(self._url)
            with open(os.getcwd() + '/img/' + filename, 'wb') as f:
                f.write(resp.content)
                print("已下载%s" % filename)
        finally:
            self._lock.release()


def main():
    response = requests.get('https://www.58pic.com/')
    if response.status_code != 200:
        print("请求失败")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.findAll("img")
    srcs = []
    for img_tag in img_tags:
        src = img_tag.get("src")
        if src is not None and src != '' and re.match(r'(\S*?jpg|\S*?png|\S*?svg)', src):
            if src[0:2] == '//':
                src = 'http:' + src
            srcs.append(src)
    img_src = list(set(srcs))  # list()的作用就是将字符串str或者元祖转换为数组
    img_src.sort(key=srcs.index)
    threads = []
    start = time()
    for src in img_src:
        t = DownloadHandler(src)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time()
    print("完成对千图网%d张图片的下载，耗时%.2fs" % (len(img_src), (end - start)))


if __name__ == '__main__':
    main()
