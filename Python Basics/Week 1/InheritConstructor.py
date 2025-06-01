# Types of variables
# Class variables - define inside the class
# Instance variable - define inside the constructor
class Calcul:
    num = 100
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def summation(self):
        return self.first + self.second

    def classsum(self):
        return self.first + self.second + Calcul.num
        #return self.first + self.second + self.num


obj = Calcul(1, 2)
print(obj.summation())

if __name__ == "__main__":
    obj1 = Calcul(50, 100)
    print(obj1.summation())
    print(obj1.classsum())