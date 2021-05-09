# Наследование подразумевает то, что дочерний класс содержит все атрибуты родительского класса,
#  при этом некоторые из них могут быть переопределены или добавлены в дочернем.

class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
 
class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p
 
class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = Table(100, 80, 70)
print(t1.length, t1.width, t1.height)

t2 = KitchenTable(110, 100, 90)
t2.setPlaces(50)
print(t2.places)

t3=DeskTable(50, 40, 30)
print(t3.square())