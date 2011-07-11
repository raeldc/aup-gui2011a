from abc import *

class MyClass:
    __metaclass__ = ABCMeta
    @abstractmethod
    def mymethod(self):
        pass

class NewClass(MyClass):
    pass

c = NewClass()
c.mymethod()