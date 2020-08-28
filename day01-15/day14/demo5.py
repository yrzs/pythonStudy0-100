import json
from base64 import b64decode
from socket import socket


def main():
    client = socket()
    client.connect(('192.168.1.139', 1234))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = json.loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata']
    with open('img/' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print("接收到图片%s,保存于img/%s" % (filename, filename))


if __name__ == '__main__':
    main()
