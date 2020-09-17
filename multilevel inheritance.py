# multilevel
class Grandparent():
    def __init__(self,name):
        self.name = name

class Parent(Grandparent):
    def display(self):
        print(__class__.__name__)

class Child(Parent):
    def __init__(self,name,age):
        super(Parent,self).__init__(name)
        self.age = age

c=Child("itv",10)
c.display()
print(c.name)
print(c.age)
