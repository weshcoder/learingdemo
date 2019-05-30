#Inheriting when you take information/features from different classes and add it into one or many other subclasses

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature2 is working")


class B():
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B, A):
    def feature5():
        print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()

c1.
#C is Inheriting from class B and Class A but neither of them are inheriting from any class they are called subclasses
