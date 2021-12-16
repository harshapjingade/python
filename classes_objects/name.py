class Name:
    def __init__(self):
        self.name = "harsha"
        self.age = 29

    def compare(self,n2):
        if self.age == n2.age:
            return True
        else:
            return False

n1 = Name()
n2 = Name()
n2.age=30
if n1.compare(n2):
    print("same age")
else:
    print("different age")
