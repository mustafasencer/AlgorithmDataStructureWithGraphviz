import collections
import io
import typing
from abc import ABC, abstractmethod
import contextlib
import requests as requests


class Foo(ABC):

    def __init__(self, data: typing.Sequence):
        self.data = data
        self.index = 0

    def __hash__(self):
        return hash(self.data[0])

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.data == other.data

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1
        if len(self.data) == index:
            self.index = 0
            raise StopIteration
        return self.data[index]

    @abstractmethod
    def to_implement(self):
        raise NotImplementedError

    def __str__(self):
        return "hadi bakalim"

    def __repr__(self):
        return "hadi bakalim-----"


class ContextManager:
    def __init__(self):
        self.mutex = None

    def __enter__(self):
        self.mutex = 1

    def __exit__(self, *args):
        self.mutex = 0


def call_api():
    r = requests.get(
        "https://images.unsplash.com/photo-1452857576997-f0f12cd77844?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto"
        "=format&fit=crop&w=2850&q=80")
    with io.BytesIO() as buf:
        buf.write(r.content)
        buf.seek(0)

        requests.post(
            "https://api.telegram.org/bot<TOKEN>/sendPhoto?chat_id=<chat_id>",
            files={"photo": buf}
        )


def fun1(a):
    print("a:", a)
    a = 33
    print("local a:", a)
    a = 100


def generate_numbers(min_value, max_value):
    while min_value < max_value:
        yield min_value
        min_value += 1


if __name__ == '__main__':
    numbers = generate_numbers(10, 12)
    print(type(numbers))
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))

    with ContextManager() as cm:
        print(cm)
    lookup = {}
    tuple_1 = (1, 2, 3)
    list_1 = [1, 2, 3]
    foo_hash = hash(Foo([32]))

    list_1_id = id(list_1)
    print(dir(list_1))

    foo_1 = Foo([1])
    foo_1.to_implement()
    foo_2 = Foo([2])
    foo_3 = Foo([3])
    foo_4 = Foo([1])

    print(foo_1)
    print(foo_2)
    print(foo_3)
    print(foo_4)

    print(foo_1 == foo_4)
    print(foo_1 == foo_2)
    for i in foo_1:
        print(i)

    lookup[foo_1] = 1
    lookup[set] = 1
    lookup[list] = 2
    lookup[foo_2] = 2
    lookup[foo_3] = 3
    lookup[foo_4] = 4

    print(foo_1)
    print(foo_2)
    print(foo_3)
    print(foo_4)
    call_api()
