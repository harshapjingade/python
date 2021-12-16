class A:
    def feature1(self):
        print("feature1 from class A")
class E:
    def feature5(self):
        print("feature5 from class E")

class B(A):
    def feature2(self):
        print("feature2 from class B")

class C(B): # multilevel inheritance
    def feature3(self):
        print("feature3 from class C")

class D(A,E): # multiple inheritance
    def feature4(self):
        print("feature4 from class D")

a1 = A()
b1 = B()
c1 = C()
d1 = D()
a1.feature1()
b1.feature1()

c1.feature1()
d1.feature1()