class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature1 from class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
        
    def feature2(self):
        print("feature2 from class B")
        super().feature1()

b1 = B()
b1.feature2()