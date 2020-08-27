import os


def main():
    f = None
    try:
        f = open('wenquan.txt', 'r', encoding='utf-8')
        contents = f.readlines()
        for i in range(len(contents)):
            os.system('clear')
            print(contents[i])

    except FileNotFoundError:
        print("文件找不到")
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
