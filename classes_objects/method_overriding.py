class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("class B")


b1 = B()
b1.show()