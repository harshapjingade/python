class Computer:

    def __init__(self,laptop,ram):
        self.laptop = laptop
        self.ram = ram

    def config(self):
        print("my system info is", self.laptop, self.ram)

com1 = Computer('mac',8)
com1.config()
