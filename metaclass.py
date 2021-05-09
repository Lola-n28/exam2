class MetaOne(type):
    def __new__(cls, name, bases, dict):
        pass

class MetaTwo(type):
    def __init__(self, name, bases, dict):
        pass

