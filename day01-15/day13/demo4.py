from threading import Thread
from time import sleep

"""
    未加锁的多线程  临界资源混乱
"""


class Account(object):
    def __init__(self):
        self._balance = 0

    # 存款
    def deposit(self, money):
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance

    @property  # getter
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等待所有线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为￥%d元。' % account.balance)


if __name__ == '__main__':
    main()
