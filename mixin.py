class Mixin1(object):
    def test(self):
        print ("Mixin1")

class Mixin2(object):
    def test(self):
        print ("Mixin2")

class BaseClass(object):
    def test(self):
        print ("Base")

class MyClass(BaseClass, Mixin1, Mixin2):
    pass

x = MyClass()
x.test()