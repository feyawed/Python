from collections.abc import MutableSequence
from dataclasses import dataclass


def indexing_decorator(func):
    def decorated(self, index, *args):
        return func(self, index, *args)

    return decorated


@dataclass
class Person:
    age: int = 1


class MyList(MutableSequence):
    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        if cls_type is None:
            self._inner_list = list([None])
        else:
            self._inner_list = list([Person()])

    def __len__(self):
        return len(self._inner_list)

    @indexing_decorator
    def __delitem__(self, index):
        self._inner_list.__delitem__(index)

    @indexing_decorator
    def insert(self, index, value):
        self._inner_list.insert(index, value)

    @indexing_decorator
    def __setitem__(self, index, value):
        self._inner_list.__setitem__(index, value)

    @indexing_decorator
    def __getitem__(self, index):
        return self._inner_list.__getitem__(index)

    def append(self, value):
        self.insert(len(self), value)

    def __str__(self):
        return self._inner_list.__str__()


a = MyList(cls_type=Person)
a[0].age = 5
a.append(4)

print(a)
