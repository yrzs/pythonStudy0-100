import json
from base64 import b64encode
from socket import socket
from threading import Thread

"""
    多线程处理多个用户请求的服务器
"""


def main():
    server = socket()
    server.bind(('192.168.1.139', 1234))
    server.listen(512)
    print("服务器开始监听...")
    with open('img/icon.png', 'rb') as f:
        # data = b64encode(f.read().decode('utf-8'))
        data = str(b64encode(f.read()), 'utf-8')

    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self._cclient = cclient

        def run(self):
            my_dict = {'filename': 'post.png', 'filedata': data}
            json_str = json.dumps(my_dict)
            self._cclient.send(json_str.encode('utf-8'))
            self._cclient.close()

    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
