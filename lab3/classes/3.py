class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, len, wid):
        Shape.__init__(self)
        self.length = len
        self.width = wid
    
    def area(self):
        return self.length*self.width
a,b = map(int,input().split())
c = Rectangle(a,b)
print(c.area())