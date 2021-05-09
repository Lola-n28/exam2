class Number:
    def __init__(self):
        self.n = 10
 
    def sum(self, a):
        return self.n + int(a)
 
 
class String:
    def __init__(self):
        self.string = 'Hi'
 
    def sum(self, a):
        return len(self.string + str(a))
 
 
integer = Number()
string = String()
 
print(integer.sum(55))
print(string.sum(105))