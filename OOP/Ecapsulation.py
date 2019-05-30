# private methods can only be accesed within the method
class myClass:
    def __display1(self):
        print("This is a pprivate method")

    def accesable(self):
        print("This is display2 method")
        self.__display1

class myClass2:
    __a = 10

    def display(self):
        print(self.__a)

obj = myClass()
obj.__display1()# This will not work
 # we cannot access the variable outside the class

#You cannot acces private methods or variables outside the class of the variables and methods
