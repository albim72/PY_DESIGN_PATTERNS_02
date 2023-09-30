from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance,0)

    def __set__(self, instance, value):
        if not(0<=value<=100):
            raise ValueError('ocena to wartość z przedziału 0-100')
        self._values[instance] = value


class ExamR:
    first_part = Grade()
    second_part = Grade()
    third_part = Grade()
