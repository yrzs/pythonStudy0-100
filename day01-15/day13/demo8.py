from time import time

"""
    1~100000000求和的计算密集型任务
"""


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    end = time()
    print(total)
    print('耗时：%.3fs' % (end - start))


if __name__ == '__main__':
    main()
