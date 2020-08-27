class Person(object):

    # 限定可以绑定到类的属性
    __slots__ = ('_name', '_age', '_sex')

    def __init__(self, name, age):
        # _开头的属性，受保护的
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name


def main():
    person = Person('zzc', 23)
    print(person.name)
    person.name = 'yRzs'
    print(person.name)
    print(person.age)
    person.age = 33
    print(person.age)
    person._sex = '男'
    print(person._sex)


if __name__ == '__main__':
    main()
