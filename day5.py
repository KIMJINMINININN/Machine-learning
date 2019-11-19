class Person:
    name =""
    age = 0
    tel = ""

    def __init__(self, a, b, c): #생성자의 개념으로 생각하면 된다(초기화 시키는 변수)
        self.name = a
        self.age = b
        self.tel = c

    def printname(self):
        print(self.name)

    def printage(self):
        print(self.age)

    def printtel(self):
        print(self.tel)
    
    def sum(self, a, b):
        return a + b

a = [1,2,3,4,5]

a.append(6)
a.insert(0,7)
a.remove(6)
del a[1]