class ParentClass:
    def __init__(self):
        print('Parent class')

    def my_method(self):
        print('Method of parent class')

class ChildClass(ParentClass):
    def __init__(self):
        print("Child's class")
        ParentClass.__init__(self)

    def my_method(self):
        print("Child's method")
        ParentClass.my_method(self)

a = ChildClass()
a.my_method()
