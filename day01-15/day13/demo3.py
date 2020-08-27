from random import randint
from threading import Thread
from time import sleep, time

"""
    重写线程类 
"""


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗时%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('python 从入门到放弃.pdf')
    t1.start()
    t2 = DownloadTask('python hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
