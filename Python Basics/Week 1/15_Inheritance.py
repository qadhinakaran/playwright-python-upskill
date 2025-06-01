from InheritConstructor import Calcul

class ChildImpl(Calcul):
    num2 = 200

    def __init__(self):
        Calcul.__init__(self, 10, 20)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getCompleteData())