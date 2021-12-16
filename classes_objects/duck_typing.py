class vs:
    def execute(self):
        print("compiling")
        print("runnning")

class myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("runnning")


class laptop:
    def code(self,ide):
        ide.execute()

ide = vs()
myide = myeditor()

lap1 = laptop()
lap1.code(ide)
lap1.code(myide)