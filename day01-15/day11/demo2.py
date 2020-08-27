import time


def main():
    with open('wenquan.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
            time.sleep(0.5)


if __name__ == '__main__':
    main()
