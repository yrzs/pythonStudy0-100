def main():
    # 二进制读取写入 实现文件复制
    try:
        with open('zuobiao2.png', 'rb') as fs1:
            data = fs1.read()
            print(data)
        with open('copy.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print("文件找不到")
    print("执行结束")


if __name__ == '__main__':
    main()
