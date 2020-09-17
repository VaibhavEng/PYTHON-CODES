#single Inheritance
class Parent():
    def __init__(self,a):
        self.a=a

    def display(self):
        print("You are in parent class")

class Child(Parent):
    def __init__(self,a,b):
        #when there are same function name in
        #both child and parent class use:
        #1.super function
        #2. parent class name
        # to call the same function

        super(Child, self).__init__(a)
        self.b=b
    def greet (self):
        print("Good Afternoon")

    def display(self):
        Parent.display(self)
        
c=Child(10,20)
c.greet()
c.display()
print(c.a)
print(c.b)
