#multipe
class Parent1():
    def display(self):
        print(__class__.__name__)

class Parent2():
    def display(self):
        print(__class__.__name__)

class Child(Parent2, Parent1):
    def display(self):
        super(Child,self).display()
        Parent1.display(self)

c= Child()
c.display()
#c.disp
    
